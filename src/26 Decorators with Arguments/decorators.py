import time


### decorators with function arguments ###

def greetings(func):
    def wrapper(*args, **kwargs):
        print("Welcome!")
        func(*args, **kwargs)
        print("Bye!")
        return args[0]
    return wrapper


@greetings
def hello(name: str):
    print(f"Hello {name}")


# name = hello("Josh")
# print()
# print(name)


def timing(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        stop_time = time.perf_counter()
        time_elapsed = stop_time - start_time
        print(f"It took {time_elapsed} seconds to run the function.")
        return value
    return wrapper

@timing
def squares(stop_number):
    return [x**2 for x in range(stop_number)]


# l_squares = squares(1000000)
# print(l_squares[:10])


### decorators with arguments ###

def wait(seconds: int):
    def wait_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Wait for the magic to happen in {seconds} seconds...")
            time.sleep(seconds)
            func(*args, **kwargs)
        return wrapper
    return wait_decorator


@wait(3)
@greetings
def hello(name: str):
    print(f"Hello {name}")

hello("Anna")
























