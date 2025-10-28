from hangman.game import init_state, is_won, validate_guess, apply_guess, is_lost, render_display, render_summary
from hangman.words import choose_secret_word
from hangman.io import print_status, prompt_guess, print_result
from data.words import words




MAX_TRIES = 6

def play(words: list[str], max_tries: int = MAX_TRIES) -> None:
    secret_word = choose_secret_word(words)
    state = init_state(secret_word,max_tries)
    print("ברוך הבא למשחק")

    while not is_won(state) and not is_lost(state):
        print_status(state)
        render_display(state)
        p = prompt_guess()
        print(validate_guess(p,state["guessed"]))
        apply_guess(state,p)

    print_result(state)
    print(render_summary(state))

if __name__ == "__main__":
    play(words,MAX_TRIES)

