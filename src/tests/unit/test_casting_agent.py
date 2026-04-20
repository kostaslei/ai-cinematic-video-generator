import pytest
from unittest.mock import patch
from agents.casting_agent import CastingAgent
from schemas.casting import CastingInput, CastingOutput
from schemas.video_input import VideoInput
from schemas.scene_breakdown import SceneBreakdownOutput
from schemas.character import CharacterAgentOutput
from schemas.concept_director import ConceptDirectorOutput
from schemas.environment import EnvironmentAgentOutput
from tests.conftest import load_fixture

# Fixtures
@pytest.fixture
def agent():
    return CastingAgent()

@pytest.fixture
def standard_input(video_input_fixture, concept_fixture, scenes_fixture, character_fixture, environment_fixture):
    return CastingInput(
        idea=video_input_fixture,
        concept=concept_fixture,
        scenes=scenes_fixture,
        characters=character_fixture,
        environments=environment_fixture
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
def scenes_fixture():
    data = load_fixture("scene_breakdown_response.json")
    return SceneBreakdownOutput(**data)

@pytest.fixture
def concept_fixture():
    data = load_fixture("concept_director_response.json")
    return ConceptDirectorOutput(**data)

@pytest.fixture
def character_fixture():
    data = load_fixture("character_response.json")
    return CharacterAgentOutput(**data)

@pytest.fixture
def environment_fixture():
    data = load_fixture("environment_response.json")
    return EnvironmentAgentOutput(**data)

# TODO: LLM call behavior tests


# Live tests
@pytest.mark.live
def test_story_agent_live(standard_input):
    agent = CastingAgent()
 
    result = agent.run(standard_input)
    #print(f"\nStory response: {result}\n")

    # shape
    assert isinstance(result, CastingOutput)