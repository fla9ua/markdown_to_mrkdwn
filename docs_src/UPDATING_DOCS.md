# How to Update Documentation

This file documents the process for updating the project documentation.

## Overview

The project uses Sphinx to generate HTML documentation from source files (`.rst`, `.md`, and Python docstrings).
The generated HTML is stored in the `docs/` directory and served via GitHub Pages.
A GitHub Actions workflow automatically builds and deploys the documentation upon pushes to the `main` branch.

## Update Process

1.  **Edit Source Files:**
    Make the necessary changes to the documentation source files and potentially the package version. This typically involves:
    *   Editing `.rst` files in the `docs_src/` directory (e.g., `index.rst`).
    *   Updating the main `README.md` and `README.rst` files in the project root.
    *   Modifying docstrings within the Python code (`markdown_to_mrkdwn/**/*.py`).
    *   **Updating the package version:** If releasing a new version or making significant changes, update the `__version__` variable in `markdown_to_mrkdwn/__init__.py`.

2.  **Commit and Push:**
    Commit the changes made to the source files and push them to the `main` branch of the GitHub repository.
    ```bash
    git add <modified_source_files>
    git commit -m "Update documentation for ..."
    git push origin main
    ```

3.  **Automatic Build and Deployment:**
    The GitHub Actions workflow (`.github/workflows/docs-deploy.yml`) will automatically trigger upon the push.
    It performs the following steps:
    *   Checks out the code.
    *   Sets up Python and installs Sphinx.
    *   Builds the HTML documentation (`cd docs_src && make html`).
    *   Copies the generated HTML files from `docs_src/_build/html/` to the `docs/` directory.
    *   Commits and pushes the updated `docs/` directory back to the `main` branch.

**Important:** You do **not** need to manually run `make html` or commit changes to the `docs/` directory. The automated workflow handles this entire process.
You only need to edit the *source* files and push them. 