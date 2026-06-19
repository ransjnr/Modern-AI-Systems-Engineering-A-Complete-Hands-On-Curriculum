import pytest
from pydantic import ValidationError
from app.build_schemas import BuildRequest

def test_validation():
    with pytest.raises(ValidationError):
        BuildRequest(task="too short")

def test_valid_request():
    r = BuildRequest(task="Write a function that reverses a string with asserts.")
    assert r.task.startswith("Write")
