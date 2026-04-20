import pytest
from unittest.mock import patch
from agents.character_agent import CharacterAgent
from schemas.story import StoryOutput
from schemas.narrative_script import NarrativeScriptOutput
from schemas.video_input import VideoInput
from schemas.scene_breakdown import SceneBreakdownOutput
from schemas.concept_director import ConceptDirectorOutput
from schemas.style import StyleOutput
from schemas.character import CharacterAgentInput, CharacterAgentOutput
from tests.conftest import load_fixture

# Fixtures
@pytest.fixture
def agent():
    return CharacterAgent()

@pytest.fixture
def standard_input(video_input_fixture, story_fixture, style_fixture, concept_direction_fixture, script_fixture, scenes_fixture):
    return CharacterAgentInput(
        idea=video_input_fixture,
        story=story_fixture,
        style=style_fixture,
        concept=concept_direction_fixture,
        scenes=scenes_fixture
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
def script_fixture():
    data = load_fixture("narrative_script_response.json")
    return NarrativeScriptOutput(**data)

@pytest.fixture
def concept_direction_fixture():
    data = load_fixture("concept_director_response.json")
    return ConceptDirectorOutput(**data)

@pytest.fixture
def scenes_fixture():
    data = load_fixture("scene_breakdown_response.json")
    return SceneBreakdownOutput(**data)


# TODO: LLM call behavior tests


# Live tests
@pytest.mark.live
def test_story_agent_live(standard_input):
    agent = CharacterAgent()
 
    result = agent.run(standard_input)
    #print(f"\nStory response: {result}\n")

    # shape
    assert isinstance(result, CharacterAgentOutput)