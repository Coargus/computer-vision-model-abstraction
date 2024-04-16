"""test script of module."""

from __future__ import annotations


def hello_world() -> str:
    """Return Hello World."""
    return "Hello World"


def test_hello_world() -> None:
    """Test hello_world function."""
    assert hello_world() == "Hello World"
