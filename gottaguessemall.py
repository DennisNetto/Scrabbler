import config

import itertools
import nltk
from nltk.corpus import words

# Ensure you have the word list downloaded
nltk.download("words")
word_list = set(words.words())  # Load words from nltk

def find_words(letters, length):
    possible_words = (''.join(p) for p in itertools.product(letters, repeat=length))
    return [word for word in possible_words if word in word_list]

# Example: 6-letter words using only 'x', 'o', and 'r'
print(find_words("thean", 4))

