# markdown_to_mrkdwn

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/fla9ua/markdown_to_mrkdwn)
[![PyPI Version](https://img.shields.io/pypi/v/markdown-to-mrkdwn.svg?style=flat-square&logo=python&logoColor=white)](https://pypi.org/project/markdown-to-mrkdwn/)
[![PyPI Downloads](https://static.pepy.tech/badge/markdown-to-mrkdwn)](https://pepy.tech/projects/markdown-to-mrkdwn)
[![Python Unit Tests](https://github.com/fla9ua/markdown_to_mrkdwn/actions/workflows/python-tests.yml/badge.svg)](https://github.com/fla9ua/markdown_to_mrkdwn/actions/workflows/python-tests.yml)
[![codecov](https://codecov.io/gh/fla9ua/markdown_to_mrkdwn/branch/main/graph/badge.svg)](https://codecov.io/gh/fla9ua/markdown_to_mrkdwn)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg?style=flat-square)](https://fla9ua.github.io/markdown_to_mrkdwn/)
[![GitHub Stars](https://img.shields.io/github/stars/fla9ua/markdown_to_mrkdwn?style=social)](https://github.com/fla9ua/markdown_to_mrkdwn)

A library for converting Markdown to Slack's mrkdwn format

## Features

- Supports conversion from Markdown to Slack's mrkdwn format
- Supports nested lists, quotes, inline code, and image URLs

## Installation

```bash
pip install markdown_to_mrkdwn
```

## Usage

Here's a simple example of how to use the library:

```python
from markdown-to-mrkdwn import SlackMarkdownConverter

converter = SlackMarkdownConverter()
markdown_text = """
# header1
**bold text**
- list
[link](https://example.com)
"""
mrkdwn_text = converter.convert(markdown_text)
print(mrkdwn_text)
```

Check the output in Slack Block Kit Builder:
[Slack Block Kit Builder](https://app.slack.com/block-kit-builder/T01R1PV07QQ#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22This%20is%20a%20mrkdwn%20section%20block%20:ghost:%20*this%20is%20bold*,%20and%20~this%20is%20crossed%20out~,%20and%20%3Chttps://google.com%7Cthis%20is%20a%20link%3E%22%7D%7D%5D%7D)

## Contributing

Feel free to send pull requests and issues

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
