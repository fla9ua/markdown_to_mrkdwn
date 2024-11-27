# tests/test_converter.py
import unittest
from markdown_to_mrkdwn import SlackMarkdownConverter

class TestSlackMarkdownConverter(unittest.TestCase):
    def test_headers(self):
        markdown = "# Header 1\n## Header 2\n### Header 3"
        expected = "*Header 1*\n*Header 2*\n_Header 3_"
        self.assertEqual(SlackMarkdownConverter.convert(markdown).strip(), expected)

    def test_emphasis(self):
        markdown = "**Bold** and _Italic_"
        expected = "*Bold* and _Italic_"
        self.assertEqual(SlackMarkdownConverter.convert(markdown), expected)

    def test_code_blocks(self):
        markdown = "Inline `code` and block:\n```python\ndef hello():\n    print('world')\n```"
        expected = "Inline `code` and block:\n```\ndef hello():\n    print('world')\n```"
        self.assertEqual(SlackMarkdownConverter.convert(markdown).strip(), expected)

    def test_unordered_list(self):
        markdown = "- Item 1\n- Item 2\n- Item 3"
        expected = "• Item 1\n• Item 2\n• Item 3"
        self.assertEqual(SlackMarkdownConverter.convert(markdown).strip(), expected)

    def test_ordered_list(self):
        markdown = "1. First\n2. Second\n3. Third"
        expected = "1. First\n2. Second\n3. Third"
        self.assertEqual(SlackMarkdownConverter.convert(markdown).strip(), expected)

if __name__ == '__main__':
    unittest.main()