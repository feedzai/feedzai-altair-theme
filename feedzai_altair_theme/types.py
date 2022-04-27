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


class Config(TypedDict):
    """Chart theme configuration."""

    axis: Axis


class Theme(TypedDict):
    """Wrapper for the chart theme configuration."""

    config: Config
