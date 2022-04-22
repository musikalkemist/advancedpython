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
    def check_currence_is_supported(cls, value: str, values: dict) -> str:
        if value not in supported_currencies:
            msg = f"Currency '{value}' isn't supported in product '{values['name']}'."
            raise CurrencyError(msg)
        return value

    def to_tuple(self):
        """Convert Product object to a list of the type:
        (name, currency, price).
        """
        return (self.name, self.currency, self.price)
