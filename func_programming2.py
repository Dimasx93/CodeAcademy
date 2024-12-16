#Lesson Functional Programming Intro (Part 2)

from functools import reduce


#Exercise n1 Square All Numbers

# numbers = [1, 2, 3, 4]
#
# square_numbers = list(map(lambda num: num**2 , numbers))
# print(square_numbers)

#Exercise n2 Triple All Numbers

# numbers = [1, 2, 3, 4]
#
# triple_numbers = list(map(lambda num: num * 3, numbers))
# print(triple_numbers)

#Exercise n3 Convert Integers to Strings

# data = [1, 2, 3]
# data_tuple = (4, 5, 6)
#
# # convert_to_strings = list(map(str, data + list(data_tuple)))
# def convert_to_strings(string):
#     return list(map(str, string))
# print(convert_to_strings(data + list(data_tuple)))

#Exercise n4 Sum Three Lists

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [7, 8, 9]
#
# add_three_lists = list(map(lambda z,y,x: z+y+x, a,b,c))
# print(add_three_lists)

#Exercise n5 Sum and Differences of Two Lists

# a = [1, 2, 3]
# b = [3, 2, 1]
#
# add_and_diff_lists = list(map(lambda x,y: (x+y , abs(x-y)), a,b))
# print(add_and_diff_lists)

#Exercise n6 Separate by Parity

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# def filter_integers(numbers):
#     evens = list(filter(lambda x: x % 2 == 0, numbers))
#     odds = list(filter(lambda x: x % 2 != 0, numbers))
#     return evens, odds
# evens, odds = filter_integers(numbers)
# print("Even numbers:", evens)  # Output: [2, 4, 6, 8, 10]
# print("Odd numbers:", odds)  # Output: [1, 3, 5, 7, 9]

#Exercise n7 Filter by Divisibility

# numbers = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
#
# def divisible_by(numbers):
#     return list(filter(lambda x: x % 13 or x % 19 == 0, numbers))
# print(divisible_by(numbers))

#Exercise n8 Multiply All Numbers

# numbers = [1, 2, 3, 4]
#
# multiply_list = reduce(lambda x,y: x*y, numbers)
# print(multiply_list)

#Exercise n9 Concatenate Strings

# strings = ["Hello", "World", "From", "Python"]
#
# concatenate_strings = reduce(lambda a,b: a+b, strings)
# print(concatenate_strings)

#Exercise n10 Count Even and Odd Numbers

# numbers = [1, 2, 3, 5, 7, 8, 9, 10]
#
# def count_even_odd(numbers):
#     counts = reduce(lambda acc, x: (acc[0] + (x % 2 == 0), acc[1] + (x % 2 != 0)), numbers, (0, 0))
#     return counts
# even_count, odd_count = count_even_odd(numbers)
# print("Number of even numbers:", even_count)  # Output: 3
# print("Number of odd numbers:", odd_count)  # Output: 5

#Exercise n11 Find Maximum Value

numbers = [1, 2, 3, 4, 5]

find_max = reduce(lambda x, y: x if x > y else y, numbers)

print(find_max)