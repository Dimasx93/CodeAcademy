# Lesson Introduction to testing: Pytest Testing                       date: 12/03/2025

# Exercise n2 Testing balanced parentheses

import pytest

def test_empty_string():
    assert is_balanced("")

def test_balanced_simple_parentheses():
    assert is_balanced("()")
    assert is_balanced("[]")
    assert is_balanced("{}")

def test_balanced_mixed_types():
    assert is_balanced("{[()]}")

def test_unbalanced_brackets():
    assert not is_balanced("(")
    assert not is_balanced("[}")
    assert not is_balanced("{[}")

def test_long_balanced_expression():
    assert is_balanced("{[()()]}[()]")

def test_long_unbalanced_expression():
    assert not is_balanced("((()))]")

def test_nested_balanced_brackets():
    assert is_balanced("{({[]})}")

def test_nested_unbalanced_brackets():
    assert not is_balanced("{([)]}")

def test_strings_with_characters():
    assert is_balanced("a(b[c]{d}e)f")

def test_incorrect_closing_bracket():
    assert not is_balanced("(]")

def test_non_string_input():
    with pytest.raises(TypeError):
        is_balanced(123)

# Modifying the original function to include error handling
def is_balanced(expression: str) -> bool:
    if not isinstance(expression, str):
        raise TypeError("Input must be a string")
    stack = []
    mapping = {")": "(", "]": "[", "}": "{"}
    for char in expression:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping:
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

########################################################################

#Exercise n3 Testing Roman numeral to integer conversion

def test_basic_symbols():
    assert roman_to_int("I") == 1
    assert roman_to_int("V") == 5
    # Add assertions for all individual symbols

def test_standard_cases():
    assert roman_to_int("II") == 2
    assert roman_to_int("XIII") == 13
    assert roman_to_int("LVIII") == 58

def test_subtractive_notation():
    assert roman_to_int("IV") == 4
    assert roman_to_int("IX") == 9
    assert roman_to_int("XC") == 90

def test_upper_limit():
    assert roman_to_int("MMMCMXCIX") == 3999

def test_combination_of_all_symbols():
    assert roman_to_int("MCMXLIV") == 1944

def test_empty_string():
    assert roman_to_int("") == 0

def test_invalid_characters():
    with pytest.raises(ValueError):
        roman_to_int("ABC")

def test_lowercase_input():
    with pytest.raises(ValueError):
        roman_to_int("mmcmxcix")

def test_non_string_inputs():
    with pytest.raises(TypeError):
        roman_to_int(123)

def test_repeating_subtractive_notation():
    with pytest.raises(ValueError):
        roman_to_int("IVIV")

# Updated function with error handling
def roman_to_int(roman_num: str) -> int:
    if not isinstance(roman_num, str):
        raise TypeError("Input must be a string")
    if any(ch not in "IVXLCDM" for ch in roman_num.upper()):
        raise ValueError("Invalid Roman numeral")
    if roman_num != roman_num.upper():
        raise ValueError("Input must be uppercase Roman numerals")
    invalid_subtractive = ["IVIV", "IXIX", "XCXC", "CMCM"]
    for pattern in invalid_subtractive:
        if pattern in roman_num:
            raise ValueError("Invalid repetition of subtractive notation")

    roman_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "M": 1000}
    total = 0
    prev_val = 0
    for char in roman_num.upper():
        val = roman_map[char]
        total += val
        if prev_val < val:
            total -= 2 * prev_val
        prev_val = val
    return total