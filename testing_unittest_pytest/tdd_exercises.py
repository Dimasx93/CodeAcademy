#Test-driven development lesson                          date 13/03/2025

import pytest


#Exercise n1 TDD: First two of string

def test_if_integer():
    with pytest.raises(ValueError):
        first_two_of_string(22)

def test_is_correct_string():
    assert first_two_of_string("Hello") == "He"

def test_is_shorter_than_2():
    assert first_two_of_string("X") == "X"

def test_is_empty_string():
    assert first_two_of_string("") == "yields the empty string"


def first_two_of_string(value:str)-> str:
    if not isinstance(value, str):
        raise ValueError
    if len (value) >= 2:
        return value[:2]
    elif len(value) == 1:
        return value
    else:
        return "yields the empty string"

################################################################################

#Exercise n2 TDD: Rotated left 2

def test_if_integer_rotated_left():
    with pytest.raises(ValueError):
        rotated_left_2(22)

def test_is_correct_string_rotated_left():
    assert rotated_left_2("Hello") == "lloHe"

def test_less_than_2_rotated_left():
    with pytest.raises(ValueError):
        rotated_left_2("H")
    with pytest.raises(ValueError):
        rotated_left_2("")

def test_exactly_2_chars():
    assert rotated_left_2("Hi") == "Hi"

def rotated_left_2(value:str)-> str:
    if not isinstance(value,str):
        raise ValueError

    if len(value) < 2:
        raise ValueError

    return value[2:] + value[:2]

################################################################################

#Exercise n3 TDD: Which element is larger?

def test_first_is_bigger():
    assert larger_element([3,2,1]) == [3,3,3]

def test_last_is_bigger():
    assert larger_element([1,2,3]) == [3,3,3]

def test_mid_is_bigger():
    assert larger_element([1,3,2]) == [3,3,3]

def test_not_all_int():
    with pytest.raises(ValueError):
        larger_element(["a", 2, 6])

def test_len_not_3():
    with pytest.raises(ValueError):
        larger_element([1])

def test_not_a_list():
    with pytest.raises(TypeError):
        larger_element({1:2})

def larger_element(numbers:list) ->list:
    if not isinstance(numbers, list):
        raise TypeError("You have to put a list.")
    if len(numbers) != 3:
        raise ValueError("List has to be minimum 3 integers")
    if not all(isinstance(number,int)for number in numbers):
            raise ValueError("List must contain only integers")
    max_value = max(numbers)
    return [max_value] * len(numbers)

################################################################################

#Exercise n4 TDD: Sum of two ints with forbidden range

def test_sum_of_2_not_int():
    with pytest.raises(ValueError):
        sum_of_2_int("1", 2)

def test_sum_of_2_len():
    with pytest.raises(ValueError):
        sum_of_2_int(1)

def test_sum_of_2_correct():
    assert sum_of_2_int(10,10)

def test_sum_of_2_incorrect_min_value():
    with pytest.raises(ValueError):
        sum_of_2_int(5,5)

def test_sum_of_2_incorrect_max_value():
    with pytest.raises(ValueError):
        sum_of_2_int(14,5)

def sum_of_2_int(*args)-> int:
    if len(args) != 2:
        raise ValueError("You can sum exactly 2 numbers")
    if not all(isinstance(num, int)for num in args):
        raise ValueError("You have to insert only integers")
    if 10 <= sum(args) <= 19:
        raise ValueError("Value cannot be between 10 to 19")
    return sum(args)
