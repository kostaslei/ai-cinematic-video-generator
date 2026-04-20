from pydantic import BaseModel, Field, field_validator
from schemas.concept_director import ConceptDirectorOutput
from schemas.video_input import VideoInput
from schemas.style import StyleOutput
from schemas.scene_breakdown import SceneBreakdownOutput
from schemas.narrative_script import NarrativeScriptOutput
from schemas.story import StoryOutput
from schemas.base import BaseAgentOutput
from typing import Literal


# INPUT

class EnvironmentAgentInput(BaseModel):
    idea: VideoInput
    story: StoryOutput
    concept: ConceptDirectorOutput
    style: StyleOutput
    scenes: SceneBreakdownOutput

# OUTPUT 

class EnvironmentLighting(BaseModel):
    time_of_day: str
    weather: str
    light_source: str
    shadow_quality: Literal["harsh", "soft", "diffuse", "none"]


class Environment(BaseModel):
    environment_id: str
    name: str
    physical_description: str
    lighting: EnvironmentLighting
    atmosphere: str
    consistency_anchor: str
    forbidden_elements: list[str]


class EnvironmentAgentOutput(BaseAgentOutput):
    environments: list[Environment]