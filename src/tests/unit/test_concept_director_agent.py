import pytest
from unittest.mock import patch
from agents.concept_director_agent import ConceptDirectorAgent
from schemas.video_input import VideoInput
from schemas.story import StoryOutput
from schemas.concept_director import ConceptDirectorInput, ConceptDirectorOutput
from tests.conftest import load_fixture

# Fixtures
@pytest.fixture
def agent():
    return ConceptDirectorAgent()

@pytest.fixture
def standard_input(video_input_fixture, story_fixture):
    return ConceptDirectorInput(
        story_concept=story_fixture,
        video_input=video_input_fixture
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

@pytest.fixture
def story_fixture():
    data = load_fixture("story_response.json")
    return StoryOutput(**data)


# TODO: LLM call behavior tests


# Live tests
@pytest.mark.live
def test_story_agent_live(standard_input):
    agent = ConceptDirectorAgent()
 
    result = agent.run(standard_input)
    #print(f"\nStory response: {result}\n")

    # shape
    assert isinstance(result, ConceptDirectorOutput)