import re
import logging
from typing import List, Tuple, Dict, Callable, Any, Optional


class SlackMarkdownConverter:
    """
    A converter class to transform Markdown text into Slack's mrkdwn format.

    Attributes:
        encoding (str): The character encoding used for the conversion.
        patterns (List[Tuple[str, str]]): A list of regex patterns and their replacements.
        plugins (Dict[str, Dict[str, Any]]): A dictionary of registered plugins.
        plugin_order (List[str]): A list of plugin names in execution order.
    """

    def __init__(self, encoding="utf-8"):
        """
        Initializes the SlackMarkdownConverter with a specified encoding.

        Args:
            encoding (str): The character encoding to use for the conversion. Default is 'utf-8'.
        """
        self.encoding = encoding
        self.in_code_block = False
        self.table_replacements = {}
        self.plugins: Dict[str, Dict[str, Any]] = {}  # プラグインを格納する辞書
        self.plugin_order: List[str] = []  # プラグインの実行順序
        # Use compiled regex patterns for better performance
        self.patterns: List[Tuple[re.Pattern, str]] = [
            (re.compile(r"^(\s*)- \[([ ])\] (.+)", re.MULTILINE), r"\1• ☐ \3"),  # Unchecked task list
            (re.compile(r"^(\s*)- \[([xX])\] (.+)", re.MULTILINE), r"\1• ☑ \3"),  # Checked task list
            (re.compile(r"^(\s*)- (.+)", re.MULTILINE), r"\1• \2"),  # Unordered list
            (re.compile(r"^(\s*)(\d+)\. (.+)", re.MULTILINE), r"\1\2. \3"),  # Ordered list
            (re.compile(r"!\[.*?\]\((.+?)\)", re.MULTILINE), r"<\1>"),  # Images to URL
            (re.compile(r"(?<!\*)\*([^*\n]+?)\*(?!\*)", re.MULTILINE), r"_\1_"),  # Italic
            (re.compile(r"^###### (.+)$", re.MULTILINE), r"*\1*"), # H6 as bold
            (re.compile(r"^##### (.+)$", re.MULTILINE), r"*\1*"), # H5 as bold
            (re.compile(r"^#### (.+)$", re.MULTILINE), r"*\1*"), # H4 as bold
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

    def register_plugin(self, name: str, converter_func: Callable[[str], str], 
                       priority: int = 50, scope: str = "line") -> None:
        """
        Register a custom conversion plugin.
        
        Args:
            name (str): A unique name for the plugin
            converter_func (callable): A function that takes a text string and returns the converted text
            priority (int): Execution priority (lower numbers execute first)
            scope (str): Application scope - "global" (entire text), "line" (line by line), or "block" (block by block)
        """
        if scope not in ["global", "line", "block"]:
            raise ValueError("Plugin scope must be 'global', 'line', or 'block'")
            
        self.plugins[name] = {
            "func": converter_func,
            "priority": priority,
            "scope": scope
        }
        # Update plugin execution order based on priority (lower numbers execute first)
        self.plugin_order = sorted(
            self.plugins.keys(),
            key=lambda x: self.plugins[x]["priority"]
        )
        
    def remove_plugin(self, name: str) -> bool:
        """
        Remove a registered plugin.
        
        Args:
            name (str): The name of the plugin to remove
            
        Returns:
            bool: True if the plugin was removed, False if it wasn't found
        """
        if name in self.plugins:
            del self.plugins[name]
            self.plugin_order = [p for p in self.plugin_order if p != name]
            return True
        return False
        
    def get_registered_plugins(self) -> Dict[str, Dict[str, Any]]:
        """
        Get a list of all registered plugins.
        
        Returns:
            Dict[str, Dict[str, Any]]: A dictionary of plugin names and their properties
        """
        return {name: {
            "priority": info["priority"],
            "scope": info["scope"]
        } for name, info in self.plugins.items()}

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
            markdown = markdown.strip()

            self.table_replacements = {}

            markdown = self._convert_tables(markdown)
            
            # Apply global scope plugins
            for plugin_name in self.plugin_order:
                plugin = self.plugins[plugin_name]
                if plugin["scope"] == "global":
                    markdown = plugin["func"](markdown)
            
            lines = markdown.split("\n")
            converted_lines = []
            
            for line in lines:
                # Skip conversion for table placeholders
                if line.startswith("%%TABLE_PLACEHOLDER_") and line.endswith("%%"):
                    converted_lines.append(line)
                    continue
                
                # Apply line scope plugins
                for plugin_name in self.plugin_order:
                    plugin = self.plugins[plugin_name]
                    if plugin["scope"] == "line":
                        line = plugin["func"](line)
                
                # Apply standard line conversion
                line = self._convert_line(line)
                converted_lines.append(line)
                
            result = "\n".join(converted_lines)

            for placeholder, table in self.table_replacements.items():
                result = result.replace(placeholder, table)
            
            # Apply block scope plugins
            for plugin_name in self.plugin_order:
                plugin = self.plugins[plugin_name]
                if plugin["scope"] == "block":
                    result = plugin["func"](result)
                
            return result.encode(self.encoding).decode(self.encoding)
        except Exception as e:
            # Log the error for debugging
            logging.error(f"Markdown conversion error: {str(e)}")
            return markdown

    def _convert_tables(self, markdown: str) -> str:
        """
        Convert Markdown tables to Slack's mrkdwn format.

        Args:
            markdown (str): The Markdown text containing tables.

        Returns:
            str: The text with tables converted to Slack's format.
        """
        table_pattern = re.compile(
            r"^\|(.+)\|\s*$\n^\|[-:| ]+\|\s*$(\n^\|.+\|\s*$)*", re.MULTILINE
        )

        def convert_table(match):
            original_table = match.group(0)

            table_lines = original_table.strip().split("\n")
            header_line = table_lines[0]
            separator_line = table_lines[1]
            data_lines = table_lines[2:] if len(table_lines) > 2 else []

            headers = [cell.strip() for cell in header_line.strip("|").split("|")]

            rows = []
            for line in data_lines:
                cells = [cell.strip() for cell in line.strip("|").split("|")]
                rows.append(cells)

            result = []
            result.append(" | ".join(f"*{header}*" for header in headers))

            for row in rows:
                result.append(" | ".join(row))

            placeholder = f"%%TABLE_PLACEHOLDER_{hash(original_table)}%%"
            self.table_replacements[placeholder] = "\n".join(result)
            return placeholder

        return table_pattern.sub(convert_table, markdown)

    def _convert_line(self, line: str) -> str:
        """
        Convert a single line of Markdown.

        Args:
            line (str): A single line of Markdown text.

        Returns:
            str: The converted line in Slack's mrkdwn format.
        """
        if line.startswith("%%TABLE_PLACEHOLDER_") and line.endswith("%%"):
            return line

        code_block_match = re.match(r"^```(\w*)$", line)
        if code_block_match:
            language = code_block_match.group(1)
            self.in_code_block = not self.in_code_block
            if self.in_code_block and language:
                return f"```{language}"
            return "```"

        if self.in_code_block:
            return line

        line = re.sub(
            r"(?<!\*)\*\*\*([^*\n]+?)\*\*\*(?!\*)",
            lambda m: f"{self.triple_start}{m.group(1)}{self.triple_end}",
            line,
        )

        for pattern, replacement in self.patterns:
            line = pattern.sub(replacement, line)

        line = re.sub(
            re.escape(self.triple_start) + r"(.*?)" + re.escape(self.triple_end),
            r"*_\1_*",
            line,
            flags=re.MULTILINE,
        )

        return line.rstrip()
