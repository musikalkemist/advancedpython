from abc import ABC, abstractmethod

from src.project.product import Product


class Transform(ABC):
    """Interface for concrete Transform which modify a product object."""

    @abstractmethod
    def apply(self, product: Product) -> Product:
        """Apply a transform to a product. Method must be implemented by
        concrete transforms."""
