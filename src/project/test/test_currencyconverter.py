import pytest

from src.project.transforming.currencyconverter import CurrencyConverter, latest_exchange_rates
from src.project.product import Product


@pytest.fixture
def product():
    return Product(name="product_1",
                   currency="dollar",
                   price=10.)


@pytest.fixture
def currency_converter():
    exchange_rate = {"euro": {"dollar": 2}}
    return CurrencyConverter(exchange_rate, "euro")


def test_apply_on_product_that_doesnt_have_target_currency(currency_converter):
    product = Product(name="product_1",
                      currency="euro",
                      price=10.)
    new_product = currency_converter.apply(product)
    assert new_product == product


def test_create_currency_converted_product_is_called_once(currency_converter, mocker):
    product = Product(name="product_1",
                      currency="dollar",
                      price=10.)
    mock_method = mocker.patch.object(currency_converter, "_create_currency_converted_product", autospec=True)
    mock_method.return_value = "dummy"
    _ = currency_converter.apply(product)
    mock_method.assert_called_once_with(product)


def test_apply_on_product_that_already_has_target_currency(product, currency_converter):
    currency_converted_product = currency_converter.apply(product)
    assert currency_converted_product.price == 20.
    assert currency_converted_product.name == "product_1"
    assert currency_converted_product.currency == "euro"


def test_currenty_converted_product_is_created(product, currency_converter):
    currency_converted_product = currency_converter._create_currency_converted_product(product)
    assert currency_converted_product.price == 20.
    assert currency_converted_product.name == "product_1"
    assert currency_converted_product.currency == "euro"


def test_convert_price(product, currency_converter):
    converted_price = currency_converter._convert_price(product)
    assert converted_price == 20.


def test_currency_converter_init():
    currency_converter = CurrencyConverter(latest_exchange_rates, "euro")
    assert type(currency_converter) == CurrencyConverter
    assert currency_converter.exchange_rates == latest_exchange_rates
    assert currency_converter.target_currency == "euro"



