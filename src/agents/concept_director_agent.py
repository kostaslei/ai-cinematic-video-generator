
from llm.client import call_llm
from schemas.concept_director import ConceptDirectorInput, ConceptDirectorOutput
from prompts.concept_director import CONCEPT_DIRECTOR_SYSTEM_PROMPT
from config import BALANCED_MODEL

class ConceptDirectorAgent:

    def run(self, input: ConceptDirectorInput) -> ConceptDirectorOutput:
        #logger.info(f"ConceptDirectorAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=CONCEPT_DIRECTOR_SYSTEM_PROMPT,
            user=user_message,
            response_model=ConceptDirectorOutput,
            model=BALANCED_MODEL,
            temperature=0.7
        )

        #logger.info(f"ConceptDirectorAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: ConceptDirectorInput) -> str:
        return f"""
        Story concept: {input.story_concept}
        Video input: {input.video_input}
        """.strip()
