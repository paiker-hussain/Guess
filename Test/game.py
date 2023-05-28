class Game:
    def __init__(self, word):
        self.word = word
        self.current_word = "_" * len(word)
        self.guesses = []

    def get_current_word(self):
        return self.current_word

    def make_guess(self, letter):
    if letter in self.guesses:
        return self.current_word

    self.guesses.append(letter)

    if letter in self.word:
        self.update_current_word(letter)

    if len(self.guesses) >= 10:
        return "Game over! You have used all your attempts."

    if self.current_word == self.word:
        return "Congratulations! You guessed the word correctly."

    return self.current_word


    def update_current_word(self, letter):
    updated_word = ""
    for i in range(len(self.word)):
        if self.word[i] == letter or self.current_word[i] != "_":
            updated_word += self.word[i]
        else:
            updated_word += self.current_word[i]
    self.current_word = updated_word

