#  Copyright 2022 Feedzai
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

"""Altair theme configuration."""

from .tokens import COLORS, FONT, FONT_SIZES, OPACITIES, SPACING, STROKE_WIDTHS
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
                "gridDash": [2, 4],
                "gridWidth": STROKE_WIDTHS["sm"],
                "labelColor": COLORS["axis"],
                "labelFont": FONT,
                "labelPadding": SPACING["sm"],
                "tickColor": COLORS["axis"],
                "tickOpacity": OPACITIES["md"],
                "tickSize": SPACING["md"],
                "titleColor": COLORS["text"],
                "titleFont": FONT,
                "titleFontSize": FONT_SIZES["sm"],
            },
            "axisBand": {"domain": True, "labelPadding": SPACING["md"], "ticks": False},
            "axisY": {
                "domain": False,
                "titleAlign": "left",
                "titleAngle": 0,
                "titleX": -20,
                "titleY": -10,
            },
            "legend": {
                "labelColor": COLORS["axis"],
                "labelFont": FONT,
                "labelFontSize": FONT_SIZES["sm"],
                "symbolSize": 40,
                "titleColor": COLORS["text"],
                "titleFont": FONT,
                "titleFontSize": FONT_SIZES["sm"],
                "titlePadding": SPACING["md"],
            },
            # Marks
            "arc": {"stroke": COLORS["arc"], "strokeWidth": STROKE_WIDTHS["md"]},
            "bar": {"fill": COLORS["mark"], "stroke": None},
            "line": {"stroke": COLORS["mark"], "strokeWidth": STROKE_WIDTHS["lg"]},
            "path": {"stroke": COLORS["mark"], "strokeWidth": STROKE_WIDTHS["sm"]},
            "point": {"fill": COLORS["mark"], "shape": "circle", "filled": True},
            "rect": {"fill": COLORS["mark"]},
            "rule": {"stroke": COLORS["axis"]},
            "shape": {"stroke": COLORS["mark"]},
            "text": {
                "color": COLORS["text"],
                "font": FONT,
                "fontSize": FONT_SIZES["sm"],
            },
            # Color scales
            "range": {
                "category": COLORS["schemes"]["categorical"]["default"],
                "diverging": COLORS["schemes"]["diverging"]["tealred"],
                "heatmap": COLORS["schemes"]["sequential"]["blues"],
                "ramp": COLORS["schemes"]["sequential"]["blues"],
            },
            # Chart
            "background": COLORS["background"],
            "group": {"fill": COLORS["background"]},
            "header": {
                "labelColor": COLORS["text"],
                "labelFont": FONT,
                "labelFontSize": FONT_SIZES["sm"],
                "titleColor": COLORS["text"],
                "titleFont": FONT,
                "titleFontSize": FONT_SIZES["md"],
            },
            "title": {
                "anchor": "start",
                "color": COLORS["text"],
                "font": FONT,
                "fontSize": FONT_SIZES["lg"],
                "fontWeight": "bold",
                "offset": SPACING["xl"],
                "subtitleColor": COLORS["text"],
                "subtitleFontSize": FONT_SIZES["md"],
            },
            "view": {
                "continuousHeight": 300,
                "continuousWidth": 400,
                "stroke": "transparent",
            },
        }
    }
