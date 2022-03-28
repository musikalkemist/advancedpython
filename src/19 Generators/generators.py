# def composer_generator():
#     yield "Beethoven"
#     yield "Mozart"
#     yield "Haydn"
#
# composer = composer_generator()

# print(next(composer))
# print(next(composer))
# print(next(composer))
# print(next(composer))

# for c in composer:
#     print(c)

def squares_sum(start, stop):
    i = start
    sum = 0
    while i < stop:
        square = i ** 2
        sum += square
        yield sum
        i += 1

s = squares_sum(0, 3)
print(next(s))
print(next(s))
print(next(s))
print(next(s))







