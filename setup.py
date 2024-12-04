from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="markdown_to_mrkdwn",
    version="0.1.0",
    description="A library to convert Markdown to Slack's mrkdwn format",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="02tYasui",
    author_email="yasutai12@gmail.com",
    url="https://github.com/02tYasui/markdown_to_mrkdwn",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
