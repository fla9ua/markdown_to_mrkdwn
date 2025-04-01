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
        
    def test_convert_ordered_list(self):
        self.assertEqual(self.converter.convert("1. item"), "1. item")
        self.assertEqual(self.converter.convert("2. item"), "2. item")
        
    def test_nested_ordered_list(self):
        markdown = """1. Item 1
   1. Subitem 1
   2. Subitem 2
2. Item 2"""
        expected = """1. Item 1
   1. Subitem 1
   2. Subitem 2
2. Item 2"""
        self.assertEqual(self.converter.convert(markdown), expected)
        
    def test_mixed_list_types(self):
        markdown = """1. Ordered item
   - Unordered subitem
2. Another ordered item
   1. Ordered subitem"""
        expected = """1. Ordered item
   • Unordered subitem
2. Another ordered item
   1. Ordered subitem"""
        self.assertEqual(self.converter.convert(markdown), expected)

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

    def test_code_block_with_language(self):
        markdown = """```python
def hello_world():
    print("Hello, world!")
```"""
        expected = """```python
def hello_world():
    print("Hello, world!")
```"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_code_block_with_cron(self):
        markdown = """```cron
# comment
0 */12 * * * certbot renew --quiet
```"""
        expected = """```cron
# comment
0 */12 * * * certbot renew --quiet
```"""
        self.assertEqual(self.converter.convert(markdown), expected)
        
    def test_multiple_code_blocks_with_different_languages(self):
        markdown = """```python
print("Hello from Python")
```

Some text in between

```javascript
console.log("Hello from JavaScript");
```"""
        expected = """```python
print("Hello from Python")
```

Some text in between

```javascript
console.log("Hello from JavaScript");
```"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_mixed_code_block_and_markdown(self):
        markdown = """```cron
# comment
0 */12 * * * certbot renew --quiet
```

# comment
0 */12 * * * certbot renew --quiet"""
        expected = """```cron
# comment
0 */12 * * * certbot renew --quiet
```

*comment*
0 _/12 _ _ _ certbot renew --quiet"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_convert_bold_in_list(self):
        markdown = "- **test**: a"
        expected = "• *test*: a"
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_convert_bold_and_underline(self):
        markdown = "This is ***bold and italic***"
        expected = "This is *_bold and italic_*"
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_convert_strikethrough(self):
        markdown = "This is ~~strikethrough~~ text"
        expected = "This is ~strikethrough~ text"
        self.assertEqual(self.converter.convert(markdown), expected)
        
    def test_convert_task_list(self):
        markdown = "- [ ] Unchecked task\n- [x] Checked task\n- [X] Also checked task"
        expected = "• ☐ Unchecked task\n• ☑ Checked task\n• ☑ Also checked task"
        self.assertEqual(self.converter.convert(markdown), expected)
        
    def test_convert_table(self):
        markdown = """| Header 1 | Header 2 | Header 3 |
| --- | --- | --- |
| Row 1 Col 1 | Row 1 Col 2 | Row 1 Col 3 |
| Row 2 Col 1 | Row 2 Col 2 | Row 2 Col 3 |"""
        expected = """*Header 1* | *Header 2* | *Header 3*
Row 1 Col 1 | Row 1 Col 2 | Row 1 Col 3
Row 2 Col 1 | Row 2 Col 2 | Row 2 Col 3"""
        self.assertEqual(self.converter.convert(markdown), expected)
        
    def test_convert_table_with_alignment(self):
        markdown = """| Left | Center | Right |
| :--- | :---: | ---: |
| Left-aligned | Center-aligned | Right-aligned |"""
        expected = """*Left* | *Center* | *Right*
Left-aligned | Center-aligned | Right-aligned"""
        self.assertEqual(self.converter.convert(markdown), expected)
        
    def test_error_handling(self):
        """Test that the converter returns the original markdown when an exception occurs."""
        # Create a converter with a method that will raise an exception
        converter = SlackMarkdownConverter()
        
        # Mock the _convert_tables method to raise an exception
        original_convert_tables = converter._convert_tables
        def mock_convert_tables(markdown):
            raise Exception("Test exception")
        converter._convert_tables = mock_convert_tables
        
        # Test that the original markdown is returned when an exception occurs
        markdown = "# Test markdown"
        result = converter.convert(markdown)
        self.assertEqual(result, markdown)
        
        # Restore the original method
        converter._convert_tables = original_convert_tables


if __name__ == "__main__":
    unittest.main()
