from pathlib import Path

from setuptools import find_packages, setup


def get_version(root: Path, rel_path: str) -> str:
    """Get the package version from a given file."""
    for line in (root / rel_path).read_text().splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


here: Path = Path(__file__).parent.resolve()

setup(
    name="feedzai-altair-theme",
    version=get_version(here, "feedzai_altair_theme/__init__.py"),
    description="Feedzai's theme for Altair charts.",
    author="Feedzai",
    url="https://github.com/feedzai/feedzai-altair-theme",
    packages=find_packages(),
    python_requires=">=3.7",
)
