#Lesson Generators  18/12/2024


#Exercise n1 Next Even Number

# def next_even_num():
#     num = 1
#     while True:
#         if num % 2 == 0:
#             yield num
#             num += 1
#         else:
#             num += 1
#
# gen = next_even_num()
# print(next(gen))
# print(next(gen))

#Exercise n2 Squares Up to a Given Number

# def square_number(number):
#     for num in range(1, number+ 1):
#         yield num ** 2
#
# sq_num = square_number(5)
# for square in sq_num:
#     print(square)

#Exercise n3 Iterating Over a String

# def iterate_string(string):
#     for char in string:
#         yield char
#
# ite_str = iterate_string("Hello, how are you?")
# for character in ite_str:
#     print(character)

#Exercise n4 Yield Only Numbers

# def only_numbers(sample_list:list):
#     for numb in sample_list:
#         if isinstance(numb, (int, float)) and not isinstance(numb, bool):
#             yield numb
#
# on_num = only_numbers([1, "HI", 3, 69, True, 3.5])
# for number in on_num:
#     print(number)

#Exercise n5 Fibonacci Generator

# def fibonacci_gen():
#     num1 = 0
#     num2 = 1
#     while True:
#         yield num1
#         num3 = num1
#         num1 = num2
#         num2 = num3 + num2
#
#
# fibo_gen = fibonacci_gen()
# for x in range(10):
#     print(next(fibo_gen))

#Exercise n6 File Reader

# def file_reader():
#     with open("data.txt" , "r") as f:
#         for line in f:
#             yield line.strip()
#
# gen = file_reader()
# for lines in gen:
#     print(lines)

#Exercise n7 Random Numbers From the Interval

# import random
#
#
# def random_number_generator(n, low, high):
#     for _ in range(n):
#         yield random.randint(low, high)
#
# gen = random_number_generator(5, 1, 100)
# for number in gen:
#     print(number)

#Exercise n8 The Data Pipeline Challenge

from typing import Generator, List, Tuple

# Sample data
people_data: List[Tuple[str, int, str, float]] = [
    ("Alice", 25, "New York", 60000.0),
    ("Bob", 30, "San Francisco", 80000.0),
    ("Charlie", 22, "Los Angeles", 55000.0),
    ("Monica", 35, "Houston", 95000.0),
]


# Generator 1: Filtering Generator
def filter_below_age(
    data: List[Tuple[str, int, str, float]], age_threshold: int
) -> Generator[Tuple[str, int, str, float], None, None]:
    for person in data:
        if person[1] > age_threshold:
            yield person


# Generator 2: Mapping Generator
def map_to_uppercase(
    data: Generator[Tuple[str, int, str, float], None, None]
) -> Generator[Tuple[str, int, str, float], None, None]:
    for person in data:
        yield (person[0].upper(),) + person[1:]


# Generator 3: Aggregation Generator (Running Average)
def calculate_running_average_salary(
    data: Generator[Tuple[str, int, str, float], None, None]
) -> Generator[float, None, None]:
    total_salary = 0
    count = 0
    for person in data:
        total_salary += person[3]
        count += 1
        yield total_salary / count if count > 0 else 0


# Usage
age_threshold = 23

# Step 1: Filter data based on age
filtered_data = filter_below_age(people_data, age_threshold)

# Step 2: Convert the names of people to uppercase
uppercase_names = map_to_uppercase(filtered_data)

# Step 3: Calculate running average salary
running_average_gen = calculate_running_average_salary(uppercase_names)

average_salary: float

# Print the running average salary after each person is processed
for avg_salary in running_average_gen:
    print(f"Running average salary: {avg_salary:.2f}")
    average_salary = avg_salary
# 60000.00
# 70000.00
# 78333.33

print(
    f"The average salary of people above {age_threshold} with uppercase names is: "
    f"{average_salary:.2f}"
)
# The average salary of people above 23 with uppercase names is: 78333.33