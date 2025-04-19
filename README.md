# markdown_to_mrkdwn

[![MIT License](https://img.shields.io/badge/license-MIT-green.svg?style=flat-square)](https://opensource.org/licenses/MIT)
![GitHub release (latest by date)](https://img.shields.io/github/v/release/fla9ua/markdown_to_mrkdwn)
[![PyPI Version](https://img.shields.io/pypi/v/markdown-to-mrkdwn.svg?style=flat-square&logo=python&logoColor=white)](https://pypi.org/project/markdown-to-mrkdwn/)
[![PyPI Downloads](https://static.pepy.tech/badge/markdown-to-mrkdwn)](https://pepy.tech/projects/markdown-to-mrkdwn)
[![Python Unit Tests](https://github.com/fla9ua/markdown_to_mrkdwn/actions/workflows/python-tests.yml/badge.svg)](https://github.com/fla9ua/markdown_to_mrkdwn/actions/workflows/python-tests.yml)
[![codecov](https://codecov.io/gh/fla9ua/markdown_to_mrkdwn/branch/main/graph/badge.svg)](https://codecov.io/gh/fla9ua/markdown_to_mrkdwn)
[![Documentation](https://img.shields.io/badge/docs-latest-blue.svg?style=flat-square)](https://fla9ua.github.io/markdown_to_mrkdwn/)
[![GitHub Stars](https://img.shields.io/github/stars/fla9ua/markdown_to_mrkdwn?style=social)](https://github.com/fla9ua/markdown_to_mrkdwn)

A lightweight, efficient library for converting standard Markdown to Slack's mrkdwn format. This library helps you maintain consistent formatting when sending messages to Slack from your applications.

## Features

- Fast and lightweight conversion from Markdown to Slack's mrkdwn format
- No external dependencies
- Comprehensive support for Markdown elements:
  - Headings (H1, H2, H3, H4, H5, H6)
  - Text formatting (bold, italic, strikethrough)
  - Lists (ordered and unordered, with nesting)
  - Ordered lists (numbered lists with proper indentation)
  - Task lists (checked and unchecked items)
  - Tables (with header formatting)
  - Links and image references
  - Code blocks (with language specification preserved)
  - Blockquotes
  - Horizontal rules
- Preserves code blocks without converting their contents
- Handles special characters and edge cases

## Installation

Install from PyPI using pip:

```bash
pip install markdown_to_mrkdwn
```

Requirements:
- Python 3.8 or higher

## Usage

### Basic Usage

```python
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
```

### Output

```
*Heading 1*
*Bold text*
• List item
<https://example.com|Link>
~Strikethrough text~
```

### Supported Conversions

| Markdown | Slack mrkdwn |
|----------|--------------|
| `# Heading` | `*Heading*` |
| `## Heading` | `*Heading*` |
| `### Heading` | `*Heading*` |
| `#### Heading` | `*Heading*` |
| `##### Heading` | `*Heading*` |
| `###### Heading` | `*Heading*` |
| `**Bold**` | `*Bold*` |
| `__Bold__` | `*Bold*` |
| `*Italic*` | `_Italic_` |
| `~~Strikethrough~~` | `~Strikethrough~` |
| `[Link](https://example.com)` | `<https://example.com\|Link>` |
| `![Image](https://example.com/img.png)` | `<https://example.com/img.png>` |
| `- List item` | `• List item` |
| `1. Ordered item` | `1. Ordered item` |
| `- [ ] Task` | `• ☐ Task` |
| `- [x] Task` | `• ☑ Task` |
| `> Quote` | `> Quote` |
| `` `Code` `` | `` `Code` `` |
| `` ```python `` | `` ```python `` |
| `---` | `──────────` |
| Tables | Simple text tables with bold headers |

### Testing in Slack

You can test the output in Slack Block Kit Builder:
[Slack Block Kit Builder](https://app.slack.com/block-kit-builder/)

## Advanced Usage

### Custom Encoding

You can specify a custom encoding when initializing the converter:

```python
converter = SlackMarkdownConverter()
```

### Plugin System

The library supports a flexible plugin system that allows you to extend or customize the conversion process:

```python
from markdown_to_mrkdwn import SlackMarkdownConverter

# Create a converter instance
converter = SlackMarkdownConverter()

# Define a custom plugin function
def emoji_converter(line):
    """Convert emoji codes to actual emoji characters"""
    emoji_map = {
        ":smile:": "😊",
        ":thumbsup:": "👍",
        ":heart:": "❤️"
    }
    for code, emoji in emoji_map.items():
        line = line.replace(code, emoji)
    return line

# Register the plugin
converter.register_plugin(
    name="emoji_converter",
    converter_func=emoji_converter,
    priority=10,  # Lower numbers execute first
    scope="line"  # Process each line individually
)

# Convert markdown with emoji codes
markdown_text = "I :smile: this feature!"
mrkdwn_text = converter.convert(markdown_text)
# Result: "I 😊 this feature!"
```

#### Plugin Scopes

Plugins can operate at three different scopes:

- `global`: Process the entire text before any standard conversions
- `line`: Process each line individually (after standard line conversions)
- `block`: Process the entire text after all standard conversions

#### Plugin Management

You can manage plugins with these methods:

```python
# Get a list of registered plugins
plugins = converter.get_registered_plugins()

# Remove a plugin
converter.remove_plugin("emoji_converter")
```

### Error Handling

The converter will return the original markdown text if an error occurs during conversion:

```python
try:
    mrkdwn_text = converter.convert(markdown_text)
except Exception as e:
    print(f"Conversion error: {e}")
```

## Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Submit a pull request

Please make sure to update tests as appropriate.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
