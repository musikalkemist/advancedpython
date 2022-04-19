import pytest

from src.project.product import Product
from src.project.errors import CurrencyError
from src.project.utils import create_products


def test_product_init():
    product = Product(name="product_1",
                      currency="dollar",
                      price=13.5)
    assert type(product) == Product
    assert product.name == "product_1"
    assert product.currency == "dollar"
    assert product.price == 13.5


def test_currency_error_raised_when_passing_unsupported_currency():
    with pytest.raises(CurrencyError):
        Product(name="product_1",
                currency="UNSUPPORTED_CURRENCY",
                price=13.5)


def test_product_to_tuple():
    product = Product(name="product_1",
                      currency="dollar",
                      price=13.5)
    product_tuple = product.to_tuple()
    assert len(product_tuple) == 3
    assert type(product_tuple) == tuple
    assert product_tuple[0] == "product_1"
    assert product_tuple[1] == "dollar"
    assert product_tuple[2] == 13.5