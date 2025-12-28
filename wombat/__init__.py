"""Wombat - Reddit scraping CLI tool"""

__version__ = "0.1.0"

from .reddit import initialize_reddit

__all__ = ["initialize_reddit", "__version__"]
