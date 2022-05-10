from english_dictionary.scripts.read_pickle import get_dict
import random
words_dict = get_dict()


words = {}

for word in words_dict:
    if word.islower():
        words.update({word: len(word)})


choices = []
for word in words:
    if words[word] == 4:
        choices.append(word)

print(random.choice(choices))
