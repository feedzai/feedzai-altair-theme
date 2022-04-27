"""Altair theme configuration."""

from .tokens import COLORS, FONT, FONT_SIZES, OPACITIES, STROKE_WIDTHS
from .types import Theme


def feedzai() -> Theme:
    """Feedzai theme (light theme)."""
    return {
        "config": {
            # Guides
            "axis": {
                "domain": True,
                "domainColor": COLORS["axis"],
                "grid": False,
                "gridCap": "round",
                "gridColor": COLORS["grid"],
                "gridDash": [3, 5],
                "gridWidth": 0.8,
                "labelColor": COLORS["axis"],
                "labelFont": FONT,
                "labelPadding": 3,
                "tickColor": COLORS["axis"],
                "tickOpacity": OPACITIES["md"],
                "tickSize": 5,
                "titleColor": COLORS["text"],
                "titleFont": FONT,
                "titleFontSize": FONT_SIZES["sm"],
            },
            "axisBand": {"domain": True, "ticks": False, "labelPadding": 7},
            "axisY": {
                "domain": False,
                "titleAlign": "left",
                "titleAngle": 0,
                "titleX": -20,
                "titleY": -10,
            },
            "legend": {
                "labelColor": COLORS["axis"],
                "labelFontSize": FONT_SIZES["sm"],
                "symbolSize": 40,
                "titleColor": COLORS["text"],
                "titleFontSize": FONT_SIZES["sm"],
                "titlePadding": 10,
                "titleFont": FONT,
                "labelFont": FONT,
            },
            # Marks
            "line": {"stroke": COLORS["mark"], "strokeWidth": STROKE_WIDTHS["lg"]},
            "rule": {"stroke": COLORS["axis"]},
            "path": {"stroke": COLORS["mark"], "strokeWidth": STROKE_WIDTHS["sm"]},
            "rect": {"fill": COLORS["mark"]},
            "point": {"filled": True, "shape": "circle", "fill": COLORS["mark"]},
            "shape": {"stroke": COLORS["mark"]},
            "bar": {"fill": COLORS["mark"], "stroke": None},
            "text": {
                "font": FONT,
                "color": COLORS["text"],
                "fontSize": FONT_SIZES["sm"],
            },
            "arc": {"stroke": COLORS["arc"], "strokeWidth": STROKE_WIDTHS["md"]},
            # Color scales
            "range": {
                "category": COLORS["schemes"]["categorical"]["default"],
                "ramp": COLORS["schemes"]["sequential"]["blues"],
                "heatmap": COLORS["schemes"]["sequential"]["blues"],
                "diverging": COLORS["schemes"]["diverging"]["tealred"],
            },
            # Chart
            "title": {
                "anchor": "start",
                "fontSize": FONT_SIZES["lg"],
                "color": COLORS["text"],
                "fontWeight": "bold",
                "offset": 20,
                "font": FONT,
                "subtitleColor": COLORS["text"],
                "subtitleFontSize": FONT_SIZES["md"],
            },
            "header": {
                "labelFontSize": FONT_SIZES["sm"],
                "titleFontSize": FONT_SIZES["md"],
                "labelColor": COLORS["text"],
                "titleColor": COLORS["text"],
                "titleFont": FONT,
                "labelFont": FONT,
            },
            "group": {"fill": COLORS["background"]},
            "background": COLORS["background"],
            "view": {
                "stroke": "transparent",
                "continuousHeight": 300,
                "continuousWidth": 400,
            },
        }
    }
