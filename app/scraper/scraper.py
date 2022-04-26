"""
scraper.py

Created by Stephen Andrews, April 26th, 2022.
"""
from abc import ABC, abstractmethod
from typing import List

from app.model.product import Product


class Scraper(ABC):
    """An abstract base class for scraper implementations."""

    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_products(self) -> List[Product]:
        pass
