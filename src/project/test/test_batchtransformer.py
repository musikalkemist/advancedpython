import pytest

from src.project.transforming.batchtransformer import BatchTransformer
from src.project.transforming.currencyconverter import CurrencyConverter
from src.project.transforming.pricemultiplier import PriceMultiplier
from src.project.product import Product


@pytest.fixture
def batch_transformer():
    exchange_rate = {"euro": {"dollar": 2}}
    currency_converter = CurrencyConverter(exchange_rate, "euro")
    price_multiplier = PriceMultiplier(2)
    return BatchTransformer([currency_converter, price_multiplier])


def test_batch_transform_init(batch_transformer):
    assert type(batch_transformer) == BatchTransformer
    assert len(batch_transformer.transforms) == 2
    assert type(batch_transformer.transforms[0]) == CurrencyConverter


def test_apply_transforms(batch_transformer):
    products = [Product(name="product_1", currency="dollar", price=10.),
                Product(name="product_2", currency="euro", price=10.)]
    transformed_products = batch_transformer.apply(products)
    assert len(transformed_products) == 2
    assert transformed_products[0].currency == "euro"
    assert transformed_products[0].price == 40.
    assert transformed_products[1].price == 20.

