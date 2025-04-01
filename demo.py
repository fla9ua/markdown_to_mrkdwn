import sys
import io
import json
from markdown_to_mrkdwn import SlackMarkdownConverter, BlockKitConverter

# Set the standard output encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

# Sample markdown text
markdown_text = """
# Heading 1
## Heading 2
### Heading 3

This is a test of **bold** and *italic* text.

> This is a quote.

- List item 1
- List item 2
  - Nested list 1
  - Nested list 2

1. Numbered list 1
2. Numbered list 2

[Link example](https://www.instagram.com/fla9ua)

`Inline code`

![Image example](https://picsum.photos/300/200)
___
~~Strikethrough text~~

- [ ] Unchecked task
- [x] Checked task
- [X] Also checked task

| Header 1 | Header 2 | Header 3 |
| --- | --- | --- |
| Row 1 Col 1 | Row 1 Col 2 | Row 1 Col 3 |
| Row 2 Col 1 | Row 2 Col 2 | Row 2 Col 3 |

| Left | Center | Right |
| :--- | :---: | ---: |
| Left-aligned | Center-aligned | Right-aligned |

```
# This is a code block example
```

```python
# This is a Python code block example
print("Hello, World!")
```

"""

# Demo 1: Convert to mrkdwn text format
print("=== DEMO 1: MARKDOWN TO MRKDWN TEXT ===\n")
converter = SlackMarkdownConverter()
mrkdwn_text = converter.convert(markdown_text)
print(mrkdwn_text)

# Compare before and after conversion
print("\nBefore and after comparison:")
for before, after in zip(markdown_text.strip().split('\n'), mrkdwn_text.split('\n')):
    print(f"Before: [{before}]")
    print(f"After:  [{after}]")
    print()

# Demo 2: Convert to Block Kit JSON format
print("\n=== DEMO 2: MARKDOWN TO BLOCK KIT JSON ===\n")
block_kit_converter = BlockKitConverter()
block_kit_json = block_kit_converter.convert_to_blocks(markdown_text)

# Print the JSON with indentation for readability
print(json.dumps(block_kit_json, indent=2))

print("\n=== DEMO COMPLETE ===")
