import unittest
from markdown_to_mrkdwn.converter import SlackMarkdownConverter


class TestSlackMarkdownConverter(unittest.TestCase):
    def setUp(self):
        self.converter = SlackMarkdownConverter()

    def test_convert_headers(self):
        self.assertEqual(self.converter.convert("# Header 1"), "*Header 1*")
        self.assertEqual(self.converter.convert("## Header 2"), "*Header 2*")
        self.assertEqual(self.converter.convert("### Header 3"), "*Header 3*")
        self.assertEqual(self.converter.convert("#### Header 4"), "*Header 4*")
        self.assertEqual(self.converter.convert("##### Header 5"), "*Header 5*")
        self.assertEqual(self.converter.convert("###### Header 6"), "*Header 6*")

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

    def test_unordered_list(self):
        self.assertEqual(self.converter.convert("- Item 1\n- Item 2\n  - Sub Item 2.1\n  - Sub Item 2.2\n- Item 3"), "• Item 1\n• Item 2\n  • Sub Item 2.1\n  • Sub Item 2.2\n• Item 3")

    def test_nested_unordered_list(self):
        self.assertEqual(self.converter.convert("- アイテム1\n  - サブアイテム1.1\n  - サブアイテム1.2\n- アイテム2"), "• アイテム1\n  • サブアイテム1.1\n  • サブアイテム1.2\n• アイテム2")

    def test_nested_ordered_list(self):
        self.assertEqual(self.converter.convert("1. アイテム1\n   1. サブアイテム1.1\n   2. サブアイテム1.2\n2. アイテム2"), "1. アイテム1\n   1. サブアイテム1.1\n   2. サブアイテム1.2\n2. アイテム2")

    def test_mixed_nested_list(self):
        self.assertEqual(self.converter.convert("- アイテム1\n  1. サブアイテム1.1\n  2. サブアイテム1.2\n- アイテム2\n    - サブアイテム2.1\n        1. サブサブアイテム2.1.1"), "• アイテム1\n  1. サブアイテム1.1\n  2. サブアイテム1.2\n• アイテム2\n    • サブアイテム2.1\n        1. サブサブアイテム2.1.1")

    def test_list_item_with_bold_and_italic(self):
        self.assertEqual(self.converter.convert("- *太字*で_イタリック_なアイテム\n- **太字**と*イタリック*"), "• _太字_で_イタリック_なアイテム\n• *太字*と_イタリック_")

    def test_list_item_with_link(self):
        self.assertEqual(self.converter.convert("- [Google](https://google.com)へのリンク"), "• <https://google.com|Google>へのリンク")

    def test_list_item_with_inline_code(self):
        self.assertEqual(self.converter.convert("- `code`を含むアイテム"), "• `code`を含むアイテム")

    def test_list_item_with_combined_formatting(self):
        self.assertEqual(self.converter.convert("- ***太字***で[`リンク`](https://example.com)も含む_イタリック_なアイテム"), "• *_太字_*で<https://example.com|`リンク`>も含む_イタリック_なアイテム")

    def test_ordered_list(self):
        self.assertEqual(self.converter.convert("1. First item\n2. Second item\n   1. Sub first\n   2. Sub second\n3. Third item"), "1. First item\n2. Second item\n   1. Sub first\n   2. Sub second\n3. Third item")

    def test_nested_unordered_list_detailed(self):
        markdown = """- Item 1
  - Subitem 1.1
  - Subitem 1.2
- Item 2"""
        expected = """• Item 1
  • Subitem 1.1
  • Subitem 1.2
• Item 2"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_nested_ordered_list_detailed(self):
        markdown = """1. Item 1
   1. Subitem 1.1
   2. Subitem 1.2
2. Item 2"""
        expected = """1. Item 1
   1. Subitem 1.1
   2. Subitem 1.2
2. Item 2"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_mixed_nested_list_detailed(self):
        markdown = """- Item 1
  1. Subitem 1.1
  2. Subitem 1.2
- Item 2
    - Subitem 2.1
        1. Sub-subitem 2.1.1"""
        expected = """• Item 1
  1. Subitem 1.1
  2. Subitem 1.2
• Item 2
    • Subitem 2.1
        1. Sub-subitem 2.1.1"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_list_item_with_bold_and_italic_detailed(self):
        markdown = """- *Bold* and _italic_ item
- **Bold** and *italic*"""
        expected = """• _Bold_ and _italic_ item
• *Bold* and _italic_"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_list_item_with_link_detailed(self):
        markdown = "- Link to [Google](https://google.com)"
        expected = "• Link to <https://google.com|Google>"
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_list_item_with_inline_code_detailed(self):
        markdown = "- Item containing `code`"
        expected = "• Item containing `code`"
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_list_item_with_combined_formatting_detailed(self):
        markdown = "- ***Bold Italic*** item with a [`link`](https://example.com)"
        expected = "• *_Bold Italic_* item with a <https://example.com|`link`>"
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_very_deep_nested_list(self):
        markdown = """- Level 1
  - Level 2
    - Level 3
      - Level 4
        - Level 5"""
        expected = """• Level 1
  • Level 2
    • Level 3
      • Level 4
        • Level 5"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_list_item_with_multiline(self):
        markdown = """- Item 1 spans
  multiple
  lines.
- Item 2"""
        expected = """• Item 1 spans
  multiple
  lines.
• Item 2"""
        self.assertEqual(self.converter.convert(markdown), expected)

    def test_list_item_with_code_block(self):
        markdown = """- Item 1
    ```python
    def test():
        print("hello")
    ```
- Item 2"""
        expected = """• Item 1
    ```python
    def test():
        print("hello")
    ```
• Item 2"""
        self.assertEqual(self.converter.convert(markdown), expected)
        
    def test_list_item_with_complex_combined_formatting(self):
        markdown = "- Item with ~strikethrough~, ***bold italic***, and a [`link`](http://ex.com)"
        expected = "• Item with ~strikethrough~, *_bold italic_*, and a <http://ex.com|`link`>"
        self.assertEqual(self.converter.convert(markdown), expected)


if __name__ == "__main__":
    unittest.main()
