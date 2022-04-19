from pathlib import Path

from src.project.utils import create_products
from src.project.utils import create_file_paths_from_dir, nest_list
from src.project.product import Product



def test_create_products():
    product_params = [
        {
            "name": "product_1",
            "currency": "dollar",
            "price": 100
        },
        {
            "name": "product_2",
            "currency": "dollar",
            "price": 10
        }
    ]
    products = create_products(product_params)
    assert len(products) == 2
    assert type(products[0]) == Product
    assert products[1].price == 10.0


def test_create_file_paths_from_dir():
    dir = Path("files")
    paths = create_file_paths_from_dir(dir)
    assert paths == [Path("files/5.json"), Path("files/4.json"), Path("files/3.json"), Path("files/2.json"), Path("files/1.json")]


def test_nest_list():
    l = [0, 1, 2, 3, 4, 5]

    nested_l = nest_list(l, 6)
    assert nested_l == [[0, 1, 2, 3, 4, 5]]

    nested_l = nest_list(l, 5)
    assert nested_l == [[0, 1, 2, 3, 4], [5]]

    nested_l = nest_list(l, 4)
    assert nested_l == [[0, 1, 2, 3], [4, 5]]

    nested_l = nest_list(l, 3)
    assert nested_l == [[0, 1, 2], [3, 4, 5]]
    
    nested_l = nest_list(l, 2)
    assert nested_l == [[0, 1], [2, 3], [4, 5]]
    
    nested_l = nest_list(l, 1)
    assert nested_l == [[0], [1], [2], [3], [4], [5]]

