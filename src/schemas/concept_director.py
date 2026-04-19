from pydantic import BaseModel, Field
from schemas.video_input import VideoInput
from schemas.story import StoryOutput
from schemas.base import BaseAgentOutput
from typing import Literal
from enum import Enum

# INPUT
class ConceptDirectorInput(BaseModel):
    story_concept: StoryOutput
    video_input: VideoInput

# OUTPUT
class ShotStyle(str, Enum):
    CINEMATIC = "cinematic"
    DOCUMENTARY = "documentary"
    VLOG = "vlog"
    MOTION_GRAPHICS = "motion_graphics"
    MIXED = "mixed"

class ConceptDirectorOutput(BaseAgentOutput):
    shot_style: ShotStyle
    pacing: Literal["slow_build", "rapid_cut", "rhythmic", "static_contemplative"]
    genre_anchors: list[str] = Field(description="2-4 reference genres or visual styles. E.g. 'nature documentary', 'noir thriller'.")
    opening_technique: str = Field(description="Specific technique for the first 3 seconds. E.g. 'extreme close-up followed by fast zoom out'.")
    visual_motif: str = Field(description="A recurring visual element that ties scenes together.")
    camera_language: str = Field(description="Dominant camera movements and framing rules for this video.")
    forbidden_elements: list[str] = Field(description="Visual or narrative elements to explicitly avoid for this story.")