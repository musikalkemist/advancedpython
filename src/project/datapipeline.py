from typing import List, Dict
from pathlib import Path
from sqlite3 import Cursor

from project.loading.loaderiterator import LoaderIterator
from project.transforming.batchtransformer import BatchTransformer
from project.storing.sqlitebatchproductstorer import SQLiteBatchProductStorer
from project.storing.sqlitecontextmanager import SQLiteContextManager
from project.utils import create_products
from project.utils import accepts_types
from project.loading.serialization import JsonSerializer
from project.transforming.currencyconverter import CurrencyConverter, latest_exchange_rates
from project.transforming.pricemultiplier import PriceMultiplier


class DataPipeline:
    """A class that wraps the different components of the system. It processes
    data using these steps:  load -> apply transforms -> store
    """

    def __init__(self,
                 loader_iterator: LoaderIterator,
                 batch_transformer: BatchTransformer,
                 storer: SQLiteBatchProductStorer,
                 sqlite_context_manager: SQLiteContextManager) -> None:
        self.loader_iterator = loader_iterator
        self.batch_transformer = batch_transformer
        self.storer = storer
        self.sqlite_context_manager = sqlite_context_manager

    @accepts_types(list)
    def process(self, load_paths: List[Path]) -> None:
        """Process files in batches: load -> transform -> store to db."""
        self.loader_iterator.load_paths = load_paths
        with self.sqlite_context_manager as db_cursor:
            for product_data_batch in self.loader_iterator:
                 self._process_product_batch(db_cursor, product_data_batch)

    def _process_product_batch(self,
                               db_cursor: Cursor,
                               product_data_batch: List[Dict]) -> None:
        products = create_products(product_data_batch)
        transformed_products = self.batch_transformer.apply(products)
        self.storer.store(db_cursor, transformed_products)


def create_hardcoded_data_pipeline() -> DataPipeline:
    loader_iterator = LoaderIterator(JsonSerializer(), 2)
    batch_transformer = BatchTransformer(
         [CurrencyConverter(latest_exchange_rates, "euro"),
         PriceMultiplier(0.8)])
    product_storer = SQLiteBatchProductStorer()
    sqlite_context_manager = SQLiteContextManager("test.db")
    return DataPipeline(loader_iterator,
                        batch_transformer,
                        product_storer,
                        sqlite_context_manager)
