import sys
import io
from markdown_to_mrkdwn import SlackMarkdownConverter

# Set the standard output encoding to UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")

converter = SlackMarkdownConverter()
markdown_text = """
# Heading 1
## Heading 2
### Heading 3
#### Heading 4
##### Heading 5
###### Heading 6

This is a test of **bold** and *italic* text.

> This is a quote.

- List item 1
- List item 2
  - Nested list 1
  - Nested list 2

1. Numbered list 1
2. Numbered list 2

[Link example](https://example.com)

`Inline code`

![Image example](https://example.com/image.png)
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
mrkdwn_text = converter.convert(markdown_text)
print(mrkdwn_text)

# Compare before and after conversion
print("\nBefore and after comparison:")
for before, after in zip(markdown_text.strip().split('\n'), mrkdwn_text.split('\n')):
    print(f"Before: [{before}]")
    print(f"After:  [{after}]")
    print()
