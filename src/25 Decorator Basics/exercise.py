from time import perf_counter


def print_time(func):
    def wrapper():
        start_time = perf_counter()
        func()
        stop_time = perf_counter()
        print(f"Execution time: {stop_time - start_time} seconds")
    return wrapper


@print_time
def create_one_million_squares_list():
    return [n**2 for n in range(1000000)]


if __name__ == "__main__":
    create_one_million_squares_list()