
from llm.client import call_llm
from schemas.style import StyleInput, StyleOutput
from prompts.style import STYLE_SYSTEM_PROMPT
from config import BALANCED_MODEL

class StyleAgent:

    def run(self, input: StyleInput) -> StyleOutput:
        #logger.info(f"StyleAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=STYLE_SYSTEM_PROMPT,
            user=user_message,
            response_model=StyleOutput,
            model=BALANCED_MODEL,
            temperature=0.8
        )

        #logger.info(f"StyleAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: StyleInput) -> str:
        return f"""
        idea: {input.idea}
        Story concept: {input.story_concept}
        Concept direction: {input.concept_direction}
        """.strip()
