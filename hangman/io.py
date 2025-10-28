from game import apply_guess
from hangman.game import render_display, is_won, is_lost


def prompt_guess() -> str:
    guess = input("בחר אות אחת בעברית: ")
    return guess

def print_status(state: dict) -> None:
    display_word = render_display(state)
    guessed_letters = state["guessed"]
    tries_left = state["max_tries"] - state["wrong_guesses"]

    print("=" * 30)
    print(f" המצב הנוכחי: {display_word}")
    print(f"מצב הניחושים: {tries_left} מתוך {state["max_tries"]}")
    print(f"האותיות שניחשת עד עכשיו: {' '.join(guessed_letters)}")
    print("=" * 30)


def print_result(state: dict) -> None:
    if is_won(state):
        print("מדהים, הצלחת!")
    if is_lost(state):
        print("נסיון נחמד, לא עבד הפעם:)")
