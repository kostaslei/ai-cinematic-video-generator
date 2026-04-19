
from llm.client import call_llm
from schemas.video_input import VideoInput
from schemas.story import StoryOutput
from prompts.story import STORY_SYSTEM_PROMPT
from config import BALANCED_MODEL

class StoryAgent:

    def run(self, input: VideoInput) -> StoryOutput:
        #logger.info(f"StoryAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=STORY_SYSTEM_PROMPT,
            user=user_message,
            response_model=StoryOutput,
            model=BALANCED_MODEL,
            temperature=0.9
        )

        #logger.info(f"StoryAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: VideoInput) -> str:
        return f"""
        Topic: {input.topic}
        Target duration seconds: {input.target_duration_seconds}
        Platform: {input.platform}
        Target audience: {input.target_audience}
        Tone: {input.tone}
        """.strip()
