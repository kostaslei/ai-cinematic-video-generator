from pydantic import BaseModel, Field, field_validator, model_validator
from typing import Literal
from enum import Enum
from schemas.base import BaseAgentOutput
from schemas.video_input import VideoInput
from schemas.scene_breakdown import SceneBreakdownOutput
from schemas.character import CharacterAgentOutput
from schemas.environment import EnvironmentAgentOutput
from schemas.concept_director import ConceptDirectorOutput

# INPUT

class CastingInput(BaseModel):
    idea: VideoInput
    concept: ConceptDirectorOutput
    scenes: SceneBreakdownOutput
    characters: CharacterAgentOutput
    environments: EnvironmentAgentOutput

    @model_validator(mode="after")
    def validate_ids_available(self):
        char_ids = {c.character_id for c in self.characters.characters}
        env_ids = {e.environment_id for e in self.environments.environments}
        assert len(char_ids) > 0, "No characters to cast."
        assert len(env_ids) > 0, "No environments to cast."
        return self

# OUTPUT

class SceneCast(BaseModel):
    scene_id: str
    environment_id: str
    character_assignments: list[dict] = Field(
        description="Each entry: {character_id, state_id, position_note}"
    )
    foreground_focus: str
    composition_note: str


class CastingOutput(BaseAgentOutput):
    scene_casts: list[SceneCast]

    def validate_coverage(self, scenes: SceneBreakdownOutput):
        expected = {s.scene_id for s in scenes.scenes}
        actual = {sc.scene_id for sc in self.scene_casts}
        missing = expected - actual
        assert not missing, f"Scenes missing cast assignments: {missing}"

    def validate_references(
        self,
        characters: CharacterAgentOutput,
        environments: EnvironmentAgentOutput,
    ):
        char_ids = {c.character_id for c in characters.characters}
        state_ids_by_char = {
            c.character_id: {s.state_id for s in c.states}
            for c in characters.characters
        }
        env_ids = {e.environment_id for e in environments.environments}

        for cast in self.scene_casts:
            assert cast.environment_id in env_ids, (
                f"Scene {cast.scene_id}: unknown environment '{cast.environment_id}'"
            )
            for assignment in cast.character_assignments:
                cid = assignment["character_id"]
                sid = assignment["state_id"]
                assert cid in char_ids, f"Scene {cast.scene_id}: unknown character '{cid}'"
                assert sid in state_ids_by_char[cid], (
                    f"Scene {cast.scene_id}: unknown state '{sid}' for character '{cid}'"
                )