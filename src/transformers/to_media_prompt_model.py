from schemas.concept_director import ConceptDirectorOutput
from schemas.style import StyleOutput
from schemas.scene_breakdown import SceneBreakdownOutput
from schemas.environment import EnvironmentAgentOutput
from schemas.casting import CastingOutput
from schemas.media_prompt import MediaPromptInput, SceneForMediaPrompt, SceneCastForMediaPrompt, EnvironmentForMediaPrompt

def build_media_prompt_input(
    concept: ConceptDirectorOutput,
    style: StyleOutput,
    scenes: SceneBreakdownOutput,
    environments: EnvironmentAgentOutput,
    casting: CastingOutput,
) -> MediaPromptInput:
    return MediaPromptInput(
        midjourney_style_suffix=style.midjourney_style_suffix,
        camera_language=concept.camera_language,
        pacing=concept.pacing,
        visual_motif=concept.visual_motif,
        forbidden_elements=concept.forbidden_elements,
        scenes=[
            SceneForMediaPrompt(
                scene_id=s.scene_id,
                duration_seconds=s.duration_seconds,
                action=s.action,
                mood=s.mood,
            )
            for s in scenes.scenes
        ],
        environments=[
            EnvironmentForMediaPrompt(
                environment_id=e.environment_id,
                consistency_anchor=e.consistency_anchor,
                lighting=e.lighting,
                forbidden_elements=e.forbidden_elements,
            )
            for e in environments.environments
        ],
        casting=[
            SceneCastForMediaPrompt(
                scene_id=sc.scene_id,
                environment_id=sc.environment_id,
                character_assignments=sc.character_assignments,
                composition_note=sc.composition_note,
                foreground_focus=sc.foreground_focus,
            )
            for sc in casting.scene_casts
        ],
    )