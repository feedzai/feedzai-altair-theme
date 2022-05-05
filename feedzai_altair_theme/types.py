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

"""Theme-related types."""

from tokenize import group
from typing import List, Optional

from typing_extensions import TypedDict


class Axis(TypedDict, total=False):
    """`axis`, `axisBand`, and `axisY` configurations."""

    domain: bool
    domainColor: str
    grid: bool
    gridCap: str
    gridColor: str
    gridDash: List[int]
    gridWidth: float
    labelColor: str
    labelFont: str
    labelPadding: int
    tickColor: str
    tickOpacity: float
    ticks: bool
    tickSize: int
    titleAlign: str
    titleAngle: int
    titleColor: str
    titleFont: str
    titleFontSize: int
    titleX: int
    titleY: int


class Legend(TypedDict):
    """`legend` configuration."""

    labelColor: str
    labelFont: str
    labelFontSize: int
    symbolSize: int
    titleColor: str
    titleFont: str
    titleFontSize: int
    titlePadding: int


class Mark(TypedDict, total=False):
    """`arc`, `bar`, `line`, `path`, `point`, `rect`, `rule`, `shape`, `text`, and `group` configurations."""

    color: str
    fill: str
    filled: bool
    font: str
    fontSize: int
    shape: str
    stroke: Optional[str]
    strokeWidth: float


class ScaleRange(TypedDict):
    """Scale `range` configuration."""

    category: List[str]
    diverging: List[str]
    heatmap: List[str]
    ramp: List[str]


class Header(TypedDict):
    """`header` configuration."""

    labelColor: str
    labelFont: str
    labelFontSize: int
    titleColor: str
    titleFont: str
    titleFontSize: int


class Title(TypedDict):
    """`title` configuration."""

    anchor: str
    color: str
    font: str
    fontSize: int
    fontWeight: str
    offset: int
    subtitleColor: str
    subtitleFontSize: int


class View(TypedDict):
    """`view` configuration."""

    continuousHeight: int
    continuousWidth: int
    stroke: str


class Config(TypedDict):
    """Chart theme configuration."""

    axis: Axis
    axisBand: Axis
    axisY: Axis
    legend: Legend
    arc: Mark
    bar: Mark
    line: Mark
    path: Mark
    point: Mark
    rect: Mark
    rule: Mark
    shape: Mark
    text: Mark
    range: ScaleRange
    background: str
    group: Mark
    header: Header
    title: Title
    view: View


class Theme(TypedDict):
    """Wrapper for the chart theme configuration."""

    config: Config


class Categorical(TypedDict):
    """Categorical color scheme configurations."""

    default: List[str]
    status: List[str]


class Diverging(TypedDict):
    """Diverging color scheme configurations."""

    bluered: List[str]
    tealred: List[str]
    greenlavender: List[str]


class Sequential(TypedDict):
    """Sequential color scheme configurations."""

    blues: List[str]
    greens: List[str]
    reds: List[str]
    yellows: List[str]
    teals: List[str]
    lavenders: List[str]
    grays: List[str]


class ColorScheme(TypedDict):
    """Color scheme configuration."""

    categorical: Categorical
    diverging: Diverging
    sequential: Sequential


class Colors(TypedDict):
    """Colors token."""

    arc: str
    axis: str
    background: str
    grid: str
    mark: str
    text: str
    schemes: ColorScheme


"""
Color token

Colors should be ordered from lightest to darkest, where '00' is the lightest color and
'60' is  the darkest color.
"""
Color = TypedDict(
    "Color",
    {"00": str, "10": str, "20": str, "30": str, "40": str, "50": str, "60": str},
)
