import pytest
from pydantic import ValidationError
from app.schemas import TriageRequest
from app.tools import symptom_reference

def test_validation_rejects_short():
    with pytest.raises(ValidationError):
        TriageRequest(complaint="hi")

def test_reference_known():
    out = symptom_reference.run("chest pain")
    assert "red_flags" in out and "HIGH" in out

def test_reference_unknown():
    assert "No curated reference" in symptom_reference.run("left elbow tingle")
