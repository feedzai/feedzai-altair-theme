# feedzai-altair-theme

Feedzai's theme for [Altair](https://github.com/altair-viz/altair) charts.

## Usage

```python
import altair as alt

alt.themes.enable("feedzai")
```

## Development

Create the development environment:

```bash
make init
```

After implementing changes, run the command to check the types and to format and lint the code (you can also use the individual commands defined in the `Makefile`):

```bash
make all
```
