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
    possible_words = (''.join(p) for p in itertools.product(letters, repeat=length))
    return [word for word in possible_words if word in word_list]

kill = 0
while True:
    try:
        # Example: 6-letter words using only 'x', 'o', and 'r'
        print(find_words("thean", 4))
        # send_message("we playing")  # Example message
        break

    except NameError:
        # Ensure you have the word list downloaded
        nltk.download("words")
        word_list = set(words.words())  # Load words from nltk
        if kill == 1:
            break
        else:
            kill = 1
