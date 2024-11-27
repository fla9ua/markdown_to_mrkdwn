import re
import markdown2


class SlackMarkdownConverter:
    """
    A library to convert standard Markdown to Slack's mrkdwn format.

    Supports conversion of common Markdown elements while respecting Slack's
    specific formatting requirements.
    """

    @staticmethod
    def convert(markdown_text):
        """
        Convert standard Markdown to Slack's mrkdwn format.

        Args:
            markdown_text (str): Input Markdown text to be converted.

        Returns:
            str: Converted Slack-compatible markdown text.
        """
        try:
            # First, convert Markdown to HTML using markdown2
            html = markdown2.markdown(markdown_text)

            # Convert HTML to Slack-compatible markdown
            slack_markdown = SlackMarkdownConverter._html_to_slack_markdown(html)

            return slack_markdown
        except Exception as e:
            raise ValueError(f"Error converting markdown: {e}")

    @staticmethod
    def _html_to_slack_markdown(html):
        """
        Convert HTML to Slack markdown format.

        Args:
            html (str): HTML generated from Markdown conversion.

        Returns:
            str: Slack-compatible markdown text.
        """
        # Replace headers with Slack's bold or italic formatting
        html = re.sub(r"<h1>(.*?)</h1>", r"*\1* ", html)
        html = re.sub(r"<h2>(.*?)</h2>", r"*\1*", html)
        html = re.sub(r"<h3>(.*?)</h3>", r"_\1_", html)

        # Bold and Italics
        html = re.sub(r"<strong>(.*?)</strong>", r"*\1*", html)
        html = re.sub(r"<em>(.*?)</em>", r"_\1_", html)

        # Code blocks and inline code
        html = re.sub(
            r"<pre><code>(.*?)</code></pre>", r"```\1```", html, flags=re.DOTALL
        )
        html = re.sub(r"<code>(.*?)</code>", r"`\1`", html)

        # Unordered and ordered lists
        html = re.sub(
            r"<ul>(.*?)</ul>",
            lambda m: SlackMarkdownConverter._convert_list(m.group(1), ordered=False),
            html,
            flags=re.DOTALL,
        )
        html = re.sub(
            r"<ol>(.*?)</ol>",
            lambda m: SlackMarkdownConverter._convert_list(m.group(1), ordered=True),
            html,
            flags=re.DOTALL,
        )

        # Remove any remaining HTML tags
        html = re.sub(r"<[^>]+>", "", html)

        return html.strip()

    @staticmethod
    def _convert_list(list_content, ordered=False):
        """
        Convert HTML list items to Slack list format.

        Args:
            list_content (str): HTML list content.
            ordered (bool): Whether the list is ordered or unordered.

        Returns:
            str: Slack-formatted list.
        """
        list_items = re.findall(r"<li>(.*?)</li>", list_content, re.DOTALL)

        formatted_items = []
        for index, item in enumerate(list_items, start=1):
            clean_item = item.strip()
            if ordered:
                formatted_items.append(f"{index}. {clean_item}")
            else:
                formatted_items.append(f"• {clean_item}")

        return "\n".join(formatted_items)


# Example usage
if __name__ == "__main__":
    markdown_example = """
# Hello World

This is a **bold** and _italic_ text.

## Code Example

```python
def hello():
    print("Hello, Slack!")
```

- List item 1
- List item 2
"""

    slack_markdown = SlackMarkdownConverter.convert(markdown_example)
    print(slack_markdown)
