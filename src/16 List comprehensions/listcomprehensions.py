"""
List comprehensions:
 - Compact way to create lists
 - Faster than loops to instantiate lists
 - More pythonic!
"""


# basic usage
squares = [0, 1, 4, 9, 16, 25]
squares_list = [i**2 for i in range(6)]

squares_2 = []
for i in range(6):
    squares_2.append(i**2)


# conditionals with list comprehensions
squares_of_even_nums = [i**2 for i in range(6) if i % 2 == 0]

# 0 -> even, 1 -> odd
even_odds = ["even" if i % 2 == 0 else "odd" for i in range(6)]


# nested list comprehensions
matrix = [[0, 1], [0, 1], [0, 1]]
matrix_list = [[i for i in range(3)] for j in range(5)]
print(matrix_list)




