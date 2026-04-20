
from llm.client import call_llm
from schemas.narrative_script import NarrativeScriptInput, NarrativeScriptOutput
from prompts.narrative_script import NARRATIVE_SCRIPT_SYSTEM_PROMPT
from config import STRONG_MODEL

WORDS_PER_SECOND = {
    "slow_build": 2.0,
    "static_contemplative": 2.2,
    "rhythmic": 2.8,
    "rapid_cut": 3.2,
}

class NarrativeScriptAgent:

    def run(self, input: NarrativeScriptInput) -> NarrativeScriptOutput:
        #logger.info(f"StyleAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=NARRATIVE_SCRIPT_SYSTEM_PROMPT,
            user=user_message,
            response_model=NarrativeScriptOutput,
            model=STRONG_MODEL,
            temperature=0.8
        )

        #logger.info(f"StyleAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: NarrativeScriptInput) -> str:
        total_duration=input.idea.target_duration_seconds
        rate = WORDS_PER_SECOND[input.director_concept.pacing]
        max_words = int(total_duration * rate * 0.92)
        return f"""
        Story: {input.story_concept}
        Concept: {input.director_concept}
        Pipeline Input: {input.idea}
        Style: {input.style}
        Total duration: {total_duration}
        Max_words: {max_words}
        Word rate: {rate}
        """.strip()
