from game import Game

def test_initial_blank_word():
    game = Game("word")
    assert game.get_current_word() == "____"

def test_correct_guess():
    game = Game("word")
    assert game.make_guess("w") == "w___"

def test_incorrect_guess():
    game = Game("word")
    assert game.make_guess("x") == "____"

def test_multiple_correct_guesses():
    game = Game("intensity")
    assert game.make_guess("i") == "i_______"
    assert game.make_guess("n") == "in______"
    assert game.make_guess("t") == "int_____"
    assert game.make_guess("e") == "inte____"
    assert game.make_guess("s") == "inten___"
    assert game.make_guess("i") == "inteni__"
    assert game.make_guess("t") == "intenit_"
    assert game.make_guess("y") == "intenity"

def test_exhaust_attempts():
    game = Game("word")
    assert game.make_guess("a") == "__"
    assert game.make_guess("b") == "__"
    assert game.make_guess("c") == "__"
    assert game.make_guess("d") == "__"
    assert game.make_guess("e") == "__"
    assert game.make_guess("f") == "__"
    assert game.make_guess("g") == "__"
    assert game.make_guess("h") == "__"
    assert game.make_guess("i") == "__"
    assert game.make_guess("j") == "Game over!"
