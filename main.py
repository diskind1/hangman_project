from hangman.game import init_state, is_won, validate_guess, apply_guess, is_lost, render_display, render_summary
from hangman.words import choose_secret_word
from hangman.io import print_status, prompt_guess

MAX_TRIES = 6

def play(words: list[str], max_tries: int = MAX_TRIES) -> None:
    secret_word = choose_secret_word(words)
    state = init_state(secret_word,max_tries)
    print("ברוך הבא למשחק")

    while not is_won(state) and not is_won(state):
        print_status(state)
        




