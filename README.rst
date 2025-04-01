markdown_to_mrkdwn
==================

A lightweight, efficient library for converting standard Markdown to Slack's mrkdwn format. This library helps you maintain consistent formatting when sending messages to Slack from your applications.

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
------------

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

Output
~~~~~~

.. code-block:: text

    *Heading 1*
    *Bold text*
    • List item
    <https://example.com|Link>
    ~Strikethrough text~

Supported Conversions
~~~~~~~~~~~~~~~~~~~~

+----------------------------------+----------------------------------+
| Markdown                         | Slack mrkdwn                     |
+==================================+==================================+
| ``# Heading``                    | ``*Heading*``                    |
+----------------------------------+----------------------------------+
| ``## Heading``                   | ``*Heading*``                    |
+----------------------------------+----------------------------------+
| ``### Heading``                  | ``*Heading*``                    |
+----------------------------------+----------------------------------+
| ``**Bold**``                     | ``*Bold*``                       |
+----------------------------------+----------------------------------+
| ``__Bold__``                     | ``*Bold*``                       |
+----------------------------------+----------------------------------+
| ``*Italic*``                     | ``_Italic_``                     |
+----------------------------------+----------------------------------+
| ``~~Strikethrough~~``            | ``~Strikethrough~``              |
+----------------------------------+----------------------------------+
| ``[Link](https://example.com)``  | ``<https://example.com|Link>``   |
+----------------------------------+----------------------------------+
| ``![Image](https://example.com/img.png)`` | ``<https://example.com/img.png>`` |
+----------------------------------+----------------------------------+
| ``- List item``                  | ``• List item``                  |
+----------------------------------+----------------------------------+
| ``- [ ] Task``                   | ``• ☐ Task``                     |
+----------------------------------+----------------------------------+
| ``- [x] Task``                   | ``• ☑ Task``                     |
+----------------------------------+----------------------------------+
| ``> Quote``                      | ``> Quote``                      |
+----------------------------------+----------------------------------+
| ````Code````                     | ````Code````                     |
+----------------------------------+----------------------------------+
| ``---``                          | ``──────────``                   |
+----------------------------------+----------------------------------+
| Tables                           | Simple text tables with bold headers |
+----------------------------------+----------------------------------+

Testing in Slack
~~~~~~~~~~~~~~~

You can test the output in `Slack Block Kit Builder <https://app.slack.com/block-kit-builder/>`_.

Advanced Usage
-------------

Custom Encoding
~~~~~~~~~~~~~~

You can specify a custom encoding when initializing the converter:

.. code-block:: python

    converter = SlackMarkdownConverter(encoding="latin-1")

Error Handling
~~~~~~~~~~~~~

The converter will return the original markdown text if an error occurs during conversion:

.. code-block:: python

    try:
        mrkdwn_text = converter.convert(markdown_text)
    except Exception as e:
        print(f"Conversion error: {e}")

Contributing
------------

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: ``git checkout -b feature/your-feature-name``
3. Commit your changes: ``git commit -am 'Add some feature'``
4. Push to the branch: ``git push origin feature/your-feature-name``
5. Submit a pull request

Please make sure to update tests as appropriate.

License
-------

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`_ file for details.
