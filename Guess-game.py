import random
import re
import nltk
nltk.downnload('words')
from nltk.corpus import words

# Word Guessing Game with Hill Climbing

def initialize_game(difficulty):
    word_list = words.words()
    if difficulty == "easy":
        min_length = 3
        max_length = 5
        max_attempts = 10
        max_hints = 3
    elif difficulty == "medium":
        min_length = 6
        max_length = 8
        max_attempts = 8
        max_hints = 3
    elif difficulty == "hard":
        min_length = 8
        max_length = 11
        max_attempts = 8
        max_hints = 2
    elif difficulty == "extreme":
        min_length = 12
        max_length = 15
        max_attempts = 10
        max_hints = 1
    else:
        print("Invalid difficulty level. Setting difficulty to easy.")
        min_length = 3
        max_length = 5
        max_attempts = 10
        max_hints = 3

    filtered_words = [word for word in word_list if min_length <= len(word) <= max_length]
    target_word = random.choice(filtered_words)
    guessed_word = ["_"] * len(target_word)
    return target_word, guessed_word, max_attempts, max_hints

def evaluate_guess(guess, target_word, guessed_word):
    if guess == target_word:
        return "Correct"

    for index, letter in enumerate(target_word):
        if letter == guess[index]:
            guessed_word[index] = letter

    return guessed_word

def take_hint(target_word, guessed_word):
    hint_index = random.randint(0, len(target_word) - 1)
    while guessed_word[hint_index] != "_":
        hint_index = random.randint(0, len(target_word) - 1)
    return hint_index

def play_game():
    print("Welcome to the Word Guessing Game!")
    print("Guess the word by providing your own words.")

    difficulty = input("Select difficulty level (easy, medium, hard, extreme): ").lower()

    target_word, guessed_word, max_attempts, max_hints = initialize_game(difficulty)
    attempts = 0
    hints_taken = 0

    print("Number of letters in the word:", len(target_word))
    print("You have", max_attempts, "guesses.")
    print("You can take up to", max_hints, "hint(s) during the game.")

    while attempts < max_attempts:
        print("Attempt:", attempts + 1)
        print("Current word:", " ".join(guessed_word))
        guess = input("Enter your guess: ").lower()

        if guess == "hint" and hints_taken < max_hints:
            hints_taken += 1
            hint_index = take_hint(target_word, guessed_word)
            guessed_word[hint_index] = target_word[hint_index]
            continue

        result = evaluate_guess(guess, target_word, guessed_word)

        if result == "Correct":
            print("Congratulations! You guessed the word correctly.")
            break
        elif isinstance(result, list):
            guessed_word = result
            attempts += 1
            if attempts == max_attempts:
                print("Game over! You couldn't guess the word. The target word was:", target_word)
            else:
                print("Incorrect guess. Try again.")
        else:
            print("Invalid guess. Please enter a valid word.")

play_game()
