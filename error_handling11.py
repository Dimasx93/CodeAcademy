#Lesson n11 Error Handling and exceptions
#
##Exercise n1 Built-in Exceptions
#
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     except TypeError:
#         print("Error: Both arguments must be numbers.")
#
#
# def open_file(filename):
#     try:
#         with open(filename, 'r') as f:
#             return f.read()
#     except FileNotFoundError:
#         print(f"Error: The file '{filename}' was not found.")
#
#
# def convert_to_int(value):
#     try:
#         return int(value)
#     except ValueError:
#         print(f"Error: Cannot convert '{value}' to an integer.")
#
#
# def access_list_element(my_list, index):
#     try:
#         return my_list[index]
#     except IndexError:
#         print(f"Error: Index {index} is out of bounds.")
#     except TypeError:
#         print("Error: List and index must be of correct types.")
#
#
# def read_dictionary_key(my_dict, key):
#     try:
#         return my_dict[key]
#     except KeyError:
#         print(f"Error: Key '{key}' does not exist in the dictionary.")
#
#
# # Example usage:
# divide(10, 0)  # ZeroDivisionError
# open_file("non_existent_file.txt")  # FileNotFoundError
# convert_to_int("abc")  # ValueError
# access_list_element([1, 2, 3], 10)  # IndexError
# read_dictionary_key({"name": "Alice"}, "age")  # KeyError
#
##Exercise n2 Safe divide
#
# def divide(a, b):
#     try:
#         output = a / b
#     except ZeroDivisionError:
#         print("Cannot divide by zero")
#     except TypeError:
#         print("At least one of the var is not an int")
#     else:
#         print("Division was successful.")
#         return output
#     finally:
#         print("Executing finally clause")
# # Division by zero
# print(divide(10, 0))
#
# # Non-numeric input
# print(divide(10, "a"))
#
# # Successful division
# print(divide(10, 2))
#
##Exercise n3 Simple Calculator
#
# def calculator(a,b):
#     try:
#         a = float(a)
#         b = float(b)
#         sum_result = a + b
#         sub_result = a - b
#         mul_result = a * b
#         div_result = a / b
#
#     except ValueError:
#         print("Error: Please enter valid numeric values.")
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     except TypeError:
#         print("Error: Both inputs must be numbers.")
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#
#     else:
#         print(f"Sum: {sum_result}")
#         print(f"Subtraction: {sub_result}")
#         print(f"Multiplication: {mul_result}")
#         print(f"Division: {div_result}")
#
# calculator("ten", 2)  # ValueError (Non-numeric input)
# calculator(10, 0)  # ZeroDivisionError (Division by zero)
# calculator(10, 2)  # Successful run (No errors)
#
##Exercise n4 Custom Exception
#
# class TooLargeNumberError(Exception):
#     """Custom exception for handling numbers that are too large."""
#     pass
#
#
# def calculator(num1, num2):
#     try:
#         if num1 > 1_000_000 or num2 > 1_000_000:
#             raise TooLargeNumberError(
#                 "Error: One of the numbers is too large (greater than 1,000,000)."
#             )
#
#         num1 = float(num1)
#         num2 = float(num2)
#
#         sum_result = num1 + num2
#         sub_result = num1 - num2
#         mul_result = num1 * num2
#         div_result = num1 / num2
#
#         print(f"Sum: {sum_result}")
#         print(f"Subtraction: {sub_result}")
#         print(f"Multiplication: {mul_result}")
#         print(f"Division: {div_result}")
#
#     except ValueError:
#         print("Error: Please enter valid numeric values.")
#     except ZeroDivisionError:
#         print("Error: Division by zero is not allowed.")
#     except TypeError:
#         print("Error: Both inputs must be numbers.")
#     except TooLargeNumberError as e:
#         print(e)
#     except Exception as e:
#         print(f"An unexpected error occurred: {e}")
#
#
# # Example usage:
# calculator("ten", 2)  # ValueError (Non-numeric input)
# calculator(10, 0)  # ZeroDivisionError (Division by zero)
# calculator(10, 2)  # Successful run (No errors)
# calculator(10_000_000, 2)  # TooLargeNumberError (custom exception)