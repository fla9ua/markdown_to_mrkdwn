# markdown_to_mrkdwn

[![Documentation Status](https://img.shields.io/badge/docs-latest-brightgreen.svg)](https://02tyasui.github.io/markdown_to_mrkdwn/markdown_to_mrkdwn.html)

MarkdownをSlackのmrkdwn形式に変換するライブラリです。

## 特徴

- MarkdownからSlackのmrkdwn形式への変換をサポートします。
- ネストされたリストや引用をサポートします。
- インラインコードや画像を処理します。

## インストール

pipを使用してパッケージをインストールできます。

```bash
pip install markdown_to_mrkdwn
```

## 使用方法

ライブラリの簡単な使用例を以下に示します。

```python
from markdown_to_mrkdwn import SlackMarkdownConverter

converter = SlackMarkdownConverter()
markdown_text = """
# ヘッダー1
**太字のテキスト**
- リスト項目
[リンク](https://example.com)
"""
mrkdwn_text = converter.convert(markdown_text)
print(mrkdwn_text)
```

Slack Block Kit Builderで出力を確認してください:
[Slack Block Kit Builder](https://app.slack.com/block-kit-builder/T01R1PV07QQ#%7B%22blocks%22:%5B%7B%22type%22:%22section%22,%22text%22:%7B%22type%22:%22mrkdwn%22,%22text%22:%22This%20is%20a%20mrkdwn%20section%20block%20:ghost:%20*this%20is%20bold*,%20and%20~this%20is%20crossed%20out~,%20and%20%3Chttps://google.com%7Cthis%20is%20a%20link%3E%22%7D%7D%5D%7D)

## コントリビューション

遠慮なくpull request・issueお送りください

## ライセンス

このプロジェクトはMITライセンスの下でライセンスされています。詳細は[LICENSE](LICENSE)ファイルを参照してください。