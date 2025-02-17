import config
import socket
import time
import itertools
import nltk
import random
from nltk.corpus import words


def con_to():
    # Connect to Twitch IRC
    sock = socket.socket()
    sock.connect((config.SERVER, config.PORT))
    sock.send(f"PASS {config.TOKEN}\n".encode("utf-8"))
    sock.send(f"NICK {config.NICKNAME}\n".encode("utf-8"))
    sock.send(f"JOIN {config.CHANNEL}\n".encode("utf-8"))
    time.sleep(1)  # Give it a second to connect
    return sock


# Send a message
def send_message(message):
    sock = con_to()
    message = f"PRIVMSG {config.CHANNEL} :{message}\n"
    sock.send(message.encode("utf-8"))


def find_words(letters, length):
    # Define the letters, valid words list, and words to exclude
    exclude_words = {"tort", "taro", "tarr"}  # Words to exclude

    # Count occurrences of each letter in the given set
    letter_counts = {char: letters.count(char) for char in set(letters)}

    # Generate all possible 6-letter combinations
    possible_words = (''.join(p) for p in itertools.permutations(letters, length))  # Use permutations to avoid repeats

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
    random_words = random.sample(valid_words, min(12, len(valid_words)))
    return random_words



kill = 0
while True:
    try:
        word_list = set(words.words())
        # Example: 6-letter words using only 'x', 'o', and 'r'
        found_words = find_words("crottra", 4)
        # limits returned words by X amount.
        limited_words = list(itertools.islice(found_words, 8))
        for f in limited_words:
            print(f)
            # send_message(f)
            # time.sleep(3)
        # send_message("we playing")  # Example message
        break

    except (NameError, LookupError):
        # Ensure you have the word list downloaded
        nltk.download("words")
        word_list = set(words.words())  # Load words from nltk
        if kill == 1:
            print("Error downloading word list.")
            break
        else:
            kill = 1
