import unittest
from markdown_to_mrkdwn import SlackMarkdownConverter

class TestSlackMarkdownConverter(unittest.TestCase):
    def setUp(self):
        self.converter = SlackMarkdownConverter()

    def test_bold_conversion(self):
        """Test conversion of bold text using ** and __"""
        test_cases = [
            ('**bold text**', '*bold text*'),
            ('__bold text__', '*bold text*')
        ]
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)

    def test_italic_conversion(self):
        """Test conversion of italic text"""
        test_cases = [
            ('*italic text*', '_italic text_')
        ]
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)

    def test_link_conversion(self):
        """Test conversion of markdown links"""
        test_cases = [
            ('[Anthropic](https://www.anthropic.com)', '<https://www.anthropic.com|Anthropic>')
        ]
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)

    def test_list_conversion(self):
        """Test conversion of unordered lists"""
        test_cases = [
            ('- Item 1\n- Item 2', '• Item 1\n• Item 2')
        ]
        for markdown, expected in test_cases:
            with self.subTest(markdown=markdown):
                result = self.converter.convert(markdown)
                self.assertEqual(result, expected)

    def test_multiline_conversion(self):
        """Test conversion of multiple Markdown elements in a single document"""
        markdown = """# Title
**Bold text**
- List item
[Link](https://example.com)
"""
        expected = """*Title*
*Bold text*
• List item
<https://example.com|Link>
"""
        result = self.converter.convert(markdown)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()