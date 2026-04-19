import json
import pytest
from pathlib import Path
from unittest.mock import patch, MagicMock

def load_fixture(name: str) -> dict:
    path = Path(__file__).parent / "fixtures" / name
    return json.loads(path.read_text())

@pytest.fixture
def mock_llm():
    """Reusable fixture that patches call_llm for any test that needs it."""
    with patch("llm.client.call_llm") as mock:
        yield mock