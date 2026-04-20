import pytest
from unittest.mock import patch
from agents.media_prompt_agent import MediaPromptAgent
from schemas.casting import CastingOutput
from schemas.style import StyleOutput
from schemas.media_prompt import MediaPromptInput, MediaPromptOutput
from transformers.to_media_prompt_model import build_media_prompt_input
from schemas.scene_breakdown import SceneBreakdownOutput
from schemas.character import CharacterAgentOutput
from schemas.concept_director import ConceptDirectorOutput
from schemas.environment import EnvironmentAgentOutput
from tests.conftest import load_fixture

# Fixtures
@pytest.fixture
def agent():
    return MediaPromptAgent()

@pytest.fixture
def standard_input(concept_fixture, style_fixture, scenes_fixture, environment_fixture, casting_fixture):
    return build_media_prompt_input(
        concept=concept_fixture,
        style=style_fixture,
        scenes=scenes_fixture,
        environments=environment_fixture,
        casting=casting_fixture
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
def style_fixture():
    data = load_fixture("style_response.json")
    return StyleOutput(**data)

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

@pytest.fixture
def casting_fixture():
    data = load_fixture("casting_response.json")
    return CastingOutput(**data)

# TODO: LLM call behavior tests


# Live tests
@pytest.mark.live
def test_story_agent_live(standard_input):
    print(standard_input)
    agent = MediaPromptAgent()
 
    result = agent.run(standard_input)
    #print(f"\nStory response: {result}\n")

    # shape
    assert isinstance(result, MediaPromptOutput)