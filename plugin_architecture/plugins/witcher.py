"""Game extension that adds a bard character."""
from dataclasses import dataclass
from game import factory


@dataclass
class Witcher:
    name: str

    def make_a_noise(self) -> None:
        print("Hmm..")


def initialize() -> None:
    factory.register("witcher", Witcher)
