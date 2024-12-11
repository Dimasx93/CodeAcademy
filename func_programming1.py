# Lesson Functional Programming Intro (Part 1)    date 11/12/2024

# Exercise n1 Check Initial Character

# check_initial_char = lambda s, string: s == string[0]
#
# print(check_initial_char("hello", "z"))

# Exercise n2 Simple Lambda Calculations

# add_15 = lambda s: s + 15
# multiply = lambda s,x: s * x
#
# print(add_15(15))
# print(multiply(10, 2))

# Exercise n3 Square and Cube with Lambda
# numbers = [1,2,3,4,5]
#
# print(list(map(lambda x: (x**2, x**3), numbers )))

# Exercise n4 Extract Date and Time Components

# from datetime import datetime
#
# time_now = datetime.now()
#
# extract_time = lambda x: (print(x.year), print(x.month), print(x.day), print(x.time()))
# extract_time(time_now)
# Result on CodeAcademyOnline
# date_time_extractor = lambda x: (x.year, x.month, x.day, x.time())
# year, month, day, time = date_time_extractor(time_now)
# print(time_now, year, month, day, time, sep="\n")

# Exercise n5 Sort List of Tuples

# list_tuples = [("English", 88), ("Science", 90), ("Maths", 97), ("Social sciences", 82)]
# print(sorted(list_tuples, key=lambda x: x[1]))

# Exercise n6 Sort List of Dictionaries by Color

# phones_models = [
#     {"make": "Nokia", "model": 216, "color": "Black"},
#     {"make": "Mi Max", "model": 2, "color": "Gold"},
#     {"make": "Samsung", "model": 7, "color": "Blue"},
# ]
#
# print(sorted(phones_models, key=lambda x: x["color"]))

# Exercise n7 Sort Matrix by Row Sums

# original_matrices = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

# print(sorted(original_matrices, key=lambda x: sum(x)))

# Exercise n8 Deep Nested List Sum with a Condition

def deep_sum_divisible_by(lst, n):
    def is_divisible(x):
        return x % n == 0

    def sum_nested(x):
        if isinstance(x, int):
            return x if is_divisible(x) else 0
        elif isinstance(x, (list, tuple)):
            return sum(map(sum_nested, x))
        return 0

    return sum_nested(lst)


# Example usage:

# Example No. 1:
nested_list = [1, [2, [3, 4], 5], [6, [7, [8], 9]], 10]
n = 3
print(f"The sum of numbers divisible by {n} in the list is:", end=" ")
print(deep_sum_divisible_by(nested_list, n))

# Example No. 2:
nested_list = [1, (2, [3, 4], 5), [6, (7, [8], 9)], 10]
n = 2
print(f"The sum of numbers divisible by {n} in the list is:", end=" ")
print(deep_sum_divisible_by(nested_list, n))
