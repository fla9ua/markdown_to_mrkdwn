from setuptools import setup, find_packages

setup(
    name="markdown-to-mrkdwn",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "markdown2>=2.4.0",
    ],
    author="02tYasui",
    author_email="yasutai12@gmail.com",
    description="Convert standard Markdown to Slack's mrkdwn format",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/02tYasui/markdown_to_mrkdwn",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    keywords="markdown slack conversion",
)
