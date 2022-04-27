"""Theme-related types."""

from typing import List

from typing_extensions import TypedDict


class Axis(TypedDict):
    """`axis` configuration."""

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
    tickSize: int
    titleColor: str
    titleFont: str
    titleFontSize: int


class AxisBand(TypedDict):
    """`axisBand` configuration."""

    domain: bool
    labelPadding: int
    ticks: bool


class AxisY(TypedDict):
    """`axisY` configuration."""

    domain: bool
    titleAlign: str
    titleAngle: int
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


class Config(TypedDict):
    """Chart theme configuration."""

    axis: Axis
    axisBand: AxisBand
    axisY: AxisY
    legend: Legend


class Theme(TypedDict):
    """Wrapper for the chart theme configuration."""

    config: Config
