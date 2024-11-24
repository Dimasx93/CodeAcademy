# Lesson n14 Virtual Environment
#
#Exercise n1 Random Words

from random_word import RandomWords

for x in range(5):
    a = RandomWords()
    random_words = [a.get_random_word().upper()]
    sorted_words = sorted(random_words)
    for word in sorted_words:
        print(word)
#Exercise n2 External Package was completed in Lesson n12 exercises, Modules packages and imports.