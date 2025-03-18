# Lesson Parametrization and fixtures in pytest                      date: 17/03/2025

#Exercise n1 Redo the first lesson’s exercises with parametrization

import pytest

# def sum_of_three_ints(a: int, b: int, c: int) -> int:
#     return a + b + c
#
# @pytest.mark.parametrize("a,b,c, expected_output", [
#     (-1,-2,-3, -6),
#     (-1,2,3, 4),
#     (-1,2,-3, -2),
#     (-1,-2,3, 0),
#     (1,-2,3, 2),
#     (1,2,-3, 0),
#     (1,2,3, 6)
# ])
#
# def test_sum_of_three_ints_good_input(a,b,c, expected_output):
#     assert sum_of_three_ints(a,b,c) == expected_output
#
# #####################################################################################################
#
# #Exercise n2 Testing finding largest number
#
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
# @pytest.mark.parametrize("numbers, expected_output", [
#     ([1,2,3], 3),
#     ([1.2,2.2,3.2], 3.2),
#     ([-1,-2,-3], -1),
#     ([-1.2,-2.2,-3.2], -1.2),
#     ([1,-3,2], 2),
#     ([], None),
#     ([2,3,3,6], 6),
# ])
#
# def test_find_largest_number_assert_cases(numbers, expected_output):
#     assert find_largest_number(numbers) == expected_output

#####################################################################################################

#Exercise n3 Testing the sum function

# def sum_numbers(list_of_numbers: list) -> float:
#     """Sum all numbers in a list."""
#     return sum(list_of_numbers)
#
# @pytest.mark.parametrize("numbers_list, expected_output", [
#     ([-1,-2,-3], -6),
#     ([-1.1,-2.3,-3.2], -6.6),
#     ([1,-2,3,-4], -2),
#     ([], 0),
#     ([1,2,3], 6),
# ])
#
# def test_sum_numbers_assert_cases(numbers_list, expected_output):
#     assert sum_numbers(numbers_list) == expected_output
#
#
# def test_all_strings():
#     with pytest.raises(TypeError):
#         sum_numbers(["acc","bcc","ccc"])

#####################################################################################################

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
# @pytest.mark.parametrize("num1,num2,operator, expected_output", [
#     (4, 2, "+", 6),
#     (4, 2.0, "-", 2.0),
#     (4.0, 0.0, "*", 0),
#     (4.0, 2.0, '/', 2.0),
# ])
#
# def test_calculator_assert_cases(num1, num2, operator, expected_output):
#     calculate(num1,num2,operator) == expected_output
#
# def test_calculate_division_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         calculate(4, 0, '/')
#
# def test_calculate_invalid_operator():
#     with pytest.raises(ValueError):
#         calculate(4, 0, '()')
#
# @pytest.mark.parametrize("num1,num2,operator", [
#     ('abbc', '1', '+'),
#     ('4', 0, '+'),
#     ('a', 3, '*')
# ])
# def test_calculator_type_error(num1, num2, operator):
#     with pytest.raises(TypeError):
#         calculate(num1,num2,operator)

#####################################################################################################

#Exercise n5 Testing classes

class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def get_area(self) -> float:
        return self.width * self.height

    def set_width(self, width: float) -> None:
        self.width = width

    def set_height(self, height: float) -> None:
        self.height = height

@pytest.mark.parametrize("initial_value, new_value, expected_value",[
    (4,5,5),
    (4,-4,-4),
    (4,0,0),
    (4,4.5,4.5),
    (2,2,2),
])

def test_rectangle_assert_width(initial_value, new_value, expected_value):
    rectangle = Rectangle(initial_value, 2)
    rectangle.set_width(new_value)
    assert rectangle.width == expected_value

@pytest.mark.parametrize("initial_value, new_value, expected_value",[
    (4,5,5),
    (4,-4,-4),
    (4,0,0),
    (4,4.5,4.5),
    (2,2,2),
])

def test_rectangle_assert_height(initial_value, new_value, expected_value):
    rectangle = Rectangle(4, initial_value)
    rectangle.set_height(new_value)
    assert rectangle.height == expected_value

def test_set_width_no_value():
    with pytest.raises(TypeError):
        rectangle = Rectangle(4, 2)
        rectangle.set_width()

def test_set_height_no_value():
    with pytest.raises(TypeError):
        rectangle = Rectangle(4, 2)
        rectangle.set_height()

def test_get_area_numbers():
    rectangle = Rectangle(4, 2.5)
    assert rectangle.get_area() == 10.0

def test_get_area_strings():
    rectangle = Rectangle('test', 'test')
    with pytest.raises(TypeError):
        rectangle.get_area()

def test_get_area_no_values():
    with pytest.raises(TypeError):
        rectangle = Rectangle()
        rectangle.get_area()

# Exercise n7 Implementing a function calculate_grade and testing it

def calculate_grade(score: int | float) -> tuple:
    '''
    Converts a numerical score to a letter grade and calculates bonus points.

    Parameters:
    score (int): The numerical score, ranging from 0 to 100.

    Returns:
    tuple: A tuple containing the letter grade and any bonus points awarded.
    The letter grade is a string ('A', 'B', 'C', 'D', or 'F').
    The bonus points is an integer representing additional points.

    Grade Conversion Logic:
    - A: 90-100 (Bonus points: 5)
    - B: 80-89 (Bonus points: 4)
    - C: 70-79 (Bonus points: 3)
    - D: 60-69 (Bonus points: 1)
    - F: 0-59 (No bonus points)
    '''
    if not isinstance(score, int) and not isinstance(score, float):
        raise TypeError('Score must be a number')

    if score > 100 or score < 0:
        raise ValueError('Invalid score')

    if score >= 90:
        return 'A', 5
    elif score >= 80:
        return 'B', 4
    elif score >= 70:
        return 'C', 3
    elif score >= 60:
        return 'D', 1
    else:
        return 'F', 0


def test_calculate_grade_valid_score():
    assert calculate_grade(58) == ('F', 0)

def test_calculate_grade_negative_score():
    with pytest.raises(ValueError):
        calculate_grade(-13)

def test_calculate_grade_score_above_100():
    with pytest.raises(ValueError):
        calculate_grade(113)

def test_calculate_grade_on_boundary():
    assert calculate_grade(89.9) == ('B', 4)
    assert calculate_grade(90.0) == ('A', 5)

def test_calculate_grade_with_bonus_points():
    assert calculate_grade(81) == ('B', 4)
    assert calculate_grade(75) == ('C', 3)
    assert calculate_grade(65) == ('D', 1)

def test_calculate_grade_with_no_bonus_points():
    assert calculate_grade(59) == ('F', 0)
    assert calculate_grade(100) == ('A', 5)


#Exercise n8 Implementing a function first_last6 and testing it

def first_last6(nums: list) -> bool:
    if not nums:
        raise ValueError('The length of the list must be at least 1')
    if not all(isinstance(num, int) for num in nums):
        raise TypeError('The list must contain only integers')
    if nums[0] != 6 and nums[-1] != 6:
        return False
    return True

@pytest.mark.parametrize("input_correct, expected_output", [
    ([6], True),
    ([6,1,0], True),
    ([1,6], True),
    ([1,6,3], False),
    ([1,5,3], False),
])

def test_first_last6_assert(input_correct, expected_output):
    assert first_last6(input_correct) == expected_output

@pytest.mark.parametrize("bad_value", [
    [1,"1"],
    ["aaa", 5]
])

def test_first_last6_value_error(bad_value):
    with pytest.raises(TypeError):
        first_last6(bad_value)

@pytest.mark.parametrize("bad_input", [
    [],
])

def test_first_last6_empty_list(bad_input):
    with pytest.raises(ValueError):
        first_last6(bad_input)