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

class CharacterAgentInput(BaseModel):
    idea: VideoInput
    story: StoryOutput
    concept: ConceptDirectorOutput
    style: StyleOutput
    scenes: SceneBreakdownOutput

# OUTPUT

class CharacterState(BaseModel):
    state_id: str
    expression: str
    body_language: str
    wardrobe_note: str


class Character(BaseModel):
    character_id: str
    role: str
    visual_description: str
    base_wardrobe: str
    states: list[CharacterState]
    consistency_anchor: str = Field(description="3-5 most distinctive visual features.")

    @field_validator("states")
    @classmethod
    def at_least_one_state(cls, v):
        assert len(v) >= 1, "Each character must have at least one state."
        return v


class CharacterAgentOutput(BaseModel):
    characters: list[Character]
