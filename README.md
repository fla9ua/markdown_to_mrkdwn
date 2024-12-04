# markdown_to_mrkdwn

A library to convert Markdown to Slack's mrkdwn format.

## Features

- Convert headers, bold, italic, links, and more from Markdown to Slack's mrkdwn.
- Supports nested lists and blockquotes.
- Handles inline code and images.

## Installation

You can install the package via pip:

```bash
pip install markdown_to_mrkdwn
```

## Usage

Here's a simple example of how to use the library:

```python
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
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.