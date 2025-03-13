# Lesson Introduction to testing: Unittest Testing                       date: 12/03/2025

# Exercise n1 Do all exercises from the previous lesson but in unittest

# Exercise n1 Testing simple addition

import unittest


def sum_of_three_ints(a: int, b: int, c: int) -> int:
    return a + b + c


class TestSumOfThreeInts(unittest.TestCase):

    def test_all_negative_inputs(self):
        self.assertEqual(sum_of_three_ints(-1, -2, -3), -6)

    def test_a_negative_b_c_positive(self):
        self.assertEqual(sum_of_three_ints(-1, 2, 3), 4)

    def test_a_negative_b_positive_c_negative(self):
        self.assertEqual(sum_of_three_ints(-1, 2, -3), -2)

    def test_a_b_negative_c_positive(self):
        self.assertEqual(sum_of_three_ints(-1, -2, 3), 0)

    def test_a_positive_b_negative_c_positive(self):
        self.assertEqual(sum_of_three_ints(1, -2, 3), 2)

    def test_a_b_positive_c_negative(self):
        self.assertEqual(sum_of_three_ints(1, 2, -3), 0)

    def test_all_positive_inputs(self):
        self.assertEqual(sum_of_three_ints(1, 2, 3), 6)


if __name__ == "__main__":
    unittest.main()

######################################################################################################

# Exercise n2 Testing finding largest number

def find_largest_number(numbers: list) -> float:
    """Finds the largest number in a list of numbers."""
    if not numbers:
        return None

    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num

    return largest


class FindLargestNumber(unittest.TestCase):

    def test_list_positive_int(self):
        self.assertEqual(find_largest_number([1, 2, 3]) , 3)

    def test_list_positive_floats(self):
        self.assertEqual(find_largest_number([1.2, 2.2, 3.2]) , 3.2)

    def test_list_negative_int(self):
        self.assertEqual(find_largest_number([-1, -2, -3]) , -1)

    def test_list_negative_floats(self):
        self.assertEqual(find_largest_number([-1.2, -2.2, -3.2]) , -1.2)

    def test_list_positive_negative_numb(self):
        self.assertEqual(find_largest_number([1, -2, 3, -4]) , 3)

    def test_empty_list(self):
        self.assertEqual(find_largest_number([]) , None)

    def test_list_duplicate_values(self):
        self.assertEqual(find_largest_number([1, 2, 2]) , 2)


if __name__ == "__main__":
    unittest.main()

###################################################################################################

# Exercise n3 Testing the sum function


def sum_numbers(list_of_numbers: list) -> float:
    """Sum all numbers in a list."""
    return sum(list_of_numbers)

class SumNumbers(unittest.TestCase):
    def test_list_negative_int(self):
        self.assertEqual(sum_numbers([-1,-2,-3]) , -6.0)

    def test_list_negative_floats(self):
        self.assertEqual(sum_numbers([-1.1, -2.2 , -3.3]) , -6.6)

    def test_list_positive_negative_numb(self):
        self.assertEqual(sum_numbers([1, -2, 3, -4]) , -2.0)

    def test_empty_list(self):
        self.assertEqual(sum_numbers([]) , 0)

    def test_list_positive_int(self):
        self.assertEqual(sum_numbers([1,2,3]) , 6.0)

    def test_all_strings(self):
        with self.assertRaises(TypeError, msg="Should raise TypeError on strings"):
            sum_numbers(["abc", "bca", "cab"])

if __name__ == "__main__":
    unittest.main()

###################################################################################################

# Exercise n4 Testing a simple calculator

from numbers import Number


def calculate(num1: Number, num2: Number, operator: str) -> float:
    """Performs basic arithmetic operations on two numbers using operators (+, -, *, /).

    Raises TypeError if num1 or num2 is not a number
    Raises TypeError if operator is not a string
    """
    if not isinstance(num1, Number) or not isinstance(num2, Number):
        raise TypeError("The first two arguments must be floats")

    if not isinstance(operator, str):
        raise TypeError("The operator must be a string")

    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            raise ZeroDivisionError("Division by zero")
        return num1 / num2
    else:
        raise ValueError("Invalid operator")

class Calculate(unittest.TestCase):

    def test_calculate_numbers_plus(self):
        self.assertEqual(calculate(4, 2, '+') , 6)

    def test_calculate_numbers_minus(self):
        self.assertEqual(calculate(4, 2.0, '-') , 2.0)

    def test_calculate_numbers_multiply(self):
        self.assertEqual(calculate(4.0, 0, '*') , 0)

    def test_calculate_numbers_division(self):
        self.assertEqual(calculate(4.0, 2.0, '/') , 2.0)

    def test_calculate_division_by_zero(self):
        with self.assertRaises(ZeroDivisionError, msg='Should raise ZeroDivisionError'):
            calculate(4, 0, '/')

    def test_calculate_invalid_operator(self):
        with self.assertRaises(ValueError, msg='Should raise ValueError'):
            calculate(4, 0, '()')

    def test_calculate_strings_plus(self):
        with self.assertRaises(TypeError, msg='Should raise TypeError'):
            calculate('abbc', '1', '+')

    def test_calculate_string_number_plus(self):
        with self.assertRaises(TypeError, msg='Should raise TypeError'):
            calculate('4', 0, '+')

    def test_calculate_string_number_multiply(self):
        with self.assertRaises(TypeError, msg='Should raise TypeError'):
            calculate('a', 3, '*')



if __name__ == "__main__":
    unittest.main()

###################################################################################################

# Exercise n5 Testing classes

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

class RectangleTest(unittest.TestCase):

    def test_set_width_positive_number(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_width(5)
        self.assertEqual(rectangle.width , 5)

    def test_set_width_negative_number(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_width(-4)
        self.assertEqual(rectangle.width , -4)

    def test_set_width_zero(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_width(0)
        self.assertEqual(rectangle.width , 0)

    def test_set_width_float(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_width(4.5)
        self.assertEqual(rectangle.width , 4.5)

    def test_set_width_no_value(self):
        with self.assertRaises(TypeError, msg='Should raise TypeError'):
            rectangle = Rectangle(4, 2)
            rectangle.set_width()

    def test_set_height_positive_number(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_height(5)
        self.assertEqual(rectangle.height , 5)

    def test_set_height_negative_number(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_height(-2)
        self.assertEqual(rectangle.height , -2)

    def test_set_height_zero(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_height(0)
        self.assertEqual(rectangle.height , 0)

    def test_set_height_float(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_height(2.5)
        self.assertEqual(rectangle.height , 2.5)

    def test_set_height_no_value(self):
        with self.assertRaises(TypeError, msg='Should raise TypeError'):
            rectangle = Rectangle(4, 2)
            rectangle.set_height()

    def test_set_height_same_value(self):
        rectangle = Rectangle(4, 2)
        rectangle.set_height(2)
        self.assertEqual(rectangle.height , 2)

    def test_get_area_numbers(self):
        rectangle = Rectangle(4, 2.5)
        self.assertEqual(rectangle.get_area() , 10.0)

    def test_get_area_strings(self):
        rectangle = Rectangle('test', 'test')
        with self.assertRaises(TypeError, msg='Should raise TypeError'):
            rectangle.get_area()

    def test_get_area_no_values(self):
        with self.assertRaises(TypeError, msg='Should raise TypeError'):
            rectangle = Rectangle()
            rectangle.get_area()



if __name__ == "__main__":
    unittest.main()

###################################################################################################

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

class CalculateGrade(unittest.TestCase):

    def test_calculate_grade_valid_score(self):
        self.assertEqual(calculate_grade(58) , ('F', 0))

    def test_calculate_grade_negative_score(self):
        with self.assertRaises(ValueError, msg='Invalid score'):
            calculate_grade(-13)

    def test_calculate_grade_score_above_100(self):
        with self.assertRaises(ValueError, msg='Invalid score'):
            calculate_grade(113)

    def test_calculate_grade_on_boundary(self):
        self.assertEqual(calculate_grade(89.9) , ('B', 4))
        self.assertEqual(calculate_grade(90.0) , ('A', 5))

    def test_calculate_grade_with_bonus_points(self):
        self.assertEqual(calculate_grade(81) , ('B', 4))
        self.assertEqual(calculate_grade(75) , ('C', 3))
        self.assertEqual(calculate_grade(65) , ('D', 1))

    def test_calculate_grade_with_no_bonus_points(self):
        self.assertEqual(calculate_grade(59) , ('F', 0))
        self.assertEqual(calculate_grade(100) , ('A', 5))


if __name__ == "__main__":
    unittest.main()

###################################################################################################

# Exercise n8 Implementing a function first_last6 and testing it

def first_last6(nums: list) -> bool:
    if not nums:
        raise ValueError('The length of the list must be at least 1')
    if not all(isinstance(num, int) for num in nums):
        raise TypeError('The list must contain only integers')
    if nums[0] != 6 and nums[-1] != 6:
        return False
    return True

class FirstLast6(unittest.TestCase):

    def test_first_last6_grade_1_6element_length(self):
        self.assertTrue(first_last6([6]))

    def test_first_last6_first_6element(self):
        self.assertTrue(first_last6([6, 1, 0]))

    def test_first_last6_last_6element(self):
        self.assertTrue(first_last6([1, 6]))

    def test_first_last6_empty_list(self):
        with self.assertRaises(ValueError, msg='The length of the list must be at least 1'):
            first_last6([])

    def test_first_last6_not_integers(self):
        with self.assertRaises(TypeError, msg='The list must contain only integers'):
            first_last6([6, '6'])

    def test_first_last6_not_last_not_first_6element(self):
        self.assertFalse(first_last6([1, 6, 3]))

    def test_first_last6_no_6element(self):
        self.assertFalse(first_last6([1, 5, 3]))


if __name__ == "__main__":
    unittest.main()
