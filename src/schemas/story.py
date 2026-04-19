from pydantic import BaseModel, Field
from schemas.base import BaseAgentOutput
from schemas.video_input import VideoInput


# INPUT
class StoryInput(BaseModel):
    idea: VideoInput

# OUTPUT

class StoryOutput(BaseAgentOutput):
    logline: str = Field(description="One sentence. The whole story.")
    premise: str = Field(description="3-5 sentences. The core idea and why it matters to the audience.")
    narrative_arc: str = Field(description="Beginning / turning point / resolution — explicit beats.")
    central_conflict: str
    emotional_journey: str = Field(description="What emotion does the viewer feel at start vs end?")
    core_message: str = Field(description="The one thing the viewer should remember.")
    unique_angle: str = Field(description="What makes this version of the topic different from the 1000 others on this platform?")