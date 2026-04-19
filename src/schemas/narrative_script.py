from pydantic import BaseModel, Field
from schemas.concept_director import ConceptDirectorOutput
from schemas.story import StoryOutput
from schemas.base import BaseAgentOutput
from schemas.video_input import VideoInput
from schemas.style import StyleOutput
from schemas.concept_director import ConceptDirectorOutput
from typing import Literal


# INPUT

class NarrativeScriptInput(BaseModel):
    idea: VideoInput
    story_concept: StoryOutput
    director_concept: ConceptDirectorOutput
    style: StyleOutput

# OUTPUT

class AudioCue(BaseModel):
    timestamp_hint: str = Field(description="Relative position. E.g. 'opening', 'scene_2', 'climax', 'outro'.")
    cue_type: Literal["sfx", "music_in", "music_out", "music_swell", "ambient"]
    description: str

class NarrativeScriptOutput(BaseAgentOutput):
    full_narration: str = Field(description="Complete VO script. Formatted with [PAUSE], [EMPHASIS] markers.")
    hook_line: str = Field(description="Exact opening line. Must work as a standalone hook.")
    word_count: int
    estimated_spoken_duration_seconds: int
    audio_cues: list[AudioCue]
    music_brief: str = Field(description="Genre, tempo BPM range, emotional arc for the music.")
    narration_style: str = Field(description="Delivery instructions for TTS or human VO. E.g. 'conversational, intimate, slight urgency'.")