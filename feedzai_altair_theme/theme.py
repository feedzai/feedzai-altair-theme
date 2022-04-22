"""Altair theme configuration."""

from .tokens import COLORS


def feedzai():
    """Feedzai theme (light theme)."""
    return {
        "config": {
            "axis": {
                "domain": True,
                "domainColor": COLORS["axis"],
            }
        }
    }
