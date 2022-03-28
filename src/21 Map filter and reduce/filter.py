# The filter function takes in a function that returns a bool and an iterable(list, tuple, etc.) as an input.
# It applies passed function to each item of an iterable and returns a filter object (an iterator).

numbers = [1, 2, 3, 4]
evens_only = filter(lambda n: n % 2 == 0, numbers)

print(list(evens_only))

