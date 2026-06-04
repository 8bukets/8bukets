import pytest
import os
from utils import validate_output_path

class TestSecurity:
    def test_validate_output_path_valid(self):
        """Test that valid paths in CWD are accepted."""
        # Current directory
        cwd = os.getcwd()
        path = "test.json"
        assert validate_output_path(path) == os.path.join(cwd, path)

        # Subdirectory (assumed valid as long as it's under CWD)
        # Note: validate_output_path doesn't check if directory EXISTS, just if it's safe.
        path = "subdir/test.json"
        assert validate_output_path(path) == os.path.join(cwd, "subdir", "test.json")

    def test_validate_output_path_traversal(self):
        """Test that traversal attempts raise ValueError."""
        # This assumes we are not at the filesystem root, which is safe for this env
        with pytest.raises(ValueError, match="Security Error"):
            validate_output_path("../outside.json")

        with pytest.raises(ValueError, match="Security Error"):
            validate_output_path("/etc/passwd")

    def test_validate_output_path_custom_base(self):
        """Test that validation works with a custom base directory."""
        cwd = os.getcwd()
        base = os.path.join(cwd, "agents")

        # Valid inside base
        path = os.path.join(base, "test.json")
        # We pass absolute path to simulate what validate_output_path does internally for relative
        # But wait, validate_output_path(filepath) calls abspath(filepath).
        # If I pass "test.json", it resolves to CWD/test.json.
        # If I want it to be inside 'agents', I must pass "agents/test.json" OR run from inside agents.

        # Let's test providing a full path that IS inside base
        full_path_inside = os.path.join(base, "test.json")
        assert validate_output_path(full_path_inside, base_dir=base) == full_path_inside

        # Invalid: outside base (even if inside CWD!)
        full_path_outside = os.path.join(cwd, "outside_agents.json")
        with pytest.raises(ValueError, match="Security Error"):
            validate_output_path(full_path_outside, base_dir=base)

    def test_validate_output_path_empty(self):
        """Test that empty or None paths raise ValueError."""
        with pytest.raises(ValueError, match="Output path cannot be empty"):
            validate_output_path(None)

        with pytest.raises(ValueError, match="Output path cannot be empty"):
            validate_output_path("")
