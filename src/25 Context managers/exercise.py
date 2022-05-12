from time import perf_counter


class CodeExecutionTimer:

    def __init__(self):
        self.start_time = None
        self.stop_time = None

    def __enter__(self):
        self.start_time = perf_counter()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.stop_time = perf_counter()
        print(f"Execution time: {self.stop_time - self.start_time} seconds")


if __name__ == "__main__":
    with CodeExecutionTimer():
        squares = [n**2 for n in range(100000)]
