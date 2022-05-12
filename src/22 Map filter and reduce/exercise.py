from math import sqrt
from functools import reduce


l = [2, 4 ,16, 80]

# Exercise 1
l_divided_by_2 = map(lambda n: n / 2, l)
print(list(l_divided_by_2))

# Exercises 2
l_filtered = filter(lambda n: sqrt(n).is_integer(), l)
print(list(l_filtered))

# Exercises 3
l2 = [1, 2, 3]
cumulative_product = reduce(lambda current_product, value: current_product * value, l2)
print(cumulative_product)