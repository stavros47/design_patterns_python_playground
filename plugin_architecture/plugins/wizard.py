"""Game extension that adds a wizard character."""
from dataclasses import dataclass
from game import factory


@dataclass
class Wizard:
    name: str

    def make_a_noise(self) -> None:
        print("Fireball!!")


def initialize() -> None:
    factory.register("wizard", Wizard)
