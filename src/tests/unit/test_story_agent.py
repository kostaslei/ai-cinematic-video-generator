import pytest
from unittest.mock import patch
from agents.story_agent import StoryAgent
from schemas.video_input import VideoInput
from schemas.story import StoryOutput, StoryInput
#from tests.conftest import load_fixture

# Fixtures
@pytest.fixture
def agent():
    return StoryAgent()

@pytest.fixture
def standard_input(video_input_fixture):
    return StoryInput(
        idea=video_input_fixture
    )

@pytest.fixture
def video_input_fixture():
    return VideoInput(
        topic="Theogony: Clash of the Titans",
        target_audience="general public",
        tone="cinematic",
        target_duration_seconds=45,
        platform="tiktok",
    )


# TODO: LLM call behavior tests


# Live tests
@pytest.mark.live
def test_story_agent_live(standard_input):
    agent = StoryAgent()
 
    result = agent.run(standard_input)
    #print(f"\nStory response: {result}\n")

    # shape
    assert isinstance(result, StoryOutput)