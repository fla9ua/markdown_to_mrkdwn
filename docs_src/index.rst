.. markdown_to_mrkdwn documentation master file, created by
   sphinx-quickstart on Thu Dec  5 00:42:06 2024.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

markdown_to_mrkdwn
=================

A lightweight, efficient library for converting standard Markdown to Slack's mrkdwn format.

Features
--------

- Fast and lightweight conversion from Markdown to Slack's mrkdwn format
- No external dependencies
- Comprehensive support for Markdown elements:

  - Headings (H1, H2, H3)
  - Text formatting (bold, italic, strikethrough)
  - Lists (ordered and unordered, with nesting)
  - Task lists (checked and unchecked items)
  - Tables (with header formatting)
  - Links and image references
  - Code blocks (with language specification)
  - Blockquotes
  - Horizontal rules

- Preserves code blocks without converting their contents
- Handles special characters and edge cases

Installation
-----------

Install from PyPI using pip:

.. code-block:: bash

    pip install markdown_to_mrkdwn

Requirements:

- Python 3.8 or higher

Usage
-----

Basic Usage
~~~~~~~~~~

.. code-block:: python

    from markdown_to_mrkdwn import SlackMarkdownConverter

    # Create a converter instance
    converter = SlackMarkdownConverter()

    # Convert markdown to mrkdwn
    markdown_text = """
    # Heading 1
    **Bold text**
    - List item
    [Link](https://example.com)
    ~~Strikethrough text~~
    """
    mrkdwn_text = converter.convert(markdown_text)
    print(mrkdwn_text)

API Reference
------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:
   
   modules
