# This file is required to make Python treat the directory as a package

from .converter import SlackMarkdownConverter

__version__ = "0.1.6"
__all__ = ["SlackMarkdownConverter"]
