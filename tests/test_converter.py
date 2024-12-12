import unittest
from markdown_to_mrkdwn.converter import SlackMarkdownConverter


class TestSlackMarkdownConverter(unittest.TestCase):
    def setUp(self):
        self.converter = SlackMarkdownConverter()

    def test_convert_headers(self):
        self.assertEqual(self.converter.convert("# Header 1"), "*Header 1*")
        self.assertEqual(self.converter.convert("## Header 2"), "*Header 2*")
        self.assertEqual(self.converter.convert("### Header 3"), "*Header 3*")

    def test_convert_bold(self):
        self.assertEqual(self.converter.convert("**bold text**"), "*bold text*")
        self.assertEqual(self.converter.convert("__bold text__"), "*bold text*")

    def test_convert_italic(self):
        self.assertEqual(self.converter.convert("*italic text*"), "_italic text_")

    def test_convert_links(self):
        self.assertEqual(
            self.converter.convert("[link](http://example.com)"),
            "<http://example.com|link>",
        )

    def test_convert_inline_code(self):
        self.assertEqual(self.converter.convert("`code`"), "`code`")

    def test_convert_unordered_list(self):
        self.assertEqual(self.converter.convert("- item"), "• item")

    def test_convert_blockquote(self):
        self.assertEqual(self.converter.convert("> quote"), "> quote")

    def test_convert_images(self):
        self.assertEqual(
            self.converter.convert("![alt text](http://example.com/image.png)"),
            "<http://example.com/image.png>",
        )

    def test_convert_horizontal_rule(self):
        self.assertEqual(self.converter.convert("---"), "──────────")

    def test_empty_string(self):
        self.assertEqual(self.converter.convert(""), "")

    def test_mixed_elements(self):
        markdown = """# Title
**Bold text**
- List item
[Link](https://example.com)
"""
        expected = """*Title*
*Bold text*
• List item
<https://example.com|Link>"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_nested_list(self):
        markdown = """- Item 1
  - Subitem 1
  - Subitem 2
- Item 2"""
        expected = """• Item 1
  • Subitem 1
  • Subitem 2
• Item 2"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_multiline_blockquote(self):
        markdown = """> This is a quote
> that spans multiple lines."""
        expected = """> This is a quote
> that spans multiple lines."""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_code_block(self):
        markdown = """```
def hello_world():
    print("Hello, world!")
```"""
        expected = """```
def hello_world():
    print("Hello, world!")
```"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_convert_bold_in_list(self):
        markdown = "- **test**: a"
        expected = "• *test* : a"
        self.assertEqual(self.converter.convert(markdown), expected)


if __name__ == "__main__":
    unittest.main()
