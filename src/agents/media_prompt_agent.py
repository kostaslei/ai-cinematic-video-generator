
from llm.client import call_llm
from schemas.media_prompt import MediaPromptInput, MediaPromptOutput
from prompts.media_prompt import MEDIA_PROMPT_SYSTEM_PROMPT
from config import STRONG_MODEL

class MediaPromptAgent:

    def run(self, input: MediaPromptInput) -> MediaPromptOutput:
        #logger.info(f"StyleAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=MEDIA_PROMPT_SYSTEM_PROMPT,
            user=user_message,
            response_model=MediaPromptOutput,
            model=STRONG_MODEL,
            temperature=0.4
        )

        #logger.info(f"StyleAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: MediaPromptInput) -> str:
        return f"""
        MidJourney style suffix: {input.midjourney_style_suffix}
        Camera language: {input.camera_language}
        Pacing: {input.pacing}
        Visual motif: {input.visual_motif}
        Forbidden elements:: {input.forbidden_elements}
        Scenes: {input.scenes}
        Environments: {input.environments}
        Casting: {input.casting}
        """.strip()
