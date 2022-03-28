squares = {0: 0, 1: 1, 2: 4, 3: 9}

squares_2 = {n:n**2 for n in range(4)}

square_dictionary = {"a": 0, "b": 4, "c": 9}

dictionary = {"a": 0, "b": 2, "c": 3}
square_dictionary_2 = {k:v**2 for (k, v) in dictionary.items()}

even_odd_dict = {k: ("even" if v % 2 == 0 else "odd") for (k, v) in dictionary.items()}
print(even_odd_dict)
