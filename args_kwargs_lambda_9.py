#Lesson n9 *args **kwargs and lambda
from unittest import removeResult


# #Exercise n1 Puzzle Pieces
#
# def puzzle_pieces(a,b):
#     if len(a) != len(b):
#         return False
#     sums = []
#     for i in range(len(a)):
#         sums.append(a[i] + b[i])
#     if len(set(sums)) == 1:
#         return True
#     else:
#         return False
#
# print(puzzle_pieces([2, 9, 6, 1, 0, 8], [0, -7, -4, 1, 2, -6]))

# #Exercise n2 Repeat String
#
# repeat_string = lambda text, n: text * n
# print(repeat_string("Hello", 3))

# #Exercise n3 War of Numbers
#
# def war_of_number(a):
#     even_num = []
#     odds_num = []
#     for i in (a):
#         if i % 2 == 0:
#             even_num.append(i)
#         else:
#             odds_num.append(i)
#     even_sum = sum(even_num)
#     odds_sum = sum(odds_num)
#     if even_sum >= odds_sum:
#         return even_sum - odds_sum
#     else:
#         return odds_sum - even_sum
#
# def war_of_numbers(lst):
#     even_sum = sum(x for x in lst if x % 2 == 0)
#     odd_sum = sum(x for x in lst if x % 2 != 0)
#     return abs(even_sum - odd_sum)
#
# print(war_of_numbers([12, 90, 75]))

# #Exercise n4 Can Find Bigrams
#
# def can_find(bigrams, words):
#      return all(any(bigram in word for word in words) for bigram in bigrams)
# print(can_find(["at", "be", "th", "au"], ["beautiful", "the", "hat"]))

# #Exercise n5 Strings Starting with Vowels
#
# def start_with_vowel(words):
#     vowel_starting_words = [word for word in words if word.lower().startswith(('a', 'e', 'i', 'o', 'u'))]
#     return vowel_starting_words
#
# def start_with_vowel(strings):
#     return list(filter(lambda word: word[0].lower() in "aeiou", strings))
#
# print(start_with_vowel(["apple", "banana", "orange"]))