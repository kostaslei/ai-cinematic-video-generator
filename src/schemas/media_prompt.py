from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Literal
from enum import Enum
from schemas.base import BaseAgentOutput
from schemas.environment import EnvironmentLighting

# INPUT

class SceneForMediaPrompt(BaseModel):
    scene_id: str
    duration_seconds: int
    action: str
    mood: str


class CharacterAssignmentForMediaPrompt(BaseModel):
    character_id: str
    state_id: str
    consistency_anchor: str
    expression: str
    body_language: str
    position_note: str


class SceneCastForMediaPrompt(BaseModel):
    scene_id: str
    environment_id: str
    character_assignments: list[CharacterAssignmentForMediaPrompt]
    composition_note: str
    foreground_focus: str


class EnvironmentForMediaPrompt(BaseModel):
    environment_id: str
    consistency_anchor: str
    lighting: EnvironmentLighting
    forbidden_elements: list[str]


class MediaPromptInput(BaseModel):
    # Visual identity
    midjourney_style_suffix: str
    
    # Director constraints
    camera_language: str
    pacing: str
    visual_motif: str
    forbidden_elements: list[str]

    # Scenes — only what the prompt needs
    scenes: list[SceneForMediaPrompt]

    # Environments — anchor + lighting + forbidden only
    environments: list[EnvironmentForMediaPrompt]

    # Casting — already flattened with anchors and state details
    casting: list[SceneCastForMediaPrompt]


# OUTPUT

class ImagePrompt(BaseModel):
    scene_id: str
    prompt: str = Field(
        description="Full Midjourney-ready prompt. "
                    "Consistency anchors prepended, style suffix appended."
    )
    negative_prompt: str

    @field_validator("prompt")
    @classmethod
    def must_end_with_style_suffix(cls, v):
        assert "--" in v, "Prompt must include Midjourney technical parameters"
        return v

    @field_validator("negative_prompt")
    @classmethod
    def negative_not_empty(cls, v):
        assert len(v.strip()) > 0, "Negative prompt must not be empty"
        return v


class VideoPrompt(BaseModel):
    scene_id: str
    prompt: str = Field(
        description="Full Runway Gen-4 ready prompt. "
                    "Describes motion starting from the image frame."
    )
    camera_movement: str
    motion_intensity: Literal["static", "subtle", "moderate", "dynamic"]


class MediaPromptOutput(BaseAgentOutput):
    image_prompts: list[ImagePrompt]
    video_prompts: list[VideoPrompt]

    @model_validator(mode="after")
    def check_scene_parity(self):
        img_ids = {p.scene_id for p in self.image_prompts}
        vid_ids = {p.scene_id for p in self.video_prompts}
        assert img_ids == vid_ids, (
            f"Image/video scene mismatch. "
            f"Missing video: {img_ids - vid_ids}. "
            f"Missing image: {vid_ids - img_ids}."
        )
        return self

    @model_validator(mode="after")
    def check_scene_count(self):
        assert len(self.image_prompts) > 0, "No image prompts generated"
        assert len(self.video_prompts) > 0, "No video prompts generated"
        return self