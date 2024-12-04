import re
import logging
from typing import List, Tuple


class SlackMarkdownConverter:
    def __init__(self, log_level=logging.WARNING):
        logging.basicConfig(
            level=log_level, format="%(asctime)s - %(levelname)s: %(message)s"
        )
        self.logger = logging.getLogger(__name__)
        self.patterns: List[Tuple[str, str]] = [
            (r"!\[.*?\]\((.+?)\)", r"<\1>"),  # Images to URL
            (r"^### (.+)$", r"*\1*"),  # H3 as bold
            (r"^## (.+)$", r"*\1*"),  # H2 as bold
            (r"^# (.+)$", r"*\1*"),  # H1 as bold
            (r"\*\*(.+?)\*\*", r"*\1*"),  # Bold
            (r"__(.+?)__", r"*\1*"),  # Underline as bold
            (r"(?<!\*)\*([^*\n]+?)\*(?!\*)", r"_\1_"),  # Italic
            (r"\[(.+?)\]\((.+?)\)", r"<\2|\1>"),  # Links
            (r"`(.+?)`", r"`\1`"),  # Inline code (preserve)
            (r"^- (.+)", r"• \1"),  # Unordered list
            (r"^> (.+)", r"> \1"),  # Blockquote
            (r"(---|\*\*\*|___)", r"──────────"),  # Horizontal rule
        ]

    def convert(self, markdown: str) -> str:
        """Convert Markdown to Slack's mrkdwn format."""
        if not markdown:
            return ""

        try:
            lines = markdown.split("\n")
            converted_lines = [self._convert_line(line) for line in lines]
            return "\n".join(converted_lines).strip()
        except Exception as e:
            self.logger.error(f"Conversion error: {e}")
            return markdown

    def _convert_line(self, line: str) -> str:
        """Convert a single line of Markdown."""
        original_line = line
        for pattern, replacement in self.patterns:
            # Apply each pattern only if the line hasn't been changed by a previous pattern
            if line == original_line:
                # Handle nested lists by checking for leading spaces followed by a dash
                line = re.sub(r"^(\s*)- (.+)", r"\1• \2", line, flags=re.MULTILINE)
                line = re.sub(pattern, replacement, line, flags=re.MULTILINE)
            else:
                break  # Stop if any pattern has already changed the line

        return line.rstrip()
