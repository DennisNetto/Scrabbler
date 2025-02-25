import itertools
import nltk
import random
import subprocess
import platform
from os import system, name

from nltk.corpus import words

# Uses the operating system to define the method of clearing the shell.
def clear():
    operatingsys = platform.system()
    if operatingsys == "Windows":
        if name == 'nt':
            _ = system('cls')

    else:
        subprocess.run("clear", shell=True)


def find_words(letter, lengths, number):
    # Define the letters, valid words list, and words to exclude
    exclude_words = {}  # Words to exclude

    # Count occurrences of each letter in the given set
    letter_counts = {char: letter.count(char) for char in set(letter)}

    # Generate all possible 6-letter combinations
    possible_words = (''.join(p) for p in itertools.permutations(letter, lengths))  # Use permutations to avoid repeats

    # Function to check if word follows letter constraints
    def is_valid(word):
        # Ensure it's in the valid word list
        if word not in word_list:
            return False
        # Ensure it's not in the exclude list
        if word in exclude_words:
            return False
        # Ensure it does not contain more of any letter than allowed
        word_counts = {char: word.count(char) for char in set(word)}
        return all(word_counts[char] <= letter_counts.get(char, 0) for char in word_counts)


    # Filter valid words
    valid_words = [word for word in possible_words if is_valid(word)]

    # Randomly select X words (only if there are enough valid words)
    random_words = random.sample(valid_words, min(number, len(valid_words)))
    return random_words



kill = 0
while True:
    try:
        print("enter the letters you have (no spaces)")
        letters = str(input())
        clear()
        print("enter the length of the word")
        length = int(input())
        clear()
        print("enter the number of results you want")
        num_results = int(input())
        clear()
        word_list = set(words.words())
        # Example: box:1 is letters, two is length, and three is number of returned words.
        found_words = find_words(letters, length, num_results)
        # limits returned words by X amount.
        print("Results:")
        for f in found_words:
            print(f)
            # send_message(f, sock)
            # time.sleep(15)
        break

    except (NameError, LookupError, ValueError):
        # Ensure you have the word list downloaded
        nltk.download("words")
        word_list = set(words.words())  # Load words from nltk
        if kill == 1:
            print("Error downloading word list.")
            break
        else:
            kill = 1
