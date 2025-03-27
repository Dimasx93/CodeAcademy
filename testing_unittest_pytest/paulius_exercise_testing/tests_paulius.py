from paulius_exercise_mocking_fixtures import count_word_occurrences
from unittest.mock import patch

import pytest

@patch("paulius_exercise_mocking_fixtures.open")
def test_count_word_occurrences(mock_write):
    random_text = "hello beautiful boah"
    mock_write.return_value.read.return_value = random_text

    res = count_word_occurrences("text.txt", "hello")
    assert res == 1


def test_count_word_occurrences_two(lorem_ipsum):
    with patch("paulius_exercise_mocking_fixtures.open") as mock_write:
        mock_write.return_value.read.return_value = lorem_ipsum
        res = count_word_occurrences("file1.txt", "Lorem")
    assert res == 2

def test_count_word_occurrences_three(random_text):
    with patch("paulius_exercise_mocking_fixtures.open") as mock_write:
        mock_write.return_value.read.return_value = random_text
        res = count_word_occurrences("file2.txt", "Welcome")
    assert res == 3