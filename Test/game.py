import random

class Game:
    def __init__(self, word):
        self.word = word.lower()
        self.current_word = "_" * len(self.word)
        self.guesses = []
        self.attempts = 0

    def make_guess(self, letter):
        if letter in self.guesses:
            return self.current_word

        self.guesses.append(letter)

        if letter in self.word:
            self.update_current_word(letter)

        if self.attempts >= 10:
            return "Game over! You have used all your attempts."

        if self.current_word == self.word:
            return "Congratulations! You guessed the word correctly."

        self.attempts += 1
        return self.current_word

    def update_current_word(self, letter):
        new_word = ""
        for i in range(len(self.word)):
            if self.word[i] == letter:
                new_word += letter
            else:
                new_word += self.current_word[i]
        self.current_word = new_word

    def get_hint(self):
        if len(self.guesses) >= 10:
            return "No more hints available. Keep guessing!"
        else:
            while True:
                hint_index = random.randint(0, len(self.word) - 1)
                if self.current_word[hint_index] == "_":
                    return f"The hint is '{self.word[hint_index]}' at index {hint_index+1}."
