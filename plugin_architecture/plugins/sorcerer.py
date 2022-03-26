"""Game extension that adds a bard character."""
from dataclasses import dataclass
from game import factory


@dataclass
class Sorcerer:
    name: str

    def make_a_noise(self) -> None:
        print("Aaaargh!")


def initialize() -> None:
    factory.register("sorcerer", Sorcerer)
