"""Example tests for my_package.

These tests demonstrate the testing patterns that work well with
Claude-powered automated maintenance.
"""

import pytest
from my_package import hello, add, __version__


class TestHello:
    """Tests for the hello function."""

    def test_default_greeting(self):
        """Test default greeting."""
        assert hello() == "Hello, World!"

    def test_custom_name(self):
        """Test greeting with custom name."""
        assert hello("Claude") == "Hello, Claude!"

    def test_empty_name(self):
        """Test greeting with empty string."""
        assert hello("") == "Hello, !"


class TestAdd:
    """Tests for the add function."""

    def test_positive_integers(self):
        """Test adding positive integers."""
        assert add(2, 3) == 5

    def test_negative_integers(self):
        """Test adding negative integers."""
        assert add(-1, -1) == -2

    def test_mixed_signs(self):
        """Test adding numbers with mixed signs."""
        assert add(-5, 10) == 5

    def test_floats(self):
        """Test adding floats."""
        result = add(1.5, 2.5)
        assert result == pytest.approx(4.0)

    def test_zero(self):
        """Test adding zero."""
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0


class TestVersion:
    """Tests for package version."""

    def test_version_exists(self):
        """Test that version is defined."""
        assert __version__ is not None

    def test_version_format(self):
        """Test that version follows semver format."""
        parts = __version__.split(".")
        assert len(parts) >= 2
        assert all(p.isdigit() for p in parts[:2])
