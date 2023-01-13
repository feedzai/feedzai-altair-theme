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

from pathlib import Path
from typing import Dict, List

from setuptools import find_packages, setup

HERE: Path = Path(__file__).parent.resolve()

ENTRY_POINTS: Dict[str, List[str]] = {
    # Group: https://github.com/altair-viz/altair/blob/v4.2.0/altair/vegalite/v4/theme.py#L35
    "altair.vegalite.v4.theme": [
        "feedzai = feedzai_altair_theme.theme:feedzai",
    ],
}
DEPENDENCIES: List[str] = ["altair==4.*", "typing-extensions==4.0.*"]


def get_version(root: Path, rel_path: str) -> str:
    """Get the package version from a given file."""
    for line in (root / rel_path).read_text().splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="feedzai-altair-theme",
    version=get_version(HERE, "feedzai_altair_theme/__init__.py"),
    description="Feedzai's theme for Altair charts.",
    long_description=(HERE / "README.md").read_text(),
    long_description_content_type="text/markdown",
    author="Feedzai",
    url="https://github.com/feedzai/feedzai-altair-theme",
    packages=find_packages(),
    install_requires=DEPENDENCIES,
    entry_points=ENTRY_POINTS,
    python_requires=">=3.7, <4",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering :: Visualization",
        "Topic :: Utilities",
        "Typing :: Typed",
    ],
    keywords="altair, theme, data, visualization",
    project_urls={
        "Bug Reports": "https://github.com/feedzai/feedzai-altair-theme/issues",
        "Changelog": "https://github.com/feedzai/feedzai-altair-theme/blob/master/CHANGELOG.md",
        "Source": "https://github.com/feedzai/feedzai-altair-theme",
    },
)
