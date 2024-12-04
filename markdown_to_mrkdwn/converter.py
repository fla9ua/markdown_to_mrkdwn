import re
from typing import List, Tuple


class SlackMarkdownConverter:
    """
    A converter class to transform Markdown text into Slack's mrkdwn format.

    Attributes:
        encoding (str): The character encoding used for the conversion.
        patterns (List[Tuple[str, str]]): A list of regex patterns and their replacements.
    """

    def __init__(self, encoding="utf-8"):
        """
        Initializes the SlackMarkdownConverter with a specified encoding.

        Args:
            encoding (str): The character encoding to use for the conversion. Default is 'utf-8'.
        """
        self.encoding = encoding
        self.patterns: List[Tuple[str, str]] = [
            (r"!\[.*?\]\((.+?)\)", r"<\1>"),  # Images to URL
            (r"^### (.+)$", r"*\1* "),  # H3 as bold
            (r"^## (.+)$", r"*\1* "),  # H2 as bold
            (r"^# (.+)$", r"*\1* "),  # H1 as bold
            (r"\*\*(.+?)\*\*", r"*\1* "),  # Bold
            (r"__(.+?)__", r"*\1* "),  # Underline as bold
            (r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"_\1_ "),  # Italic
            (r"\[(.+?)\]\((.+?)\)", r"<\2|\1> "),  # Links
            (r"`(.+?)`", r"`\1` "),  # Inline code
            (r"^- (.+)", r"• \1"),  # Unordered list
            (r"^> (.+)", r"> \1"),  # Blockquote
            (r"(---|\*\*\*|___)", r"──────────"),  # Horizontal rule
        ]

    def convert(self, markdown: str) -> str:
        """
        Convert Markdown text to Slack's mrkdwn format.

        Args:
            markdown (str): The Markdown text to convert.

        Returns:
            str: The converted text in Slack's mrkdwn format.
        """
        if not markdown:
            return ""

        try:
            lines = markdown.split("\n")
            converted_lines = [self._convert_line(line) for line in lines]
            return (
                "\n".join(converted_lines)
                .strip()
                .encode(self.encoding)
                .decode(self.encoding)
            )
        except Exception:
            return markdown

    def _convert_line(self, line: str) -> str:
        """
        Convert a single line of Markdown.

        Args:
            line (str): A single line of Markdown text.

        Returns:
            str: The converted line in Slack's mrkdwn format.
        """
        original_line = line
        for pattern, replacement in self.patterns:
            if line == original_line:
                line = re.sub(r"^(\s*)- (.+)", r"\1• \2", line, flags=re.MULTILINE)
                line = re.sub(pattern, replacement, line, flags=re.MULTILINE)
            else:
                break  # Stop if any pattern has already changed the line

        return line.rstrip()
