import random
from typing import List, Dict
from pathlib import Path

from src.project.errors import DifferentNumberOfArgumentsError
from src.project.product import Product
from src.project.loading.serialization import JsonSerializer


def accepts_types(*expected_types):
    """Decorator that checks that the arguments of a method are valid.

    :raise TypeError: If type of argument isn't valid
    :raise DifferentNumberOfArgumentsError: If number of arguments passed to the
        decorator and to the method (minus self) aren't the same
    """
    def check_types(func):
        def wrapper(*args, **kwargs):
            args_without_self = args[1:]
            _raise_error_if_number_of_passed_and_expected_arguments_dont_match(args_without_self, expected_types)
            _raise_type_error_if_passed_and_expected_types_dont_match(args_without_self, expected_types)
            return func(*args, **kwargs)
        return wrapper
    return check_types


def _raise_error_if_number_of_passed_and_expected_arguments_dont_match(passed_args, expected_types):
    if len(passed_args) != len(expected_types):
        msg = "Number of arguments passed in decorator " \
              f"{len(expected_types)} doesn't match with number of " \
              f"arguments in method, i.e., {len(passed_args)}"
        raise DifferentNumberOfArgumentsError(msg)


def _raise_type_error_if_passed_and_expected_types_dont_match(passed_args, expected_types):
    for (arg, expected_type) in zip(passed_args, expected_types):
        if not isinstance(arg, expected_type):
            raise TypeError(f"Argument '{arg}' is of type {type(arg)}. "
                            f"'{expected_type}' expected instead")


def create_products(product_parameters: List[Dict]) -> List[Product]:
    """Factory function that creates a list of products from a list of
    dictionaries representing product parameters.
    """
    return [Product(**p) for p in product_parameters]


def nest_list(list: list, nested_list_length: int) -> List[List]:
    new_list = []
    nested_list = []
    for item in list:
        nested_list.append(item)
        if len(nested_list) == nested_list_length:
            new_list.append(nested_list)
            nested_list = []
    if len(nested_list) != 0:
        new_list.append(nested_list)
    return new_list


def create_file_paths_from_dir(directory: Path) -> List[Path]:
    return [path for path in directory.iterdir() if path.is_file()]


def generate_dummy_product_files(directory: Path, number_files: int) -> None:
    serializer = JsonSerializer()
    for i in range(number_files):
        data = {
            "name": f"product_{i+1}",
            "currency": _randomly_select_currency(0.3),
            "price": random.randint(10, 1000)
        }
        serializer.dump(data, Path(directory, f"{i+1}.json"))


def _randomly_select_currency(probability_euro: float = 0.5):
    if random.random() > probability_euro:
        return "dollar"
    return "euro"
