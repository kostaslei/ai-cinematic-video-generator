
from llm.client import call_llm
from schemas.scene_breakdown import SceneBreakdownInput, SceneBreakdownOutput
from prompts.scene_breakdown import SCENE_BREAKDOWN_SYSTEM_PROMPT
from config import BALANCED_MODEL

class SceneBreakdownAgent:

    def run(self, input: SceneBreakdownInput) -> SceneBreakdownOutput:
        #logger.info(f"StyleAgent starting — topic: '{input.topic}', platform: {input.platform}")

        user_message = self._build_user_message(input)
        
        result = call_llm(
            system=SCENE_BREAKDOWN_SYSTEM_PROMPT,
            user=user_message,
            response_model=SceneBreakdownOutput,
            model=BALANCED_MODEL,
            temperature=0.3
        )

        #logger.info(f"StyleAgent done — OUTPUT:\n {result}")
        return result

    def _build_user_message(self, input: SceneBreakdownInput) -> str:
        return f"""
        Idea: {input.idea}
        Story: {input.story}
        Concept: {input.concept}
        Script: {input.script}
        """.strip()
