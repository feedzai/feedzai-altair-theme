<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/feedzai/feedzai-altair-theme/master/assets/notebook_header_dark.svg" />
    <img alt="" src="https://raw.githubusercontent.com/feedzai/feedzai-altair-theme/master/assets/notebook_header.svg" height="96" />
</picture>

# feedzai-altair-theme

[![PyPI](https://img.shields.io/pypi/v/feedzai-altair-theme)](https://pypi.org/project/feedzai-altair-theme/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/feedzai/feedzai-altair-theme/master?urlpath=/lab/tree/demo.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/feedzai/feedzai-altair-theme/blob/master/demo.ipynb)

Feedzai's theme for [Altair](https://github.com/altair-viz/altair) charts.

## Sneak peek

![Examples of charts with the feedzai-altair-theme applied](https://raw.githubusercontent.com/feedzai/feedzai-altair-theme/master/assets/header.svg)

## Quickstart

### Installation

Via [pip](https://github.com/pypa/pip):

```bash
pip install feedzai-altair-theme
```

Via [Pipenv](https://pipenv.pypa.io/):

```bash
pipenv install feedzai-altair-theme
```

Via [Poetry](https://python-poetry.org/):

```bash
poetry add feedzai-altair-theme
```

Via [PDM](https://pdm.fming.dev/):

```bash
pdm add feedzai-altair-theme
```

Via [uv](https://docs.astral.sh/uv/):

```bash
uv add feedzai-altair-theme
```

### Usage

```python
import altair as alt

alt.theme.enable("feedzai")
```

You can find some example charts in the [`demo.ipynb` notebook](demo.ipynb).

## Development

Assuming [uv](https://docs.astral.sh/uv/getting-started/installation/) is installed, install Python:

```bash
uv python install
```

Create and activate the development environment:

```bash
uv sync
```

```bash
source .venv/bin/activate
```

After implementing changes, type-check with mypy, then lint and format the code with Ruff:

```bash
mypy
```

```bash
ruff check --fix
```

```bash
ruff format
```

To see the changes applied to some example charts, use the [`demo.ipynb` notebook](demo.ipynb):

```bash
jupyter lab demo.ipynb
```

Once done, deactivate the development environment:

```bash
deactivate
```

## Deployment

### Bump the package version

Bump the feedzai-altair-theme version using one of the following commands, according to the [Semantic Versioning](https://semver.org/) specification:

```bash
uv version --bump patch
```

```bash
uv version --bump minor
```

```bash
uv version --bump major
```

Next, confirm you can build the package locally:

```bash
uv build
```

### Open a PR

Once the changes are finished and the feedzai-altair-theme version is updated, open a [PR](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request). After the PR is merged, a maintainer will ensure a new package version is released.

### Release the new package version

To release a new version of feedzai-altair-theme, create a new (lightweight) tag from the `master` branch, and a GitHub Actions workflow will take care of the rest:

```bash
git tag "v$(uv version --short)"
```

```bash
git tag -n
```

```bash
git push origin --tags
```

## Misc

### Install the feedzai-altair-theme package in an environment without an Internet connection

#### Via repo

First, download the repo and move it to your environment. Then install the package with pip (or an equivalent) by pointing to the folder path and adding the necessary flags:

```bash
pip install feedzai-altair-theme/ --no-deps --no-build-isolation
```

This command assumes that the feedzai-altair-theme [dependencies](https://github.com/feedzai/feedzai-altair-theme/blob/master/pyproject.toml) and the [uv build backend](https://docs.astral.sh/uv/concepts/build-backend/) are already installed in your environment. For more information about the additional flags, check the [pip install documentation](https://pip.pypa.io/en/stable/cli/pip_install/).

#### Via wheel

First, download the [wheel (a.k.a. built distribution)](https://pypi.org/project/feedzai-altair-theme/#files) and move it to your environment. Then install the package with pip (or an equivalent) by pointing to the file path and adding the necessary flags after replacing `<VERSION>`:

```bash
pip install feedzai_altair_theme-<VERSION>-py3-none-any.whl
```

This command assumes that the feedzai-altair-theme [dependencies](https://github.com/feedzai/feedzai-altair-theme/blob/master/pyproject.toml) are already installed in your environment.
