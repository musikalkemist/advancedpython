from typing import Dict

from src.project.transforming.transform import Transform
from src.project.product import Product
from src.project.utils import accepts_types


latest_exchange_rates = {
    "euro": {"dollar": 1.1},
    "dollar": {"euro": 0.909}
}


class CurrencyConverter(Transform):
    """Convert the currency of a product, changing its currency and adjusting
    the price according to the exchange rate. It's a concrete Transform.
    """

    def __init__(self,
                 exchange_rates: Dict[str, Dict[str, float]],
                 target_currency: str = "dollar") -> None:
        self.exchange_rates = exchange_rates
        self.target_currency = target_currency

    @accepts_types(Product)
    def apply(self, product: Product) -> Product:
        """Convert currency and adjust price. If product currency is already
        target currency, no changes are applied.
        """
        if product.currency == self.target_currency:
            return product
        return self._create_currency_converted_product(product)

    def _create_currency_converted_product(self, product: Product) -> Product:
        currency_converted_product_params = {
            "name": product.name,
            "currency": self.target_currency,
            "price": self._convert_price(product)
        }
        return Product(**currency_converted_product_params)

    def _convert_price(self, product: Product) -> float:
        exchange_rate = self.exchange_rates[self.target_currency][product.currency]
        return product.price * exchange_rate
