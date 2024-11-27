# markdown_to_mrkdwn

## Overview

`markdown_to_mrkdwn` is a Python library that converts standard Markdown to Slack's mrkdwn (Markdown-like) format, ensuring compatibility with Slack's specific formatting requirements.

## Installation

```bash
pip install markdown-to-mrkdwn
```

## Requirements

- Python 3.7+
- markdown2 library

## Quick Start

```python
from markdown_to_mrkdwn import SlackMarkdownConverter

markdown_text = """
# Hello World

This is a **bold** text with _italic_ style.
"""

slack_markdown = SlackMarkdownConverter.convert(markdown_text)
print(slack_markdown)
```

## Features

- Convert standard Markdown to Slack-compatible format
- Support for headers, bold, italic, code blocks, and lists
- Simple and intuitive API
- Lightweight and easy to integrate

## Dependencies

Required dependencies are listed in `requirements.txt`:

```
markdown2>=2.4.0
pytest>=7.3.1
```

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Testing

Run tests using pytest:

```bash
pytest tests/
```

## Performance Considerations

- Designed for efficient Markdown to Slack conversion
- Minimal overhead
- Supports most common Markdown elements

## Limitations

- Complex nested Markdown structures might require additional parsing
- Some advanced Markdown features may not be fully supported

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Project Link: [https://github.com/02tYasui/markdown_to_mrkdwn](https://github.com/02tYasui/markdown_to_mrkdwn)
```