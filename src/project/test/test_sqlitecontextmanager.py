from sqlite3 import Cursor
import os

from src.project.storing.sqlitecontextmanager import SQLiteContextManager


def test_sqlite_context_manager_init():
    sqlite_context_manger = SQLiteContextManager("dummy2.db")
    assert type(sqlite_context_manger) == SQLiteContextManager


def test_enter_context_manager():
    with SQLiteContextManager("dummy.db") as cursor:
        assert type(cursor) == Cursor
    os.remove("dummy.db")

