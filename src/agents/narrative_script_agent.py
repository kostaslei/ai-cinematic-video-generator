
from llm.client import call_llm
from schemas.narrative_script import NarrativeScriptInput, NarrativeScriptOutput
from prompts.narrative_script import NARRATIVE_SCRIPT_SYSTEM_PROMPT
from config import BALANCED_MODEL

class NarrativeScriptAgent:

    def run(self, input: NarrativeScriptInput) -> NarrativeScriptOutput:
        #logger.info(f"StyleAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=NARRATIVE_SCRIPT_SYSTEM_PROMPT,
            user=user_message,
            response_model=NarrativeScriptOutput,
            model=BALANCED_MODEL,
            temperature=0.8
        )

        #logger.info(f"StyleAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: NarrativeScriptInput) -> str:
        return f"""
        Story concept: {input.story_concept}
        Director concept: {input.director_concept}
        Idea: {input.idea}
        Style: {input.style}
        """.strip()
