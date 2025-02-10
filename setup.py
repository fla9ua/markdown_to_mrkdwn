from setuptools import setup, find_packages
import markdown_to_mrkdwn

DESCRIPTION = "A library to convert Markdown to Slack's mrkdwn format"
NAME = "markdown_to_mrkdwn"
AUTHOR = "fla9ua"
AUTHOR_EMAIL = "fla9ua@gmail.com"
URL = "https://github.com/fla9ua/markdown_to_mrkdwn"
LICENSE = "MIT License"
DOWNLOAD_URL = "https://github.com/fla9ua/markdown_to_mrkdwn"
VERSION = markdown_to_mrkdwn.__version__
PYTHON_REQUIRES = ">=3.6"

INSTALL_REQUIRES = [
    # No dependencies required at the moment
]

EXTRAS_REQUIRE = {
    # Add optional dependencies here if needed
}

PACKAGES = find_packages()

CLASSIFIERS = [
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
]

with open("README.md", "r", encoding="utf-8") as fp:
    long_description = fp.read()

setup(
    name=NAME,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type="text/markdown",
    license=LICENSE,
    url=URL,
    version=VERSION,
    download_url=DOWNLOAD_URL,
    python_requires=PYTHON_REQUIRES,
    install_requires=INSTALL_REQUIRES,
    extras_require=EXTRAS_REQUIRE,
    packages=PACKAGES,
    classifiers=CLASSIFIERS,
)
