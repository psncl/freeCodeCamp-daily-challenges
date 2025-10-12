from enum import Enum

class Outcomes(str, Enum):
    VICTORY = "We win"
    DEFEAT = "We lose"
    DRAW = "Draw"

def battle(our_team: str, opponent: str) -> str:

    our_wins = opponent_wins = 0
    our_words = our_team.split(" ")
    opponent_words = opponent.split(" ")

    for i in range(len(our_words)):
        comparison = compare_words(our_words[i], opponent_words[i])
        if comparison > 0:
            our_wins += 1
        elif comparison < 0:
            opponent_wins += 1

    if our_wins > opponent_wins:
        return Outcomes.VICTORY.value
    elif our_wins < opponent_wins:
        return Outcomes.DEFEAT.value
    else:
        return Outcomes.DRAW.value

def get_letter_value(letter: str) -> int:
    """
    Return the corresponding value of a single
    uppercase or lowercase alphabet letter
    """

    initial_offset =  ord('a') if letter.islower() else ord('A')
    value = ord(letter) - initial_offset + 1
    return value if letter.islower() else (value * 2)

def get_word_value(word: str) -> int:
    return sum([get_letter_value(ch) for ch in word])

def compare_words(first: str, second: str) -> int:
    return get_word_value(first) - get_word_value(second)

## Tests

assert battle("hello world", "hello word") == "We win"
assert battle("Hello world", "hello world") == "We win"
assert battle("lorem ipsum", "kitty ipsum") == "We lose"
assert battle("hello world", "world hello") == "Draw"
assert battle("git checkout", "git switch") == "We win"
assert battle("Cheeseburger with fries", "Cheeseburger with Fries") == "We lose"
assert battle("We must never surrender", "Our team must win") == "Draw"