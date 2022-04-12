# Exercise 1
def check_int(func):
    def wrapper(*args, **kwargs):
        if not isinstance(args[0], int):
            raise TypeError(f"The argument isn't an int. '{type(args[0])}' passed instead.")
        value = func(*args, **kwargs)
        return value
    return wrapper


@check_int
def create_squares_list(stop: int):
   return [n**2 for n in range(stop)]


# Exercise 2
def filter_divisible_by(divisor: int):
    def filter_divisible_by_decorator(func):
        def wrapper(*args, **kwargs):
            values = func(*args, **kwargs)
            filtered_values = list(filter(lambda x: x % divisor == 0, values))
            return filtered_values
        return wrapper
    return filter_divisible_by_decorator


@filter_divisible_by(2)
def create_squares_list(stop: int):
   return [n**2 for n in range(stop)]


print(create_squares_list(10))

