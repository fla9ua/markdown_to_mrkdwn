markdown_to_mrkdwn
==================

A library to convert Markdown to Slack's mrkdwn format.

Features
--------

- Supports conversion from Markdown to Slack's mrkdwn format.
- Supports nested lists and blockquotes.
- Handles inline code and images.

Installation
------------

You can install the package via pip:

.. code-block:: bash

    pip install markdown_to_mrkdwn

Usage
-----

Here's a simple example of how to use the library:

.. code-block:: python

    from markdown_to_mrkdwn import SlackMarkdownConverter

    converter = SlackMarkdownConverter()
    markdown_text = """
    # Header 1
    **Bold text**
    - List item
    [Link](https://example.com)
    """
    mrkdwn_text = converter.convert(markdown_text)
    print(mrkdwn_text)

Check the output in Slack Block Kit Builder:
`Slack Block Kit Builder <https://app.slack.com/block-kit-builder/T01R1PV07QQ#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22This%20is%20a%20mrkdwn%20section%20block%20:ghost:%20*this%20is%20bold*,%20and%20~this%20is%20crossed%20out~,%20and%20%3Chttps://google.com%7Cthis%20is%20a%20link%3E%22%7D%7D%5D%7D>`_

Contributing
------------

Contributions are welcome! Please feel free to submit a Pull Request.

License
-------

This project is licensed under the MIT License - see the `LICENSE <LICENSE>`_ file for details. 