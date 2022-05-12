from math import pow

# Exercise 1
dict_1 = {f"power_{power}": [pow(i, power) for i in range(4)] for power in range(4)}
print(dict_1)

# Exercise 2
sample_dict = {
    "a": 1,
    "b": 4,
    "c": 17,
    "d": 16
}
filtered_dict = {k:v for (k, v) in sample_dict.items() if v % 4 == 0}
print(filtered_dict)