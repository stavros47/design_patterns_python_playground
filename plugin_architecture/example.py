import json
from dataclasses import dataclass
from game import factory, loader


def main() -> None:
    """Creates game characters from a file."""

    # read data from a JSON file
    with open("./level.json") as file:
        data = json.load(file)

    # load the plugins
    loader.load_plugins(data["plugins"])

    # create the characters
    characters = [factory.create(item) for item in data["characters"]]

    # do something with the characters
    for character in characters:
        print(character, end="\t")
        character.make_a_noise()


if __name__ == "__main__":
    main()
