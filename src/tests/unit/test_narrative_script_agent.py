import pytest
from unittest.mock import patch
from agents.narrative_script_agent import NarrativeScriptAgent
from schemas.story import StoryOutput
from schemas.style import StyleOutput
from schemas.video_input import VideoInput
from schemas.narrative_script import NarrativeScriptInput, NarrativeScriptOutput
from schemas.concept_director import ConceptDirectorOutput
from tests.conftest import load_fixture

# Fixtures
@pytest.fixture
def agent():
    return NarrativeScriptAgent()

@pytest.fixture
def standard_input(video_input_fixture, story_fixture, style_fixture, concept_direction_fixture):
    return NarrativeScriptInput(
        story_concept=story_fixture,
        director_concept=concept_direction_fixture,
        style=style_fixture,
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

@pytest.fixture
def story_fixture():
    data = load_fixture("story_response.json")
    return StoryOutput(**data)

@pytest.fixture
def style_fixture():
    data = load_fixture("style_response.json")
    return StyleOutput(**data)

@pytest.fixture
def concept_direction_fixture():
    data = load_fixture("concept_director_response.json")
    return ConceptDirectorOutput(**data)


# TODO: LLM call behavior tests


# Live tests
@pytest.mark.live
def test_story_agent_live(standard_input):
    agent = NarrativeScriptAgent()
 
    result = agent.run(standard_input)
    #print(f"\nStory response: {result}\n")

    # shape
    assert isinstance(result, NarrativeScriptOutput)