<picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/feedzai/feedzai-altair-theme/master/assets/notebook_header_dark.svg" />
    <img alt="" src="https://raw.githubusercontent.com/feedzai/feedzai-altair-theme/master/assets/notebook_header.svg" style="max-height: 96px;" />
</picture>

# feedzai-altair-theme

[![PyPI](https://img.shields.io/pypi/v/feedzai-altair-theme)](https://pypi.org/project/feedzai-altair-theme/)
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/feedzai/feedzai-altair-theme/master?urlpath=/lab/tree/demo.ipynb)
[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/feedzai/feedzai-altair-theme/blob/master/demo.ipynb)
[![Open with marimo](https://marimo.io/shield.svg)](https://marimo.app/https://github.com/feedzai/feedzai-altair-theme/blob/master/demo.ipynb)

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

alt.themes.enable("feedzai")
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
