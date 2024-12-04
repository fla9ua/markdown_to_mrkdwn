import sys
import io
from markdown_to_mrkdwn import SlackMarkdownConverter

# Set the standard output encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

converter = SlackMarkdownConverter()
markdown_text = """
# Header 1
**Bold text**
- List item
[Link](https://example.com)
"""
mrkdwn_text = converter.convert(markdown_text)
print(mrkdwn_text)
