import config
import socket
import time
import itertools
import nltk
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
    exclude_words = {"that", "then", "thee", "than"}
    possible_words = (''.join(p) for p in itertools.product(letters, repeat=length))
    return [word for word in possible_words if word in word_list and word not in exclude_words]



kill = 0
while True:
    try:
        word_list = set(words.words())
        # Example: 6-letter words using only 'x', 'o', and 'r'
        found_words = find_words("thean", 4)
        # limits returned words by X ammount.
        limited_words = list(itertools.islice(found_words, 3))
        print(limited_words)
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
