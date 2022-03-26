"""Represents a basic character."""

from typing import Protocol


class GameCharacter(Protocol):
    """Basic Representation of a game character."""

    def make_a_noise(self) -> None:
        """Let the character make a noise."""
