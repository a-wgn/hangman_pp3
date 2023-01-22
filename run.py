"""
Import libraries to this application to run the game.
"""
import random
import string
from words import words


def welcome():
    """TEST"""
    print('Welcome to Hangman! You have 6 lives to guess a random word.\n')


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
    """
    User input to guess the word.
    Letters user already used in the game.
    Shows the current word that the user is currently guessing.
    Reduces one live from the 6 lives till the user has 0 lives.
    """
    word = get_a_word(words)
    word_letter = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()

    live = 6

    while len(word_letter) > 0 and live > 0:
        print(live, 'lives and used letters: ', ' '.join(used_letter))

        word_li = [letter if letter in used_letter else '-' for letter in word]
        print('Current word: ', ' '.join(word_li))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in word_letter:
                word_letter.remove(user_letter)

            else:
                live = live - 1
                print('Letter is not in the word!\n')

        elif user_letter in used_letter:
            print('You already guessed this letter. Try again your luck!\n')

        else:
            print('Invalid letter. Try again!\n')

    if live == 0:
        print('You have lost the game!\n')
    else:
        print('Congrats, you guessed the word!\n')


def main():
    """TEST"""
    welcome()
    hangman()


if __name__ == '__main__':
    main()
