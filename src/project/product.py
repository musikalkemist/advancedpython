from typing import Tuple

from pydantic import BaseModel, validator

from src.project.errors import CurrencyError


supported_currencies = ["dollar", "euro"]


class Product(BaseModel):
    """This class represent a product entry."""

    name: str
    currency: str
    price: float

    @validator("currency")
    @classmethod
    def check_currency_is_supported(cls, value: str, values: dict) -> str:
        if value not in supported_currencies:
            msg = f"Currency '{value}' isn't supported in product '{values['name']}'."
            raise CurrencyError(value, msg)
        return value

    def to_tuple(self) -> Tuple:
        """Convert Product object to a tuple of the type:
        (name, currency, price).
        """
        return (self.name, self.currency, self.price)
