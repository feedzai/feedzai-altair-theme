# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Support for Altair 6.
- Test suite for theme registration and enablement.

### Changed

- Use the new `altair.datasets` module instead of `vega-datasets` for Altair 6 in the demo notebook.

## [2.0.0] - 2025-09-03

### Added

- Google Colab badge.
- Deployment instructions.
- Three new examples for the demo notebook: pie chart, strip plot, and scatterplot.
- White border to scatterplot-related marks for accessibility.
- Set the `circle` and `square` marks for scatterplots and remove the extra properties from the `point` mark.

### Changed

- Switch to uv for package management and Ruff for linting and formatting.
- Update the legacy URL parameter for the Binder demo.
- Update the `path` property to `tick`, explicitly supporting this mark.

### Removed

- Drop support for Python 3.7, 3.8, and 3.9; the minimum required version is now Python 3.10.
- Drop support for Altair 4; the minimum required version is now [Altair 5.5.0](https://github.com/vega/altair/releases/tag/v5.5.0) with the new theme API.
- Adopt the [`ThemeConfig` type](https://altair-viz.github.io/user_guide/generated/theme/altair.theme.ThemeConfig.html) and delete the custom types for the same purpose.
- Clear unused theme properties.

### Fixed

- Move dependency management to the notebook and fix the Binder demo.

## [1.1.2] - 2023-01-13

### Added

- Document how to install the package in an environment without an Internet connection.
- Changelog to `project_urls`.

## [1.1.1] - 2022-07-25

### Added

- Binder badge.
- PyPI badge.

### Fixed

- Use absolute URLs in README because of PyPI.

## [1.1.0] - 2022-06-20

### Fixed

- Add `typing-extensions` as a package dependency.

## [1.0.0] - 2022-06-02

### Added

- Boilerplate to create a Python package.
- Feedzai's Altair theme.
- GitHub Actions workflow to publish the package to PyPI.
