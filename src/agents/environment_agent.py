
from llm.client import call_llm
from schemas.environment import EnvironmentAgentInput, EnvironmentAgentOutput
from prompts.environment import ENVIRONMENT_SYSTEM_PROMPT
from config import STRONG_MODEL

class EnvironmentAgent:

    def run(self, input: EnvironmentAgentInput) -> EnvironmentAgentOutput:
        #logger.info(f"StyleAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=ENVIRONMENT_SYSTEM_PROMPT,
            user=user_message,
            response_model=EnvironmentAgentOutput,
            model=STRONG_MODEL,
            temperature=0.8
        )

        #logger.info(f"StyleAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: EnvironmentAgentInput) -> str:
        return f"""
        Idea: {input.idea}
        Story: {input.story}
        Concept: {input.concept}
        Style: {input.style}
        Scenes: {input.scenes}
        """.strip()
