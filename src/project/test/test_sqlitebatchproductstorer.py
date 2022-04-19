import sqlite3
import os

import pytest

from src.project.storing.sqlitebatchproductstorer import SQLiteBatchProductStorer
from src.project.product import Product
from src.project.storing.createdb import create_db


@pytest.fixture
def products():
    return [Product(name="product_1", currency="dollar", price=10.),
            Product(name="product_2", currency="euro", price=10.)]


@pytest.fixture
def expected_product_list():
    return [("product_1", "dollar", 10.), ("product_2", "euro", 10.)]


def test_sqlite_batch_product_storer_init():
    product_storer = SQLiteBatchProductStorer("table")
    assert type(product_storer) == SQLiteBatchProductStorer
    assert product_storer.table == "table"


def test_products_are_inserted_in_db(products, expected_product_list):
    try:
        create_db("dummy.db")
        product_storer = SQLiteBatchProductStorer("product")
        connection = sqlite3.connect("dummy.db")
        cursor = connection.cursor()

        product_storer.store(cursor, products)
        cursor.execute("SELECT NAME, CURRENCY, PRICE FROM PRODUCT")
        products = cursor.fetchall()

        assert products == expected_product_list
    finally:
        os.remove("dummy.db")


def test_convert_products_to_list(products, expected_product_list):
    products_list = SQLiteBatchProductStorer._convert_products_to_list(products)
    assert products_list == expected_product_list