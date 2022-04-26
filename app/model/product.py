"""
product.py

Created by Stephen Andrews, April 26th, 2022.
"""

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: float
