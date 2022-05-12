# Lambda is an anonymous function
# Can take any number of params, but only 1 expression
# It's useful when used with other functions (e.g., map, reduce, filter)

def square(n: int) -> int:
    return n**2

square_lambda = lambda n: n**2

# print(square_lambda(2))

minimum = lambda x, y: x if x < y else y
print(minimum(1, 2))

