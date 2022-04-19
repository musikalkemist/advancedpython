from src.project.transforming.pricemultiplier import PriceMultiplier
from src.project.product import Product


def test_price_multiplier_init():
    price_multiplier = PriceMultiplier(0.8)
    assert type(price_multiplier) == PriceMultiplier
    assert price_multiplier.multiplier == 0.8


def test_apply():
    price_multiplier = PriceMultiplier(0.8)
    product = Product(name="product_1",
                      currency="dollar",
                      price=10.)

    transformed_product = price_multiplier.apply(product)
    assert transformed_product != product
    assert transformed_product.name == product.name
    assert transformed_product.currency == product.currency
    assert transformed_product.price == 8.

