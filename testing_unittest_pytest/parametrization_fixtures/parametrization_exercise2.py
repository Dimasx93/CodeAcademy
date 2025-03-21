# Lesson Parametrization and fixtures in pytest                      date: 17/03/2025

#Exercise Redo the second lesson’s exercises with parametrization (is_prime / make_chocolate)

import pytest


def is_prime(num: int) -> bool:
    """Checks if a number is prime (greater than 1 and only divisible by 1 and itself)."""
    if not isinstance(num, int):
        raise TypeError("Input must be an integer")

    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True


@pytest.mark.parametrize("input_text, expected_output", [
    (-1, False),
    (-10, False),
    (0, False),
    (1, False),
    (4, False),
    (6, False),
    (9, False),
    (1001, False),
    (962, False),
])
def test_is_prime_is_false(input_text,expected_output):
    assert is_prime(input_text) == expected_output

@pytest.mark.parametrize("input_text, expected_output", [
    (2, True),
    (11, True),
    (7, True),
    (7919, True),
    (104729, True),
    (953, True),
])
def test_is_prime_is_true(input_text,expected_output):
    assert is_prime(input_text) == expected_output

@pytest.mark.parametrize("bad_input", [
    19.5,
    "23"
])
def test_is_prime_type_err(bad_input):
    with pytest.raises(TypeError):
        assert is_prime(bad_input)


def make_chocolate(small: int, big: int, goal: int) -> int:
    max_big_use = min(big, goal // 5)
    remainder = goal - (max_big_use * 5)
    if remainder <= small:
        return remainder
    return -1

@pytest.mark.parametrize("small, big, goal, remainder", [
    (5, 2, 15, 5),
    (3, 1, 10, -1),
    (3, 10, 28, 3),
    (0, 3, 15, 0),
    (10, 1, 3, 3),
    (0, 3, 14, -1),
    (0, 0, 0, 0)
])
def test_make_chocolate(small, big, goal, remainder):
    assert make_chocolate(small, big, goal) == remainder

