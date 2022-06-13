class PowerSum:

    def __init__(self,
                 exponent: int,
                 start: int,
                 stop: int) -> None:
        self.exponent = exponent
        self.start = start
        self.stop = stop
        self._sum = 0

    def __iter__(self):
        self.num = self.start
        return self

    def __next__(self):
        if self.num > self.stop:
            raise StopIteration
        power = pow(self.num, self.exponent)
        self.num += 1
        self._sum += power
        return self._sum


if __name__ == "__main__":
    power_sum = PowerSum(2, 0, 3)
    for sum_ in power_sum:
        print(sum_)
