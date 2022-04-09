import math
from typing import Generator


def factorial_generator(start: int, stop: int) -> Generator:
    number = start
    while number <= stop:
        value = math.factorial(number)
        yield value
        number += 1


for factorial in factorial_generator(0, 3):
    print(factorial)
