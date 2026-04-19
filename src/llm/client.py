import json
import time
import logging
from typing import Type, TypeVar
from openai import OpenAI, RateLimitError, APIConnectionError, APIError

import config
from models.schemas import BaseAgentOutput

logger = logging.getLogger(__name__)

T = TypeVar("T", bound=BaseAgentOutput)

client = OpenAI(api_key=config.OPENAI_API_KEY)


# ─────────────────────────────────────────
# Core call
# ─────────────────────────────────────────

def call_llm(
    *,
    system: str,
    user: str,
    response_model: Type[T],
    model: str = config.DEFAULT_MODEL,
    max_tokens: int = config.DEFAULT_MAX_TOKENS,
    temperature: float = 0.7,
    retries: int = 3,
) -> T:
    last_error = None

    for attempt in range(1, retries + 1):
        try:
            logger.info(f"LLM call → {response_model.__name__} (attempt {attempt}/{retries})")

            response = client.chat.completions.create(
                model=model,
                max_completion_tokens=max_tokens,
                temperature=temperature,
                response_format={"type": "json_object"},   # native JSON mode
                messages=[
                    {"role": "system", "content": _build_system_prompt(system, response_model)},
                    {"role": "user",   "content": user},
                ],
            )

            usage = response.usage
            logger.info(f"Tokens used — input: {usage.prompt_tokens}, output: {usage.completion_tokens}")

            return _parse_response(response, response_model)

        except RateLimitError as e:
            wait = 2 ** attempt
            logger.warning(f"Rate limited. Waiting {wait}s before retry...")
            time.sleep(wait)
            last_error = e

        except APIConnectionError as e:
            logger.warning(f"Connection error on attempt {attempt}: {e}")
            time.sleep(1)
            last_error = e

        except APIError as e:
            logger.error(f"OpenAI API error (no retry): {e}")
            raise

        except ValueError as e:
            logger.error(f"Failed to parse LLM response into {response_model.__name__}: {e}")
            raise

    raise RuntimeError(f"LLM call failed after {retries} attempts. Last error: {last_error}")


# ─────────────────────────────────────────
# Internal helpers
# ─────────────────────────────────────────

def _build_system_prompt(base_system: str, response_model: Type[T]) -> str:
    schema = response_model.model_json_schema()
    return (
        f"{base_system}\n\n"
        f"You must respond ONLY with a valid JSON object that matches this schema:\n"
        f"{schema}\n"
        f"No explanation, no markdown, no code fences. Raw JSON only."
    )


def _parse_response(response, response_model: Type[T]) -> T:
    raw_text = response.choices[0].message.content.strip()

    # Defensive strip in case JSON mode still wraps in fences
    if raw_text.startswith("```"):
        raw_text = raw_text.split("```")[1]
        if raw_text.startswith("json"):
            raw_text = raw_text[4:]
        raw_text = raw_text.strip()

    try:
        data = json.loads(raw_text)
    except json.JSONDecodeError as e:
        raise ValueError(f"LLM returned invalid JSON: {e}\nRaw output:\n{raw_text}")

    return response_model.model_validate(data)