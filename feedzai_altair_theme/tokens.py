"""Design tokens for the theme and standalone use."""

from typing import Dict

from .types import Color, Colors

FONT: str = "Roboto, Arial, sans-serif"

FONT_SIZES: Dict[str, int] = {"sm": 12, "md": 16, "lg": 20}

OPACITIES: Dict[str, float] = {"md": 0.5}

STROKE_WIDTHS: Dict[str, float] = {"sm": 0.5, "md": 1, "lg": 2}

SPACING: Dict[str, int] = {"xs": 1, "sm": 2, "md": 4, "lg": 8, "xl": 20}


COLOR_PRIMITIVES: Dict[str, Color] = {
    "blue": {
        "00": "#E9F1FD",
        "10": "#A6C4F7",
        "20": "#82ACF3",
        "30": "#4C88EE",
        "40": "#2770EB",
        "50": "#1B4EA5",
        "60": "#18448F",
    },
    "red": {
        "00": "#fbeaea",
        "10": "#edaaaa",
        "20": "#e58686",
        "30": "#da5252",
        "40": "#d32f2f",
        "50": "#942121",
        "60": "#811d1d",
    },
    "green": {
        "00": "#e8f3eb",
        "10": "#9fcdad",
        "20": "#77b98a",
        "30": "#3c9b58",
        "40": "#148636",
        "50": "#0e5e26",
        "60": "#0c5221",
    },
    "yellow": {
        "00": "#FFF9E6",
        "10": "#FFE796",
        "20": "#FFDD6B",
        "30": "#FFCE2B",
        "40": "#FFC400",
        "50": "#B38900",
        "60": "#7F6202",
    },
    "lavender": {
        "00": "#F5EFFD",
        "10": "#D4BDF5",
        "20": "#C2A2F1",
        "30": "#A87AEA",
        "40": "#965FE6",
        "50": "#6943A1",
        "60": "#5C3A8C",
    },
    "teal": {
        "00": "#e6f6f5",
        "10": "#96d9d7",
        "20": "#6bcac7",
        "30": "#2bb3ae",
        "40": "#00a39e",
        "50": "#00726f",
        "60": "#006360",
    },
    "neutral": {
        "00": "#F0F1F6",
        "10": "#E1E2E7",
        "20": "#B3B7C4",
        "30": "#666F89",
        "40": "#4D5776",
        "50": "#19274E",
        "60": "#000F3A",
    },
}

COLORS: Colors = {
    "arc": "#FFFFFF",
    "axis": COLOR_PRIMITIVES["neutral"]["30"],
    "background": "#FFFFFF",
    "grid": COLOR_PRIMITIVES["neutral"]["20"],
    "mark": COLOR_PRIMITIVES["blue"]["40"],
    "text": COLOR_PRIMITIVES["neutral"]["50"],
    "schemes": {
        "categorical": {
            "default": [
                COLOR_PRIMITIVES["blue"]["40"],
                COLOR_PRIMITIVES["green"]["20"],
                COLOR_PRIMITIVES["red"]["30"],
                COLOR_PRIMITIVES["yellow"]["40"],
                COLOR_PRIMITIVES["lavender"]["30"],
                COLOR_PRIMITIVES["teal"]["40"],
                COLOR_PRIMITIVES["neutral"]["50"],
            ],
            "status": [
                COLOR_PRIMITIVES["green"]["30"],
                COLOR_PRIMITIVES["red"]["30"],
                COLOR_PRIMITIVES["yellow"]["40"],
            ],
        },
        "diverging": {
            "bluered": [
                COLOR_PRIMITIVES["blue"]["60"],
                COLOR_PRIMITIVES["blue"]["30"],
                COLOR_PRIMITIVES["blue"]["10"],
                "#ffff",
                COLOR_PRIMITIVES["red"]["10"],
                COLOR_PRIMITIVES["red"]["30"],
                COLOR_PRIMITIVES["red"]["60"],
            ],
            "tealred": [
                COLOR_PRIMITIVES["teal"]["60"],
                COLOR_PRIMITIVES["teal"]["30"],
                COLOR_PRIMITIVES["teal"]["10"],
                "#ffff",
                COLOR_PRIMITIVES["red"]["10"],
                COLOR_PRIMITIVES["red"]["30"],
                COLOR_PRIMITIVES["red"]["60"],
            ],
            "greenlavender": [
                COLOR_PRIMITIVES["green"]["60"],
                COLOR_PRIMITIVES["green"]["30"],
                COLOR_PRIMITIVES["green"]["10"],
                "#ffff",
                COLOR_PRIMITIVES["lavender"]["10"],
                COLOR_PRIMITIVES["lavender"]["30"],
                COLOR_PRIMITIVES["lavender"]["60"],
            ],
        },
        "sequential": {
            "blues": [
                COLOR_PRIMITIVES["blue"]["60"],
                COLOR_PRIMITIVES["blue"]["50"],
                COLOR_PRIMITIVES["blue"]["40"],
                COLOR_PRIMITIVES["blue"]["30"],
                COLOR_PRIMITIVES["blue"]["20"],
                COLOR_PRIMITIVES["blue"]["10"],
                COLOR_PRIMITIVES["blue"]["00"],
            ],
            "greens": [
                COLOR_PRIMITIVES["green"]["60"],
                COLOR_PRIMITIVES["green"]["50"],
                COLOR_PRIMITIVES["green"]["40"],
                COLOR_PRIMITIVES["green"]["30"],
                COLOR_PRIMITIVES["green"]["20"],
                COLOR_PRIMITIVES["green"]["10"],
                COLOR_PRIMITIVES["green"]["00"],
            ],
            "reds": [
                COLOR_PRIMITIVES["red"]["60"],
                COLOR_PRIMITIVES["red"]["50"],
                COLOR_PRIMITIVES["red"]["40"],
                COLOR_PRIMITIVES["red"]["30"],
                COLOR_PRIMITIVES["red"]["20"],
                COLOR_PRIMITIVES["red"]["10"],
                COLOR_PRIMITIVES["red"]["00"],
            ],
            "yellows": [
                COLOR_PRIMITIVES["yellow"]["60"],
                COLOR_PRIMITIVES["yellow"]["50"],
                COLOR_PRIMITIVES["yellow"]["40"],
                COLOR_PRIMITIVES["yellow"]["30"],
                COLOR_PRIMITIVES["yellow"]["20"],
                COLOR_PRIMITIVES["yellow"]["10"],
                COLOR_PRIMITIVES["yellow"]["00"],
            ],
            "teals": [
                COLOR_PRIMITIVES["teal"]["60"],
                COLOR_PRIMITIVES["teal"]["50"],
                COLOR_PRIMITIVES["teal"]["40"],
                COLOR_PRIMITIVES["teal"]["30"],
                COLOR_PRIMITIVES["teal"]["20"],
                COLOR_PRIMITIVES["teal"]["10"],
                COLOR_PRIMITIVES["teal"]["00"],
            ],
            "lavenders": [
                COLOR_PRIMITIVES["lavender"]["60"],
                COLOR_PRIMITIVES["lavender"]["50"],
                COLOR_PRIMITIVES["lavender"]["40"],
                COLOR_PRIMITIVES["lavender"]["30"],
                COLOR_PRIMITIVES["lavender"]["20"],
                COLOR_PRIMITIVES["lavender"]["10"],
                COLOR_PRIMITIVES["lavender"]["00"],
            ],
            "grays": [
                COLOR_PRIMITIVES["neutral"]["60"],
                COLOR_PRIMITIVES["neutral"]["50"],
                COLOR_PRIMITIVES["neutral"]["40"],
                COLOR_PRIMITIVES["neutral"]["30"],
                COLOR_PRIMITIVES["neutral"]["20"],
                COLOR_PRIMITIVES["neutral"]["10"],
                COLOR_PRIMITIVES["neutral"]["00"],
            ],
        },
    },
}
