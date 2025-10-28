import random
from data.words import words


def choose_secret_word(words: list[str]) -> str:
    return random.choice(words)





# def choose_secret_word(words: list[str]) -> str:
#     len_word = len(words)-1
#     wo = randint(0,len_word)
#     word = words[wo]
#     return word




