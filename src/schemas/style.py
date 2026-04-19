from pydantic import BaseModel, Field
from schemas.concept_director import ConceptDirectorOutput
from schemas.video_input import VideoInput
from schemas.story import StoryOutput
from schemas.base import BaseAgentOutput
from typing import Literal


# INPUT
class StyleInput(BaseModel):
    idea: VideoInput
    story_concept: StoryOutput
    concept_direction: ConceptDirectorOutput

# OUTPUT
class ColorPalette(BaseModel):
    primary: str = Field(description="Dominant color as hex")
    secondary: str
    accent: str
    background: str
    emotional_logic: str = Field(description="Why these colors serve the story's emotion.")

class StyleOutput(BaseAgentOutput):
    color_palette: ColorPalette
    lighting_style: str = Field(description="E.g. 'high contrast chiaroscuro', 'soft overcast naturalistic'.")
    texture_and_grain: str = Field(description="E.g. 'film grain 35mm', 'clean digital', 'painted watercolor'.")
    typography_style: str = Field(description="Font character for any text overlays.")
    aspect_ratio: Literal["16:9", "9:16", "1:1", "4:5"]
    negative_space_usage: Literal["minimal", "moderate", "heavy"]
    midjourney_style_suffix: str = Field(description="Ready-to-append MJ style string. E.g. '--style raw --ar 9:16 --v 6'.")