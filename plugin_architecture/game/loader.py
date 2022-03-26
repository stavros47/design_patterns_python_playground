"""A simple plugin loader."""

import importlib


class PluginInterface:
    """A plugin has a single function to initialize a plugin."""

    @staticmethod
    def initialize() -> None:
        """Initialize a plugin."""


def import_module(name: str) -> PluginInterface:
    return importlib.import_module(name)  # type: ignore


def load_plugins(plugins: list[str]) -> None:
    """Load a list of plugins"""
    for plugin_name in plugins:
        plugin = import_module(plugin_name)
        plugin.initialize()
