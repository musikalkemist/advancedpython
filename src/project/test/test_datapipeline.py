import os
import sqlite3
from pathlib import Path

import pytest

from src.project.datapipeline import DataPipeline, create_hardcoded_data_pipeline
from src.project.loading.loaderiterator import LoaderIterator
from src.project.loading.serialization import JsonSerializer
from src.project.transforming.batchtransformer import BatchTransformer
from src.project.transforming.currencyconverter import CurrencyConverter, latest_exchange_rates
from src.project.transforming.pricemultiplier import PriceMultiplier
from src.project.storing.sqlitebatchproductstorer import SQLiteBatchProductStorer
from src.project.storing.sqlitecontextmanager import SQLiteContextManager
from src.project.storing.createdb import create_db



@pytest.fixture
def product_data():
    return 


@pytest.fixture
def expected_db_product_output():
    return [
        ("product_1", "euro", 220.),
        ("product_2", "euro", 22.),
        ("product_3", "euro", 22.),
        ("product_4", "euro", 22.),
        ("product_5", "euro", 20.)
    ]


@pytest.fixture
def data_pipeline():
    loader_iterator = LoaderIterator(JsonSerializer(), 2)
    batch_transformer = BatchTransformer([CurrencyConverter(latest_exchange_rates, "euro"),
                                          PriceMultiplier(2.)])
    product_storer = SQLiteBatchProductStorer()
    sqlite_context_manager = SQLiteContextManager("dummy.db")
    return DataPipeline(loader_iterator,
                        batch_transformer,
                        product_storer,
                        sqlite_context_manager)


def test_data_pipeline_init():
    data_pipeline = DataPipeline("load_iterator", "transformer", "storer", "context")
    assert type(data_pipeline) == DataPipeline
    assert data_pipeline.loader_iterator == "load_iterator"
    assert data_pipeline.batch_transformer == "transformer"
    assert data_pipeline.storer == "storer"


def test_process_files(data_pipeline, expected_db_product_output):
    files = [Path("files/1.json"), Path("files/2.json"), Path("files/3.json"),
             Path("non-existing"), Path("files/4.json"), Path("files/5.json")]

    try:
        create_db("dummy.db")
        connection = sqlite3.connect("dummy.db")
        cursor = connection.cursor()

        data_pipeline.process(files)

        cursor.execute("SELECT NAME, CURRENCY, PRICE FROM PRODUCT")
        products = cursor.fetchall()

        for i in range(len(products)):
            assert products[i][0] == expected_db_product_output[i][0]
            assert products[i][1] == expected_db_product_output[i][1]
            assert products[i][2] == pytest.approx(expected_db_product_output[i][2])
    finally:
        os.remove("dummy.db")


def test_process_product_batch(data_pipeline, expected_db_product_output):
    product_data = [
        {
            "name": "product_1",
            "currency": "dollar",
            "price": 100
        },
        {
            "name": "product_2",
            "currency": "dollar",
            "price": 10
        },
        {
            "name": "product_3",
            "currency": "dollar",
            "price": 10
        },
        {
            "name": "product_4",
            "currency": "dollar",
            "price": 10
        },
        {
            "name": "product_5",
            "currency": "euro",
            "price": 10
        }
    ]
    try:
        create_db("dummy.db")
        connection = sqlite3.connect("dummy.db")
        cursor = connection.cursor()

        data_pipeline._process_product_batch(cursor, product_data)

        cursor.execute("SELECT NAME, CURRENCY, PRICE FROM PRODUCT")
        products = cursor.fetchall()

        for i in range(len(products)):
            assert products[i][0] == expected_db_product_output[i][0]
            assert products[i][1] == expected_db_product_output[i][1]
            assert products[i][2] == pytest.approx(expected_db_product_output[i][2])
    finally:
        os.remove("dummy.db")


def test_hardcoded_data_pipeline_is_instantiated():
    data_pipeline = create_hardcoded_data_pipeline()
    assert type(data_pipeline) == DataPipeline
