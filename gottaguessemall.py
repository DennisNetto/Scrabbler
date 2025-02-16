import config
import socket
import time
import itertools
import nltk
from nltk.corpus import words

# Ensure you have the word list downloaded
nltk.download("words")
word_list = set(words.words())  # Load words from nltk

# Connect to Twitch IRC
sock = socket.socket()
sock.connect((config.SERVER, config.PORT))
sock.send(f"PASS {config.TOKEN}\n".encode("utf-8"))
sock.send(f"NICK {config.NICKNAME}\n".encode("utf-8"))
sock.send(f"JOIN {config.CHANNEL}\n".encode("utf-8"))
time.sleep(1)  # Give it a second to connect

def find_words(letters, length):
    possible_words = (''.join(p) for p in itertools.product(letters, repeat=length))
    return [word for word in possible_words if word in word_list]

# Example: 6-letter words using only 'x', 'o', and 'r'
print(find_words("thean", 4))

# Send a message
def send_message(message):
    for f in message:
        message = f"PRIVMSG {config.CHANNEL} :{f}\n"
        sock.send(message.encode("utf-8"))
        send_message("Hello, Twitch Chat!")  # Example message
        time.sleep(1)

