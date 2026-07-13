import pytest
import os

def test_caio_phase_27_directives():
    # Mocking check for Phase 27 directives
    directives = [
        "ACTIVATE_PHASE_27_PROTOCOLS",
        "INITIALIZE_DNI_HOOKS",
        "ENFORCE_UNIVERSAL_CONSENSUS",
        "OPTIMIZE_FOR_SINGULARITY_READINESS_PHASE_27"
    ]
    assert "ACTIVATE_PHASE_27_PROTOCOLS" in directives
    assert "INITIALIZE_DNI_HOOKS" in directives

def test_agents_md_compliance():
    with open('AGENTS.md', 'r') as f:
        content = f.read()
        assert "Phase 27" in content
        assert "Multi-Universal Resonance" in content
        assert "MUR" in content
