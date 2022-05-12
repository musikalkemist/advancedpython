import time


def wait(seconds: int):
    def wait_decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Wait for the magic to happen in {seconds} seconds...")
            time.sleep(seconds)
            func(*args, **kwargs)
        return wrapper
    return wait_decorator


def greet(user):
    def wrapper(*args, **kwargs):
        value = user(*args, **kwargs)
        print(f"Hello {value.name}")
        return value
    return wrapper


@greet
class User:

    def __init__(self, name: str) -> None:
        self.name = name

    @wait(seconds=3)
    def login(self) -> None:
        print(f"You've been logged in {self.name}")



user = User("Josh")
print(user.name)


