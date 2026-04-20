
from llm.client import call_llm
from schemas.casting import CastingInput, CastingOutput
from prompts.casting import CASTING_SYSTEM_PROMPT
from config import BALANCED_MODEL

class CastingAgent:

    def run(self, input: CastingInput) -> CastingOutput:
        #logger.info(f"StyleAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=CASTING_SYSTEM_PROMPT,
            user=user_message,
            response_model=CastingOutput,
            model=BALANCED_MODEL,
            temperature=0.2
        )

        #logger.info(f"StyleAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: CastingInput) -> str:
        return f"""
        Idea: {input.idea}
        Concept: {input.concept}
        Scenes: {input.scenes}
        Characters: {input.characters}
        Environments: {input.environments}
        """.strip()
