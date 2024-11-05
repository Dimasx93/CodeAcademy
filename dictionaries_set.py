# #Exercise n1
#
# user_info = {
#     "name": input("Enter your name: "),
#     "surname": input("Enter your surname: "),
#     "age": int(input("Enter your age: ")),
# }
# print(user_info)
import string

#Exercise n2

# is_true = True
# my_set = set()
# while is_true:
#     name = input("Enter a student's name (or type 'done' to finish): ").title()
#     if name == "Done":
#         is_true = False
#     else:
#         my_set.add(name)
# print(my_set)

# #Exercise n3
#
# dictionary = {
#     "apple": "a fruit that grows on trees",
#     "book": "a set of printed pages, bound together, containing text or pictures",
#     "computer": "an electronic device for storing and processing data",
# }
#
# while True:
#     words = input("Enter a word to look up its meaning (or 'done' to finish): ")
#     if words == "done":
#         break
#     if words in dictionary:
#         print(f"The meaning of {words} is: {dictionary[words]}")
#     else:
#         print("This word is not in our dictionary.")

# #Exercise n4
#
# phone_book = {}
#
# while True:
#     ask_input = input("Would you like to Add, Search, Delete a contact or Exit? ").title()
#     if ask_input == "Exit":
#         break
#     if ask_input == "Add":
#         name = input("Write the name: ")
#         phone_number = input("Write the phone number: ")
#         phone_book[name] = phone_number
#         print(f"{name} has been added.")
#     elif ask_input == "Search":
#         ask_contact = input("Write the name you want to search: ")
#         if ask_contact in phone_book:
#             print(f"This person {ask_contact} is in the phone book.")
#         else:
#             print(f"This person {ask_contact} is not in the phone book.")
#     elif ask_input == "Delete":
#         ask_delete = input("Who would you like to delete? ")
#         if ask_delete in phone_book:
#             del phone_book[ask_delete]
#             print(f"{ask_delete} has been deleted.")
#         else:
#             print("Person was not found")
#     elif ask_input == "Exit":
#         break
#     else:
#         print("Wrong input")
# print(phone_book)

# #Exercise n5
#
# students_db = {}
# while True:
#     ask_name = input("Enter student name (or type 'done' to finish): ")
#     if ask_name == "done":
#         break
#     ask_grade = int(input("Enter grade: "))
#     students_db[ask_name] = ask_grade
#     average = sum(students_db.values()) / len(students_db) if len(students_db) > 0 else 0
#     print(f"Average grade of all students: {average:.2f}")
#     if students_db[ask_name] < 80:
#         del students_db[ask_name]
#         continue
#
# while True:
#     student_to_check = input("Enter a student name to check (or type 'done' to finish): ")
#     if student_to_check.lower() == "done":
#         break
#     if student_to_check in students_db:
#         print(f"{student_to_check} found. Grade: {students_db[student_to_check]}")
#     else:
#         print(f"{student_to_check} not found.")

# #Exercise n6
#
# import string
#
# # Function to normalize text
# def normalize_text(text):
#     # Handle apostrophes specifically for contractions and possessives
#     text = text.replace("'", " ")
#     # Remove all other punctuation
#     translator = str.maketrans("", "", string.punctuation)
#     return text.translate(translator).lower()
#
# # Main program
# text = input("Enter a block of text: ")
#
# # Check if the input is not just whitespace
# if not text.strip():
#     print("No text provided. Please enter some text.")
# else:
#     # Normalize text
#     normalized_text = normalize_text(text)
#
#     # Split text into words
#     words = normalized_text.split()
#     word_count = {}
#
#     # Count frequencies of each word
#     for word in words:
#         if word in word_count:
#             word_count[word] += 1
#         else:
#             word_count[word] = 1
#
#     # Sort the dictionary by frequency
#     sorted_word_count = sorted(
#         word_count.items(), key=lambda item: item[1], reverse=True
#     )
#
#     print("Word frequencies:")
#     for word, count in sorted_word_count:
#         print(f"{word}: {count}")