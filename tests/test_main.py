"""
Tests for PROMETHEUS Self-Evolving AI
"""

import pytest
from prometheus_self_evolving_ai import PROMETHEUSSelfEvolvingAI


@pytest.fixture
def system():
    return PROMETHEUSSelfEvolvingAI()


def test_initialization(system):
    assert system.version == "2.0.0"
    assert system.status == "Research"


def test_process(system):
    result = system.process({"test": "input"})
    assert result["status"] == "success"
    assert result["version"] == "2.0.0"


def test_info(system):
    info = system.get_info()
    assert info["name"] == "PROMETHEUS Self-Evolving AI"
    assert info["version"] == "2.0.0"
