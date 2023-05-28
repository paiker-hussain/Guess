from game import Game

def test_initial_blank_word():
    game = Game("word")
    assert game.current_word == "____"

def test_multiple_correct_guesses():
    game = Game("intensity")
    assert game.make_guess("i") == "i_______"

def test_exhaust_attempts():
    game = Game("word")
    game.make_guess("a")
    assert game.make_guess("a") == "____"

def test_successful_guess():
    game = Game("python")
    assert game.make_guess("p") == "p____"
    assert game.make_guess("y") == "py___"
    assert game.make_guess("t") == "pyt__"
    assert game.make_guess("h") == "pyth_"
    assert game.make_guess("o") == "pytho"
    assert game.make_guess("n") == "python"
    assert game.make_guess("x") == "Congratulations! You guessed the word correctly."

def test_hint():
    game = Game("example")
    hint = game.get_hint()
    assert len(hint) == 35
    assert hint.startswith("The hint is ")
    assert hint.endswith(".")
    assert hint[12] == "'"
    assert hint[15] == "'"
    assert hint[19] == "'"
    assert hint[22] == "'"
