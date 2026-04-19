from pydantic import BaseModel
from typing import Literal

class VideoInput(BaseModel):
    topic: str
    target_duration_seconds: int
    platform: Literal["youtube", "tiktok", "instagram_reels", "x", "linkedin"]
    target_audience: str
    tone: Literal["inspirational", "educational", "entertaining", "dramatic", "humorous", "documentary", "cinematic"]