import re
import logging

class SlackMarkdownConverter:
    def __init__(self, log_level=logging.WARNING):
        logging.basicConfig(level=log_level)
        self.patterns = [
            # More complex and ordered patterns
            (r'^# (.+)$', r'*\1*'),  # H1 as bold
            (r'^## (.+)$', r'*\1*'),  # H2 as bold
            (r'\*\*(.+?)\*\*', r'*\1*'),  # Bold
            (r'__(.+?)__', r'*\1*'),  # Underline as bold
            (r'(?<!\*)\*(.+?)\*(?!\*)', r'_\1_'),  # Italic
            (r'\[(.+?)\]\((.+?)\)', r'<\2|\1>'),  # Links
            (r'`(.+?)`', r'`\1`'),  # Inline code
            (r'^- (.+)', r'• \1'),  # Unordered list
            (r'^> (.+)', r'> \1'),  # Blockquote
            (r'!\[.*?\]\((.+?)\)', r'<\1>'),  # Images to URL
            (r'---|___|\*\*\*', r'──────────'),  # Horizontal rule
        ]
    
    def convert(self, markdown: str) -> str:
        """Convert Markdown to Slack's mrkdwn format."""
        try:
            lines = markdown.split('\n')
            converted_lines = [
                self._convert_line(line) for line in lines
            ]
            return '\n'.join(converted_lines)
        except Exception as e:
            logging.error(f"Conversion error: {e}")
            return markdown

    def _convert_line(self, line: str) -> str:
        """Convert a single line of Markdown."""
        for pattern, replacement in self.patterns:
            line = re.sub(pattern, replacement, line, flags=re.MULTILINE)
        return line