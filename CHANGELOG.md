# Changelog
## [0.2.0] - 2025-04-19
### Added
- Plugin system: `register_plugin`, `register_regex_plugin` for user-defined conversions
- Support for regex-based line plugins (with priority and timing)
- `timing` (before/after) to control plugin application order
- Enhanced tests for plugin and regex features
- Expanded documentation and usage examples in README.md, README.rst

## [0.1.7] - 2025-04-12
### Added
- Added support for header (H4, H5, H6)

## [0.1.6] - 2025-04-02
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
