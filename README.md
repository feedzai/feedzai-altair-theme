# feedzai-altair-theme <img align="right" src="https://raw.githubusercontent.com/feedzai/feedzai-altair-theme/master/assets/logo.svg" height="96" />

[![PyPI](https://img.shields.io/pypi/v/feedzai-altair-theme)](https://pypi.org/project/feedzai-altair-theme/) [![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/feedzai/feedzai-altair-theme/master?labpath=demo.ipynb)

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

Via [Pyflow](https://github.com/David-OConnor/pyflow):

```bash
pyflow install feedzai-altair-theme
```

### Usage

```python
import altair as alt

alt.themes.enable("feedzai")
```

You can find some example charts in the [`demo.ipynb` notebook](demo.ipynb).

## Development

Create the development environment:

```bash
make init
```

After implementing changes, run the command to check the types and to format and lint the code (you can also use the individual commands defined in the `Makefile`):

```bash
make all
```

To see the changes applied to some example charts, use the [`demo.ipynb` notebook](demo.ipynb):

```bash
make demo
```

## Misc

### Install the feedzai-altair-theme package in an environment without an Internet connection

First, download the repo and move its root folder to your environment. From there, you can install the package with pip by pointing to the folder path and adding some extra flags:

```bash
pip install -e feedzai-altair-theme/ --no-deps --no-build-isolation
```

This command assumes that the feedzai-altair-theme package [dependencies](https://github.com/feedzai/feedzai-altair-theme/blob/master/setup.py#L28) are already installed in your environment. For more information about the additional flags, check the [pip install documentation](https://pip.pypa.io/en/stable/cli/pip_install/).
