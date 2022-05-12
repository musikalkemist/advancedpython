from __future__ import annotations

# l = [1, 2, 3]
#
# l_iterator = iter(l)
# print(next(l_iterator))
# print(next(l_iterator))
# print(next(l_iterator))
# print(next(l_iterator))

class Square:

    def __init__(self, start: int, stop: int) -> None:
        self.start = start
        self.stop = stop

    def __iter__(self) -> Square:
        self.num = self.start
        return self

    def __next__(self) -> int:
        if self.num > self.stop:
            raise StopIteration
        square = self.num ** 2
        self.num += 1
        return square


if __name__ == "__main__":
    square = Square(0, 5)

    square_i = iter(square)
    print(next(square_i))
    print(next(square_i))
    print(next(square_i))
    print(next(square_i))
    print(next(square_i))
    print(next(square_i))
    print(next(square_i))




