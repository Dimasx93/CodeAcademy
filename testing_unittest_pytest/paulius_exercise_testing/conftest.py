import pytest

@pytest.fixture
def lorem_ipsum():
    with open("file1.txt", "r") as file:
        content = file.read()
    return content

@pytest.fixture
def random_text():
    with open("file2.txt", "r") as file:
        content = file.read()
    return content