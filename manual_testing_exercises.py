# Lesson Introduction to testing: Manual Testing                       date: 10/03/2025

#Exercise n1 Testing simple addition

# def sum_of_three_ints(a: int, b: int, c: int) -> int:
#     return a + b + c
#
#
# def all_negative_inputs():
#     assert sum_of_three_ints(-1, -2, -3) == -6
#
#
# def a_negative_b_c_positive():
#     assert sum_of_three_ints(-1, 2, 3) == 4
#
#
# def a_negative_b_positive_c_negative():
#     assert sum_of_three_ints(-1, 2, -3) == -2
#
#
# def a_b_negative_c_positive():
#     assert sum_of_three_ints(-1, -2, 3) == 0
#
#
# def a_positive_b_negative_c_positive():
#     assert sum_of_three_ints(1, -2, 3) == 2
#
#
# def a_b_positive_c_negative():
#     assert sum_of_three_ints(1, 2, -3) == 0
#
#
# def all_positive_inputs():
#     assert sum_of_three_ints(1, 2, 3) == 6
#
#
# if __name__ == "__main__":
#     all_negative_inputs()
#     a_negative_b_c_positive()
#     a_negative_b_positive_c_negative()
#     a_b_negative_c_positive()
#     a_positive_b_negative_c_positive()
#     a_b_positive_c_negative()
#     all_positive_inputs()
#     print("All tests passed.")

#Exercise n2 Testing finding largest number

# def find_largest_number(numbers: list) -> float:
#     """Finds the largest number in a list of numbers."""
#     if not numbers:
#         return None
#
#     largest = numbers[0]
#     for num in numbers:
#         if num > largest:
#             largest = num
#
#     return largest
#
# def list_positive_int():
#     assert find_largest_number([1,2,3]) == 3
#
# def list_positive_floats():
#     assert find_largest_number([1.2, 2.2, 3.2]) == 3.2
#
# def list_negative_int():
#     assert find_largest_number([-1,-2,-3]) == -1
#
# def list_negative_floats():
#     assert find_largest_number([-1.2, -2.2 , -3.2]) == -1.2
#
# def list_positive_negative_numb():
#     assert find_largest_number([1, -2, 3, -4]) == 3
#
# def empty_list():
#     assert find_largest_number([]) is None
#
# def list_duplicate_values():
#     assert find_largest_number([1, 2, 2]) == 2
#
# if __name__ == "__main__":
#     list_positive_int()
#     list_negative_int()
#     list_positive_floats()
#     list_negative_floats()
#     list_positive_negative_numb()
#     empty_list()
#     list_duplicate_values()
#     print("All tests passed.")

#Exercise n3 Testing the sum function

# def sum_numbers(list_of_numbers: list) -> float:
#     """Sum all numbers in a list."""
#     return sum(list_of_numbers)
#
# def list_negative_int():
#     assert sum_numbers([-1,-2,-3]) == -6.0
#
# # def list_negative_floats():
# #     assert sum_numbers([-1.2, -2.2 , -3.2]) == -6.6
#
# def list_positive_negative_numb():
#     assert sum_numbers([1, -2, 3, -4]) == -2.0
#
# def empty_list():
#     assert sum_numbers([]) == 0
#
# def list_positive_int():
#     assert sum_numbers([1,2,3]) == 6.0
#
# def all_strings():
#     try:
#         sum_numbers(["acc","bcc","ccc"])
#         assert False, "Only int or float allowed."
#     except TypeError as e:
#         pass
#
# if __name__ == "__main__":
#     list_positive_int()
#     list_negative_int()
#     # list_negative_floats()
#     list_positive_negative_numb()
#     empty_list()
#     all_strings()
#     print("All tests passed.")

#Exercise n4 Testing a simple calculator

# from numbers import Number
#
#
# def calculate(num1: Number, num2: Number, operator: str) -> float:
#     """Performs basic arithmetic operations on two numbers using operators (+, -, *, /).
#
#     Raises TypeError if num1 or num2 is not a number
#     Raises TypeError if operator is not a string
#     """
#     if not isinstance(num1, Number) or not isinstance(num2, Number):
#         raise TypeError("The first two arguments must be floats")
#
#     if not isinstance(operator, str):
#         raise TypeError("The operator must be a string")
#
#     if operator == "+":
#         return num1 + num2
#     elif operator == "-":
#         return num1 - num2
#     elif operator == "*":
#         return num1 * num2
#     elif operator == "/":
#         if num2 == 0:
#             raise ZeroDivisionError("Division by zero")
#         return num1 / num2
#     else:
#         raise ValueError("Invalid operator")
#
#
# def calculate_numbers_plus():
#     assert calculate(4, 2, '+') == 6
#
#
# def calculate_numbers_minus():
#     assert calculate(4, 2.0, '-') == 2.0
#
#
# def calculate_numbers_multiply():
#     assert calculate(4.0, 0, '*') == 0
#
#
# def calculate_numbers_division():
#     assert calculate(4.0, 2.0, '/') == 2.0
#
#
# def calculate_division_by_zero():
#     try:
#         calculate(4, 0, '/')
#         assert False, 'Should raise ZeroDivisionError'
#     except ZeroDivisionError:
#         pass
#
#
# def calculate_invalid_operator():
#     try:
#         calculate(4, 0, '()')
#         assert False, 'Should raise ValueError'
#     except ValueError:
#         pass
#
#
# def calculate_strings_plus():
#     try:
#         calculate('abbc', '1', '+')
#         assert False, 'Should raise TypeError'
#     except TypeError:
#         pass
#
#
# def calculate_string_number_plus():
#     try:
#         calculate('4', 0, '+')
#         assert False, 'Should raise TypeError'
#     except TypeError:
#         pass
#
#
# def calculate_string_number_multiply():
#     try:
#         calculate('a', 3, '*')
#         assert False, 'Should raise TypeError'
#     except TypeError:
#         pass
#
#
# if __name__ == "__main__":
#     calculate_numbers_plus()
#     calculate_numbers_minus()
#     calculate_numbers_multiply()
#     calculate_numbers_division()
#     calculate_division_by_zero()
#     calculate_invalid_operator()
#     calculate_strings_plus()
#     calculate_string_number_plus()
#     calculate_string_number_multiply()
#     print("All tests passed.")

#Exercise n5 Testing classes

# class Rectangle:
#     def __init__(self, width: float, height: float):
#         self.width = width
#         self.height = height
#
#     def get_area(self) -> float:
#         return self.width * self.height
#
#     def set_width(self, width: float) -> None:
#         self.width = width
#
#     def set_height(self, height: float) -> None:
#         self.height = height
#
#
# def test_set_width_positive_number():
#     rectangle = Rectangle(4, 2)
#     rectangle.set_width(5)
#     assert rectangle.width == 5
#
#
# def test_set_width_negative_number():
#     rectangle = Rectangle(4, 2)
#     rectangle.set_width(-4)
#     assert rectangle.width == -4
#
#
# def test_set_width_zero():
#     rectangle = Rectangle(4, 2)
#     rectangle.set_width(0)
#     assert rectangle.width == 0
#
#
# def test_set_width_float():
#     rectangle = Rectangle(4, 2)
#     rectangle.set_width(4.5)
#     assert rectangle.width == 4.5
#
#
# def test_set_width_no_value():
#     try:
#         rectangle = Rectangle(4, 2)
#         rectangle.set_width()
#         assert False, 'Should raise TypeError'
#     except TypeError:
#         pass
#
#
# def test_set_height_positive_number():
#     rectangle = Rectangle(4, 2)
#     rectangle.set_height(5)
#     assert rectangle.height == 5
#
#
# def test_set_height_negative_number():
#     rectangle = Rectangle(4, 2)
#     rectangle.set_height(-2)
#     assert rectangle.height == -2
#
#
# def test_set_height_zero():
#     rectangle = Rectangle(4, 2)
#     rectangle.set_height(0)
#     assert rectangle.height == 0
#
#
# def test_set_height_float():
#     rectangle = Rectangle(4, 2)
#     rectangle.set_height(2.5)
#     assert rectangle.height == 2.5
#
#
# def test_set_height_no_value():
#     try:
#         rectangle = Rectangle(4, 2)
#         rectangle.set_height()
#         assert False, 'Should raise TypeError'
#     except TypeError:
#         pass
#
#
# def test_set_height_same_value():
#     rectangle = Rectangle(4, 2)
#     rectangle.set_height(2)
#     assert rectangle.height == 2
#
#
# def test_get_area_numbers():
#     rectangle = Rectangle(4, 2.5)
#     assert rectangle.get_area() == 10.0
#
#
# def test_get_area_strings():
#     rectangle = Rectangle('test', 'test')
#     try:
#         rectangle.get_area()
#         assert False, 'Should raise TypeError'
#     except TypeError:
#         pass
#
#
# def test_get_area_no_values():
#     try:
#         rectangle = Rectangle()
#         rectangle.get_area()
#         assert False, 'Should raise TypeError'
#     except TypeError:
#         pass
#
#
# if __name__ == "__main__":
#     test_set_width_positive_number()
#     test_set_width_negative_number()
#     test_set_width_zero()
#     test_set_width_float()
#     test_set_height_positive_number()
#     test_set_height_negative_number()
#     test_set_height_zero()
#     test_set_height_float()
#     test_set_height_no_value()
#     test_set_height_same_value()
#     test_get_area_numbers()
#     test_get_area_strings()
#     test_get_area_no_values()
#     print("All tests passed.")

# Exercise n7 Implementing a function calculate_grade and testing it

# def calculate_grade(score: int | float) -> tuple:
#     '''
#     Converts a numerical score to a letter grade and calculates bonus points.
#
#     Parameters:
#     score (int): The numerical score, ranging from 0 to 100.
#
#     Returns:
#     tuple: A tuple containing the letter grade and any bonus points awarded.
#     The letter grade is a string ('A', 'B', 'C', 'D', or 'F').
#     The bonus points is an integer representing additional points.
#
#     Grade Conversion Logic:
#     - A: 90-100 (Bonus points: 5)
#     - B: 80-89 (Bonus points: 4)
#     - C: 70-79 (Bonus points: 3)
#     - D: 60-69 (Bonus points: 1)
#     - F: 0-59 (No bonus points)
#     '''
#     if not isinstance(score, int) and not isinstance(score, float):
#         raise TypeError('Score must be a number')
#
#     if score > 100 or score < 0:
#         raise ValueError('Invalid score')
#
#     if score >= 90:
#         return 'A', 5
#     elif score >= 80:
#         return 'B', 4
#     elif score >= 70:
#         return 'C', 3
#     elif score >= 60:
#         return 'D', 1
#     else:
#         return 'F', 0
#
#
# def calculate_grade_valid_score():
#     assert calculate_grade(58) == ('F', 0)
#
#
# def calculate_grade_negative_score():
#     try:
#         calculate_grade(-13)
#         assert False, 'Invalid score'
#     except ValueError:
#         pass
#
#
# def calculate_grade_score_above_100():
#     try:
#         calculate_grade(113)
#         assert False, 'Invalid score'
#     except ValueError:
#         pass
#
#
# def calculate_grade_on_boundary():
#     assert calculate_grade(89.9) == ('B', 4)
#     assert calculate_grade(90.0) == ('A', 5)
#
#
# def calculate_grade_with_bonus_points():
#     assert calculate_grade(81) == ('B', 4)
#     assert calculate_grade(75) == ('C', 3)
#     assert calculate_grade(65) == ('D', 1)
#
#
# def calculate_grade_with_no_bonus_points():
#     assert calculate_grade(59) == ('F', 0)
#     assert calculate_grade(100) == ('A', 5)
#
#
# if __name__ == "__main__":
#     calculate_grade_valid_score()
#     calculate_grade_negative_score()
#     calculate_grade_score_above_100()
#     calculate_grade_on_boundary()
#     calculate_grade_with_bonus_points()
#     calculate_grade_with_no_bonus_points()
#     print("All tests passed.")

#Exercise n8 Implementing a function first_last6 and testing it

def first_last6(nums: list) -> bool:
    if not nums:
        raise ValueError('The length of the list must be at least 1')
    if not all(isinstance(num, int) for num in nums):
        raise TypeError('The list must contain only integers')
    if nums[0] != 6 and nums[-1] != 6:
        return False
    return True


def first_last6_grade_1_6element_length():
    assert first_last6([6])


def first_last6_first_6element():
    assert first_last6([6, 1, 0])


def first_last6_last_6element():
    assert first_last6([1, 6])


def first_last6_empty_list():
    try:
        first_last6([])
        assert False, 'The length of the list must be at least 1'
    except ValueError:
        pass


def first_last6_not_integers():
    try:
        first_last6([6, '6'])
        assert False, 'The list must contain only integers'
    except TypeError:
        pass


def first_last6_not_last_not_first_6element():
    assert not first_last6([1, 6, 3])


def first_last6_no_6element():
    assert not first_last6([1, 5, 3])


if __name__ == "__main__":
    first_last6_grade_1_6element_length()
    first_last6_first_6element()
    first_last6_last_6element()
    first_last6_empty_list()
    first_last6_not_integers()
    first_last6_not_last_not_first_6element()
    first_last6_no_6element()
    print("All tests passed.")

