import os
import pytest
from app.main import transcribe

def test_transcribe_short_sample():
    sample = "tests/sample.wav"
    if os.path.exists(sample):
        text = transcribe(sample)
        assert isinstance(text, str)
        assert len(text) > 0
    else:
        pytest.skip("sample.wav not present")
