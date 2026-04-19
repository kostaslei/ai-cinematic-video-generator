from pydantic import BaseModel, Field
from schemas.concept_director import ConceptDirectorOutput
from schemas.video_input import VideoInput
from schemas.narrative_script import NarrativeScriptOutput
from schemas.story import StoryOutput
from schemas.base import BaseAgentOutput
from typing import Literal


# INPUT
class SceneBreakdownInput(BaseModel):
    idea: VideoInput
    story: StoryOutput
    concept: ConceptDirectorOutput
    script: NarrativeScriptOutput

# OUTPUT

class Scene(BaseModel):
    scene_id: str = Field(description="E.g. 'sc_01'")
    duration_seconds: int
    narrative_beat: str = Field(description="Which part of the arc this scene covers.")
    action: str = Field(description="What physically happens on screen.")
    mood: str
    narration_segment: str = Field(description="Which VO lines play over this scene.")
    transition_to_next: Literal["cut", "fade", "match_cut", "whip_pan", "dissolve", "none"]

class SceneBreakdownOutput(BaseAgentOutput):
    scenes: list[Scene]
    total_scenes: int
    total_duration_seconds: int