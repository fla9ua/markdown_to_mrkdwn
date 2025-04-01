# Changelog
## [0.1.7] - 2025-04-01
### Added
- Added extensible plugin system
  - Support for custom conversion plugins
  - Three plugin scopes: global, line, and block
  - Plugin priority system
  - Plugin management methods

## [0.1.6] - 2025-04-01
### Added
- Added support for ordered lists (numbered lists with proper indentation)
- Improved code block handling to preserve language specification

## [0.1.5] - 2025-04-01
### Fixed
- Fixed Sphinx documentation issues
  - Added proper toctree references in index.rst
  - Enhanced documentation content with installation and usage examples
  - Improved navigation between documentation pages
### Added
- Added support for task lists (- [ ] task, - [x] task)
- Added support for Markdown tables
- Added support for strikethrough text conversion (~~text~~ to ~text~)

## [0.1.4] - 2025-02-25
### Fixed
- Fixed an issue where both bold and italic text was converted incorrectly [#8](https://github.com/fla9ua/markdown_to_mrkdwn/issues/8)
  - Added related test cases

## [0.1.3] - 2025-02-10
### Changed
- Rename Author

## [0.1.2] - 2025-01-25
### Fixed
- Fixed code block conversion issue [#5](https://github.com/fla9ua/markdown_to_mrkdwn/issues/5)
  - Added code block state tracking
  - Skip conversion inside code blocks
  - Added related test cases

## [0.1.1] - 2024-12-13
### Changed
- Bug fix [#1](https://github.com/fla9ua/markdown_to_mrkdwn/issues/1)

## [0.1.0] - 2024-12-05
### Changed
- First Release
