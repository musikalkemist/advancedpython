from math import sqrt

# Exercise 1
list_1 = [sqrt(i) for i in range(10)]
print(list_1)

# Exercise 2
list_2 = [sqrt(i) if i % 3 == 0 else i**2 for i in range(20)]
print(list_2)

# Exercise 3
list_3 = [ [i*j for i in range(3)] for j in range(4)]
print(list_3)