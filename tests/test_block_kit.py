import unittest
import json
from markdown_to_mrkdwn.block_kit import BlockKitConverter


class TestBlockKitConverter(unittest.TestCase):
    def setUp(self):
        self.converter = BlockKitConverter()

    def test_empty_string(self):
        result = self.converter.convert_to_blocks("")
        self.assertEqual(result, {"blocks": []})

    def test_simple_paragraph(self):
        markdown = "This is a simple paragraph."
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 1)
        self.assertEqual(result["blocks"][0]["type"], "section")
        self.assertEqual(result["blocks"][0]["text"]["type"], "mrkdwn")
        self.assertEqual(result["blocks"][0]["text"]["text"], "This is a simple paragraph.")

    def test_multiple_paragraphs(self):
        markdown = "Paragraph 1.\n\nParagraph 2."
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 2)
        self.assertEqual(result["blocks"][0]["text"]["text"], "Paragraph 1.")
        self.assertEqual(result["blocks"][1]["text"]["text"], "Paragraph 2.")

    def test_headings(self):
        markdown = "# Heading 1\n## Heading 2\n### Heading 3"
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 3)
        
        # H1 should use header block
        self.assertEqual(result["blocks"][0]["type"], "header")
        self.assertEqual(result["blocks"][0]["text"]["text"], "Heading 1")
        
        # H2 and H3 should use section blocks with bold text
        self.assertEqual(result["blocks"][1]["type"], "section")
        self.assertEqual(result["blocks"][1]["text"]["text"], "*Heading 2*")
        
        self.assertEqual(result["blocks"][2]["type"], "section")
        self.assertEqual(result["blocks"][2]["text"]["text"], "*Heading 3*")

    def test_formatting(self):
        markdown = "**Bold** and *italic* text."
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 1)
        self.assertEqual(result["blocks"][0]["text"]["text"], "*Bold* and _italic_ text.")

    def test_lists(self):
        markdown = "- Item 1\n- Item 2\n  - Nested item"
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 1)
        self.assertEqual(result["blocks"][0]["text"]["text"], "• Item 1\n• Item 2\n  • Nested item")

    def test_task_lists(self):
        markdown = "- [ ] Unchecked task\n- [x] Checked task"
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 1)
        self.assertEqual(result["blocks"][0]["text"]["text"], "• ☐ Unchecked task\n• ☑ Checked task")

    def test_blockquote(self):
        markdown = "> This is a quote\n> spanning multiple lines."
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 1)
        self.assertEqual(result["blocks"][0]["text"]["text"], "> This is a quote\n> spanning multiple lines.")

    def test_code_block(self):
        markdown = "```python\ndef hello():\n    print('Hello')\n```"
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 1)
        self.assertEqual(result["blocks"][0]["type"], "section")
        self.assertEqual(result["blocks"][0]["text"]["text"], "```python\ndef hello():\n    print('Hello')\n```")

    def test_horizontal_rule(self):
        markdown = "Text above\n---\nText below"
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 3)
        self.assertEqual(result["blocks"][0]["type"], "section")
        self.assertEqual(result["blocks"][1]["type"], "divider")
        self.assertEqual(result["blocks"][2]["type"], "section")

    def test_image(self):
        markdown = "![Alt text](https://example.com/image.png)"
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 1)
        self.assertEqual(result["blocks"][0]["type"], "image")
        self.assertEqual(result["blocks"][0]["image_url"], "https://example.com/image.png")
        self.assertEqual(result["blocks"][0]["alt_text"], "Alt text")

    def test_table(self):
        markdown = """| Header 1 | Header 2 |
| -------- | -------- |
| Cell 1   | Cell 2   |"""
        result = self.converter.convert_to_blocks(markdown)
        
        self.assertEqual(len(result["blocks"]), 1)
        self.assertEqual(result["blocks"][0]["type"], "section")
        # The table should be converted to mrkdwn format
        self.assertIn("Header 1", result["blocks"][0]["text"]["text"])
        self.assertIn("Cell 1", result["blocks"][0]["text"]["text"])

    def test_complex_document(self):
        markdown = """# Document Title

This is an introduction paragraph with **bold** and *italic* text.

## Section 1

- List item 1
- List item 2
  - Nested item

> Important quote
> spanning multiple lines

```python
def example():
    return "Hello, world!"
```

---

![Sample Image](https://example.com/image.jpg)

| Header 1 | Header 2 |
| -------- | -------- |
| Data 1   | Data 2   |
"""
        result = self.converter.convert_to_blocks(markdown)
        
        # Check that we have the expected number of blocks
        # 1. Header
        # 2. Paragraph
        # 3. Section header
        # 4. List
        # 5. Blockquote
        # 6. Code block
        # 7. Divider
        # 8. Image
        # 9. Table
        self.assertEqual(len(result["blocks"]), 9)
        
        # Check specific block types
        self.assertEqual(result["blocks"][0]["type"], "header")  # Document Title
        self.assertEqual(result["blocks"][2]["type"], "section")  # Section 1
        self.assertEqual(result["blocks"][6]["type"], "divider")  # Horizontal rule
        self.assertEqual(result["blocks"][7]["type"], "image")    # Image


if __name__ == "__main__":
    unittest.main()
