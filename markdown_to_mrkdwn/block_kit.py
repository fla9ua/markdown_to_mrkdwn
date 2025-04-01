import re
import json
from typing import List, Dict, Any, Optional, Union
from .converter import SlackMarkdownConverter


class BlockKitConverter:
    """
    A converter class to transform Markdown text into Slack's Block Kit JSON format.

    This class converts Markdown elements to appropriate Block Kit blocks:
    - Headings → Section blocks with bold text
    - Paragraphs → Section blocks
    - Lists → Section blocks with formatted list items
    - Code blocks → Code blocks
    - Blockquotes → Section blocks with quote formatting
    - Tables → Section blocks with formatted text
    - Images → Image blocks
    - Horizontal rules → Divider blocks
    """

    def __init__(self):
        """
        Initializes the BlockKitConverter.
        """
        self.mrkdwn_converter = SlackMarkdownConverter()
        self.in_code_block = False
        self.code_block_content = []
        self.code_block_language = None

    def convert_to_blocks(self, markdown: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Convert Markdown text to Slack's Block Kit JSON format.

        Args:
            markdown (str): The Markdown text to convert.

        Returns:
            Dict[str, List[Dict[str, Any]]]: The converted text in Slack's Block Kit JSON format.
        """
        if not markdown:
            return {"blocks": []}

        # Reset state
        self.in_code_block = False
        self.code_block_content = []
        self.code_block_language = None

        blocks = []
        current_paragraph = []
        lines = markdown.strip().split("\n")
        i = 0

        while i < len(lines):
            line = lines[i]

            # Check for code block start/end
            code_block_match = re.match(r"^```(\w*)$", line)
            if code_block_match:
                if not self.in_code_block:
                    # Start of code block
                    # First, add any accumulated paragraph
                    if current_paragraph:
                        blocks.append(self._create_section_block("\n".join(current_paragraph)))
                        current_paragraph = []
                    
                    self.in_code_block = True
                    self.code_block_language = code_block_match.group(1) or None
                    self.code_block_content = []
                else:
                    # End of code block
                    blocks.append(self._create_code_block(
                        "\n".join(self.code_block_content),
                        self.code_block_language
                    ))
                    self.in_code_block = False
                    self.code_block_content = []
                    self.code_block_language = None
                i += 1
                continue

            if self.in_code_block:
                self.code_block_content.append(line)
                i += 1
                continue

            # Check for horizontal rule
            if re.match(r"^(---|\*\*\*|___)$", line):
                if current_paragraph:
                    blocks.append(self._create_section_block("\n".join(current_paragraph)))
                    current_paragraph = []
                blocks.append({"type": "divider"})
                i += 1
                continue

            # Check for table
            if i < len(lines) - 2 and line.startswith("|") and lines[i+1].startswith("|") and re.match(r"^\|[-:| ]+\|$", lines[i+1]):
                if current_paragraph:
                    blocks.append(self._create_section_block("\n".join(current_paragraph)))
                    current_paragraph = []
                
                table_lines = [line]
                j = i + 1
                while j < len(lines) and lines[j].startswith("|"):
                    table_lines.append(lines[j])
                    j += 1
                
                table_text = self.mrkdwn_converter.convert("\n".join(table_lines))
                blocks.append(self._create_section_block(table_text))
                i = j
                continue

            # Check for image
            image_match = re.match(r"!\[(.+?)\]\((.+?)\)", line)
            if image_match:
                if current_paragraph:
                    blocks.append(self._create_section_block("\n".join(current_paragraph)))
                    current_paragraph = []
                
                alt_text = image_match.group(1)
                image_url = image_match.group(2)
                blocks.append(self._create_image_block(image_url, alt_text))
                i += 1
                continue

            # Check for heading
            heading_match = re.match(r"^(#{1,3}) (.+)$", line)
            if heading_match:
                if current_paragraph:
                    blocks.append(self._create_section_block("\n".join(current_paragraph)))
                    current_paragraph = []
                
                heading_level = len(heading_match.group(1))
                heading_text = heading_match.group(2)
                blocks.append(self._create_header_block(heading_text, heading_level))
                i += 1
                continue

            # Check for list items (including task lists)
            list_match = re.match(r"^(\s*)[-*+] (?:\[([ xX])\] )?(.+)$", line)
            if list_match:
                # If we have a paragraph in progress, add it first
                if current_paragraph and not re.match(r"^(\s*)[-*+] (?:\[([ xX])\] )?(.+)$", current_paragraph[-1]):
                    blocks.append(self._create_section_block("\n".join(current_paragraph)))
                    current_paragraph = []
                
                # Add the list item to the current paragraph
                current_paragraph.append(line)
                i += 1
                continue

            # Check for blockquote
            if line.startswith(">"):
                if current_paragraph and not current_paragraph[-1].startswith(">"):
                    blocks.append(self._create_section_block("\n".join(current_paragraph)))
                    current_paragraph = []
                
                current_paragraph.append(line)
                i += 1
                continue

            # Regular paragraph text
            if line.strip():
                current_paragraph.append(line)
            else:
                # Empty line - end of paragraph
                if current_paragraph:
                    blocks.append(self._create_section_block("\n".join(current_paragraph)))
                    current_paragraph = []
            
            i += 1

        # Add any remaining paragraph
        if current_paragraph:
            blocks.append(self._create_section_block("\n".join(current_paragraph)))

        # Add any remaining code block
        if self.in_code_block and self.code_block_content:
            blocks.append(self._create_code_block(
                "\n".join(self.code_block_content),
                self.code_block_language
            ))

        return {"blocks": blocks}

    def _create_section_block(self, text: str) -> Dict[str, Any]:
        """
        Create a section block with the given text.

        Args:
            text (str): The text to include in the section.

        Returns:
            Dict[str, Any]: A section block.
        """
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": self.mrkdwn_converter.convert(text)
            }
        }

    def _create_header_block(self, text: str, level: int = 1) -> Dict[str, Any]:
        """
        Create a header block with the given text.

        Args:
            text (str): The header text.
            level (int): The heading level (1-3).

        Returns:
            Dict[str, Any]: A section block with formatted header text.
        """
        # Format as bold text
        formatted_text = f"*{text}*"
        
        # For h1, we can use the header block type
        if level == 1:
            return {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": text,
                    "emoji": True
                }
            }
        
        # For h2 and h3, use section blocks with bold text
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": formatted_text
            }
        }

    def _create_code_block(self, code: str, language: Optional[str] = None) -> Dict[str, Any]:
        """
        Create a code block with the given code.

        Args:
            code (str): The code to include in the block.
            language (Optional[str]): The programming language for syntax highlighting.

        Returns:
            Dict[str, Any]: A code block.
        """
        return {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"```{language or ''}\n{code}\n```"
            }
        }

    def _create_image_block(self, image_url: str, alt_text: str) -> Dict[str, Any]:
        """
        Create an image block with the given URL and alt text.

        Args:
            image_url (str): The URL of the image.
            alt_text (str): The alt text for the image.

        Returns:
            Dict[str, Any]: An image block.
        """
        return {
            "type": "image",
            "image_url": image_url,
            "alt_text": alt_text
        }
