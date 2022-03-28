# The map function takes in a function and an iterable(list, tuple, etc.) as an input.
# It applies passed function to each item of an iterable and returns a map object (an iterator).

def square(n):
    return n**2

numbers = [1, 2, 3]

squared_numbers = map(square, numbers)
#print(list(squared_numbers))

even_odd = map(lambda n: "even" if n % 2 == 0 else "odd", numbers)
print(list(even_odd))



