#Lesson n10 Data Structures: Specials methods
#
# #Exercise n1 Numbers Divisible by 6
#
# divide_six = [number for number in range(1,1001) if number % 6 == 0]
# print("Numbers divisible by 6 from 1 to 1000:", divide_six)
#
# #Exercise n2 Find Numbers Containing Nine
#
# numbers_with_nine = [number for number in range(1,1001) if "9" in str(number)]
# print("Numbers containing 9 from 1 to 1000:", numbers_with_nine)
#
# #Exercise n3 Count Words with “e”
#
# text = input("Please enter your text: ")
# count_e = {"e" : text.count("e")}
# print(count_e)
#
# #Exercise n4 Count Words Longer Than Five Characters
#
# text = input("Please enter your text: ")
# long_words = len([word for word in text.split() if len(word) > 5])
# print("Number of words longer than five characters:", long_words)
#
# #Exercise n5 Letter Frequency Dictionary
# from collections import Counter
#
# text = input("Please enter your text: ")
#
# count_letters2 = {i: text.lower().count(i) for i in text.lower() if i.isalpha()}
# count_letters = Counter(list(text))
#
# print("Letter frequencies:", count_letters2)
#
# #Exercise n6 Perfect Square Checker
# import math
#
# def is_perfect_square(num):
#     root = math.sqrt(num)
#     return root * root == num
#
# num = int(input("Enter an integer: "))
# result = is_perfect_square(num)
# print(f"Is {num} a perfect square? {result}")