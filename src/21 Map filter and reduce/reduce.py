# The reduce function applies a function cumulatively on all the items of an iterable
# and returns a single value.

from functools import reduce

numbers = [1, 2, 3]

cumulative_sum = reduce(lambda a, b: a + b, numbers)
print(cumulative_sum)
