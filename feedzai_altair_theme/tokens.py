"""Design tokens for the theme and standalone use."""

from typing import Dict, List, Union

FONT: str = "Roboto, Arial, sans-serif"

FONT_SIZES: Dict[str, int] = {"sm": 12, "md": 16, "lg": 20}

OPACITIES: Dict[str, float] = {"md": 0.5}

STROKE_WIDTHS: Dict[str, float] = {"sm": 0.5, "md": 1, "lg": 2}

COLORS: Dict[str, Union[str, Dict[str, Dict[str, List[str]]]]] = {
    "text": "#1A274E",
    "mark": "#2770EB",
    "axis": "#666F89",
    "background": "#FFFFFF",
    "grid": "#D1D4DC",
    "schemes": {
        "categorical": {
            "default": [
                "#2770EB",
                "#48B970",
                "#BA005D",
                "#EDB912",
                "#00A39E",
                "#AE7AFE",
                "#1A274E",
            ],
            "status": [
                "#1AA84C",
                "#D32F2F",
                "#FFC400",
            ],
        },
        "sequential": {
            "blues": [
                "#255AB8",
                "#2770EB",
                "#528DEF",
                "#7DA9F3",
                "#A9C6F7",
                "#EAF1FD",
            ],
            "greens": [
                "#208343",
                "#1AA84C",
                "#48B970",
                "#76CB94",
                "#A3DCB7",
                "#E9F7EE",
            ],
            "reds": [
                "#C11815",
                "#D32F2F",
                "#D74D51",
                "#E1797D",
                "#EBA6A8",
                "#FCD9EB",
            ],
            "pinks": [
                "#920049",
                "#BA005D",
                "#C86D9C",
                "#D89DBC",
                "#EAC2D7",
                "#FCD9EB",
            ],
            "purples": [
                "#6B44A6",
                "#965FE6",
                "#AE7AFE",
                "#BAA2EB",
                "#D1C1F1",
                "#E7DCFC",
            ],
            "greys": [
                "#333F61",
                "#4D5776",
                "#666F89",
                "#B3B7C4",
                "#C2C5D0",
                "#E1E2E7",
            ],
        },
        "diverging": {
            "bluepink": [
                "#255AB8",
                "#528DEF",
                "#A9C6F7",
                "#f5f5f5",
                "#EAC2D7",
                "#BA005D",
                "#920049",
            ],
            "greenpurple": [
                "#208343",
                "#48B970",
                "#A3DCB7",
                "#f5f5f5",
                "#D1C1F1",
                "#AE7AFE",
                "#6B44A6",
            ],
            "tealred": [
                "#035451",
                "#00A39E",
                "#A4CBCA",
                "#f5f5f5",
                "#EBA6A8",
                "#D74D51",
                "#C11815",
            ],
        },
    },
}
