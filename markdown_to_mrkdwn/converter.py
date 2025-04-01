import re
import logging
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
        self.in_code_block = False
        # Use compiled regex patterns for better performance
        self.patterns: List[Tuple[re.Pattern, str]] = [
            (re.compile(r"^(\s*)- (.+)", re.MULTILINE), r"\1• \2"),  # Unordered list
            (re.compile(r"!\[.*?\]\((.+?)\)", re.MULTILINE), r"<\1>"),  # Images to URL
            (re.compile(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", re.MULTILINE), r"_\1_"),  # Italic
            (re.compile(r"^### (.+)$", re.MULTILINE), r"*\1*"),  # H3 as bold
            (re.compile(r"^## (.+)$", re.MULTILINE), r"*\1*"),  # H2 as bold
            (re.compile(r"^# (.+)$", re.MULTILINE), r"*\1*"),  # H1 as bold
            (re.compile(r"(^|\s)~\*\*(.+?)\*\*(\s|$)", re.MULTILINE), r"\1 *\2* \3"),  # Bold with space handling
            (re.compile(r"(?<!\*)\*\*(.+?)\*\*(?!\*)", re.MULTILINE), r"*\1*"),  # Bold
            (re.compile(r"__(.+?)__", re.MULTILINE), r"*\1*"),  # Underline as bold
            (re.compile(r"\[(.+?)\]\((.+?)\)", re.MULTILINE), r"<\2|\1>"),  # Links
            (re.compile(r"`(.+?)`", re.MULTILINE), r"`\1`"),  # Inline code
            (re.compile(r"^> (.+)", re.MULTILINE), r"> \1"),  # Blockquote
            (re.compile(r"^(---|\*\*\*|___)$", re.MULTILINE), r"──────────"),  # Horizontal line
            (re.compile(r"~~(.+?)~~", re.MULTILINE), r"~\1~"),  # Strikethrough
        ]
        # Placeholders for triple emphasis
        self.triple_start = "%%BOLDITALIC_START%%"
        self.triple_end = "%%BOLDITALIC_END%%"

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
            # Remove leading and trailing whitespace
            markdown = markdown.strip()
            lines = markdown.split("\n")
            converted_lines = [self._convert_line(line) for line in lines]
            return (
                "\n".join(converted_lines)
                .encode(self.encoding)
                .decode(self.encoding)
            )
        except Exception as e:
            # Log the error for debugging
            logging.error(f"Markdown conversion error: {str(e)}")
            return markdown

    def _convert_line(self, line: str) -> str:
        """
        Convert a single line of Markdown.

        Args:
            line (str): A single line of Markdown text.

        Returns:
            str: The converted line in Slack's mrkdwn format.
        """
        # Detect code block start/end (supports language specification)
        if re.match(r"^```(\w*)$", line):
            self.in_code_block = not self.in_code_block
            return line

        # Skip conversion if inside code block
        if self.in_code_block:
            return line

        # Process bold and italic text
        line = re.sub(
            r"(?<!\*)\*\*\*([^*\n]+?)\*\*\*(?!\*)",
            lambda m: f"{self.triple_start}{m.group(1)}{self.triple_end}",
            line,
        )

        # Apply compiled patterns
        for pattern, replacement in self.patterns:
            line = pattern.sub(replacement, line)

        line = re.sub(
            re.escape(self.triple_start) + r"(.*?)" + re.escape(self.triple_end),
            r"*_\1_*",
            line,
            flags=re.MULTILINE,
        )

        return line.rstrip()
