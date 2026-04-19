import pytest
from unittest.mock import patch
from agents.scene_breakdown_agent import SceneBreakdownAgent
from schemas.story import StoryOutput
from schemas.narrative_script import NarrativeScriptOutput
from schemas.video_input import VideoInput
from schemas.scene_breakdown import SceneBreakdownInput, SceneBreakdownOutput
from schemas.concept_director import ConceptDirectorOutput
from tests.conftest import load_fixture

# Fixtures
@pytest.fixture
def agent():
    return SceneBreakdownAgent()

@pytest.fixture
def standard_input(video_input_fixture, story_fixture, concept_direction_fixture, script_fixture):
    return SceneBreakdownInput(
        idea=video_input_fixture,
        story=story_fixture,
        concept=concept_direction_fixture,
        script=script_fixture    
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
def script_fixture():
    data = load_fixture("narrative_script_response.json")
    return NarrativeScriptOutput(**data)

@pytest.fixture
def concept_direction_fixture():
    data = load_fixture("concept_director_response.json")
    return ConceptDirectorOutput(**data)


# TODO: LLM call behavior tests


# Live tests
@pytest.mark.live
def test_story_agent_live(standard_input):
    agent = SceneBreakdownAgent()
 
    result = agent.run(standard_input)
    #print(f"\nStory response: {result}\n")

    # shape
    assert isinstance(result, SceneBreakdownOutput)