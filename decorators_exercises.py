# Exercise 1: Logging Decorator
# Description:
# Write a decorator called log_execution that logs the name of the function being called and the result it returns.

# def log_execution(some_func):
#     def wrapper(*args, **kwargs):
#         return f"{some_func.__name__} returned {some_func(*args, **kwargs)}"
#     return wrapper
#
# @log_execution
# def add(a, b):
#     return a + b
#
# print(add(3,5))

# Exercise 4: Exception Handling Decorator
# Description:
# Create a decorator called handle_exceptions that catches and logs any exceptions raised by a function and returns a default value.


# def handle_exceptions(some_func):
#     def wrapper(*args, **kwargs):
#         try:
#             some_func(*args, **kwargs)
#         except ZeroDivisionError:
#             return "Cannot divide by 0!"
#         except TypeError:
#             return "Error: Both inputs must be numbers."
#         else:
#             return some_func(*args, **kwargs)
#     return wrapper
#
# @handle_exceptions
# def divide(a, b):
#     return a / b
#
# print(divide(10, "b"))
# print(divide(10, 2))
# print(divide(10, 0))


#Exercise Decorator with Arguments

# def repeat(num_times:int):
#     def repeat_decorator(fn):
#         def wrapper(*args, **kwargs):
#             for _ in range(num_times):
#                 result = fn(*args, ** kwargs)
#             return result
#         return wrapper
#     return repeat_decorator
#
#
#
# @repeat(num_times=3)
# def greet(name):
#     print(f"Hello, {name}!")
#
#
# greet("Alice")

#Exercise Timing Decorator

# import time
#
# def time_execution(some_func):
#     def wrapped(*args, **kwargs):
#         start_time = time.time()
#         result = some_func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"{some_func.__name__} executed in {execution_time:.4f} seconds")
#         return result
#     return wrapped
#
# @time_execution
# def example_function(n):
#     res = 0
#     for i in range(n):
#         res += i
#     return res
#
#
# print(example_function(1000000))

#Exercise Let’s Try Again

import random


def retry(num_retries):
    def decorator(func):
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < num_retries:
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == num_retries - 1:
                        print(f"All {num_retries} attempts failed.")
                        raise  # Re-raise the last exception
                    else:
                        print(f"Attempt {attempt+1} failed: {e}. Retrying...")
                        attempt += 1

        return wrapper

    return decorator

@retry(num_retries=3)
def unreliable_operation():
    """Simulates an operation that may fail."""
    if random.random() < 0.8:
        print("Operation failed!")
        raise ValueError("Random failure occurred.")
    else:
        print("Operation succeeded!")
        return "Success"


try:
    result = unreliable_operation()
    print(f"Result: {result}")
except Exception as e:
    print(f"Final exception after retries: {e}")