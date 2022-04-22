"""Altair theme configuration."""

from .tokens import COLORS, FONT, FONT_SIZES, OPACITIES


def feedzai():
    """Feedzai theme (light theme)."""
    return {
        "config": {
            "axis": {
                "domain": True,
                "domainColor": COLORS["axis"],
                "grid": False,
                "gridColor": COLORS["grid"],
                "gridDash": [3, 5],
                "gridWidth": 0.8,
                "gridCap": "round",
                "labelPadding": 3,
                "labelFont": FONT,
                "labelColor": COLORS["axis"],
                "tickSize": 5,
                "tickColor": COLORS["axis"],
                "tickOpacity": OPACITIES["md"],
                "titleColor": COLORS["text"],
                "titleFont": FONT,
                "titleFontSize": FONT_SIZES["sm"],
            },
            "axisBand": {
                "domain": True,
                "ticks": False,
                "labelPadding": 7,
            },
        }
    }
