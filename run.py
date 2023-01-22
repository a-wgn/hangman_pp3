"""
Import libraries to this application to run the game.
"""
import random
from words import words


def get_a_word(words):
    """
    Randomly choose a word from the list.
    Keeps iterating back and forth until it is not true anymore.
    Returns a word that those not have a word with dash or space
    """
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word


def hangman():
    word = get_a_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

user_input = input('Type something')
print(user_input)
