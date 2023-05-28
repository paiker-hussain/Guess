import random
import re
import pytest
from nltk.corpus import words
from guess_game import initialize_game, evaluate_guess, take_hint

# Ensure nltk words are downloaded
words.ensure_loaded()

@pytest.mark.parametrize("difficulty, expected_length", [
    ("easy", range(3, 6)),
    ("medium", range(6, 9)),
    ("hard", range(8, 12)),
    ("extreme", range(12, 16))
])
def test_initialize_game(difficulty, expected_length):
    target_word, guessed_word, max_attempts, max_hints = initialize_game(difficulty)
    assert len(target_word) in expected_length
    assert guessed_word == ["_"] * len(target_word)
    assert max_attempts in [8, 10]
    assert max_hints in [1, 2, 3]

def test_evaluate_guess():
    target_word = "python"
    guessed_word = ["_", "_", "_", "_", "_", "_"]
    assert evaluate_guess("p", target_word, guessed_word) == ["p", "_", "_", "_", "_", "_"]
    assert evaluate_guess("y", target_word, guessed_word) == ["_", "y", "_", "_", "_", "_"]
    assert evaluate_guess("o", target_word, guessed_word) == ["_", "_", "o", "_", "_", "_"]
    assert evaluate_guess("t", target_word, guessed_word) == ["_", "_", "_", "t", "_", "_"]
    assert evaluate_guess("h", target_word, guessed_word) == ["_", "_", "_", "_", "h", "_"]
    assert evaluate_guess("n", target_word, guessed_word) == ["_", "_", "_", "_", "_", "n"]
    assert evaluate_guess("x", target_word, guessed_word) == ["_", "_", "_", "_", "_", "_"]
    assert evaluate_guess("python", target_word, guessed_word) == "Correct"

def test_take_hint():
    target_word = "python"
    guessed_word = ["_", "_", "_", "_", "_", "_"]
    random.seed(42)  # Set seed for predictable randomness in the test
    hint_index = take_hint(target_word, guessed_word)
    assert guessed_word[hint_index] == "p"

# Add more test functions to cover other parts of your code

