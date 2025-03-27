# Exercise with mocking and fixtures

# You're working on a program that reads a file and counts how many times a word appears.
# Your task is to test it without actually creating a file by mocking the open() function.)

# Step 1: Implement the Function
#  Create a Python module(file_reader.py) with the following function

def count_word_occurrences(filename, word):
    """Reads a file and counts how many times a given word appears."""
    # with open(filename, "r") as file:
    #     content = file.read()
    file = open(filename, "r")
    content = file.read()

    return content.lower().split().count(word.lower())