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

from typing import TypedDict


class Categorical(TypedDict):
    """Categorical color scheme configurations."""

    default: list[str]
    status: list[str]


class Diverging(TypedDict):
    """Diverging color scheme configurations."""

    bluered: list[str]
    tealred: list[str]
    greenlavender: list[str]


class Sequential(TypedDict):
    """Sequential color scheme configurations."""

    blues: list[str]
    greens: list[str]
    reds: list[str]
    yellows: list[str]
    teals: list[str]
    lavenders: list[str]
    grays: list[str]


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
