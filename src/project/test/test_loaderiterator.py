from pathlib import Path

import pytest

from src.project.loading.loaderiterator import LoaderIterator
from src.project.loading.serialization import JsonSerializer


@pytest.fixture
def loader_iterator():
    paths = [Path("files/1.json"), Path("files/2.json"), Path("non-existing-path"),
             Path("files/3.json"), Path("files/4.json"), Path("files/5.json")]
    return LoaderIterator(JsonSerializer(), 2, paths)


def test_loader_iterator_init():
    loader_iterator = LoaderIterator(JsonSerializer(), 3, "dummy_paths")
    assert type(loader_iterator) == LoaderIterator
    assert type(loader_iterator.serializer) == JsonSerializer
    assert loader_iterator.load_paths == "dummy_paths"
    assert loader_iterator.num_files_per_iteration == 3


def test_loop_through_loaded_data(loader_iterator):
    expected_data = [
        [
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
        ],
        [
            {
                "name": "product_3",
                "currency": "dollar",
                "price": 10
            }
        ],
        [
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
    ]

    for i, data in enumerate(loader_iterator):
        assert data == expected_data[i]


def test_iter(loader_iterator):
    assert loader_iterator._current_iteration == None
    iterator = iter(loader_iterator)
    assert loader_iterator._current_iteration == 0
    assert type(iterator) == LoaderIterator


def test_next(loader_iterator):
    iterator = iter(loader_iterator)

    data_iteration_0 = next(iterator)
    expected_data_iteration_0 = [
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
    assert data_iteration_0 == expected_data_iteration_0

    data_iteration_1 = next(iterator)
    expected_data_iteration_1 = [
        {
            "name": "product_3",
            "currency": "dollar",
            "price": 10
        }
    ]
    assert data_iteration_1 == expected_data_iteration_1

    data_iteration_2 = next(iterator)
    expected_data_iteration_2 = [
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
    assert data_iteration_2 == expected_data_iteration_2

    with pytest.raises(StopIteration):
        next(iterator)


def test_load_data_batch(loader_iterator):
    loader_iterator._current_iteration = 0
    expected_data = [
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
    loaded_data = loader_iterator._load_data_batch()
    assert loaded_data == expected_data


def test_load_data_batch_with_non_existing_file(loader_iterator):
    loader_iterator._current_iteration = 1
    expected_data = [
        {
            "name": "product_3",
            "currency": "dollar",
            "price": 10
        }
    ]
    loaded_data = loader_iterator._load_data_batch()
    assert loaded_data == expected_data


def test_did_load_all_batches(loader_iterator):
    loader_iterator._current_iteration = 0
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 1
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 2
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 3
    assert loader_iterator._did_load_all_batches() == True

    loader_iterator.load_paths = [1, 2, 3, 4, 5, 6, 7]
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 4
    assert loader_iterator._did_load_all_batches() == True

    loader_iterator.load_paths = [1, 2, 3, 4, 5, 6, 7, 8]
    assert loader_iterator._did_load_all_batches() == True

    loader_iterator.num_files_per_iteration = 3
    loader_iterator.load_paths = [1, 2, 3, 4, 5]
    loader_iterator._current_iteration = 0
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 1
    assert loader_iterator._did_load_all_batches() == False

    loader_iterator._current_iteration = 2
    assert loader_iterator._did_load_all_batches() == True

