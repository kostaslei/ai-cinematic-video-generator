
from llm.client import call_llm
from schemas.story import StoryInput, StoryOutput
from prompts.story import STORY_SYSTEM_PROMPT
from config import STRONG_MODEL

class StoryAgent:

    def run(self, input: StoryInput) -> StoryOutput:
        #logger.info(f"StoryAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=STORY_SYSTEM_PROMPT,
            user=user_message,
            response_model=StoryOutput,
            model=STRONG_MODEL,
            temperature=0.9
        )

        #logger.info(f"StoryAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: StoryInput) -> str:
        return f"""
        Topic: {input.idea.topic}
        Target duration seconds: {input.idea.target_duration_seconds}
        Platform: {input.idea.platform}
        Target audience: {input.idea.target_audience}
        Tone: {input.idea.tone}
        """.strip()
