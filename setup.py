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
DEPENDENCIES: List[str] = ["altair==4.*"]


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
        "Development Status :: 2 - Pre-Alpha",
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
        "Source": "https://github.com/feedzai/feedzai-altair-theme",
    },
)
