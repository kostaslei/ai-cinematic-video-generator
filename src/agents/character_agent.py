
from llm.client import call_llm
from schemas.character import CharacterAgentInput, CharacterAgentOutput
from prompts.character import CHARACTER_SYSTEM_PROMPT
from config import STRONG_MODEL

class CharacterAgent:

    def run(self, input: CharacterAgentInput) -> CharacterAgentOutput:
        #logger.info(f"StyleAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=CHARACTER_SYSTEM_PROMPT,
            user=user_message,
            response_model=CharacterAgentOutput,
            model=STRONG_MODEL,
            temperature=0.8
        )

        #logger.info(f"StyleAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: CharacterAgentInput) -> str:
        return f"""
        Idea: {input.idea}
        Story: {input.story}
        Concept: {input.concept}
        Style: {input.style}
        Scenes: {input.scenes}
        """.strip()
