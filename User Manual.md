# Word Guessing Game User Manual

Welcome to the Word Guessing Game! This user manual provides detailed instructions on how to play the game and make the most of its features.

## Table of Contents

1. Game Overview
2. Installation
3. Starting the Game
4. Game Modes and Difficulty Levels
5. Gameplay Instructions
6. Using Hints
7. Ending the Game
8. Contributing and Feedback

## 1. Game Overview

The Word Guessing Game is an interactive command-line game where players attempt to guess a target word using the hill climbing optimization technique. The game provides different difficulty levels and limited attempts to make the gameplay challenging and engaging.

## 2. Installation

To install and run the Word Guessing Game, follow these steps:

1. Clone the repository from GitHub:
   ```
   git clone https://github.com/paiker-hussain/guess.git
   ```

2. Install the required dependencies:
   ```
   pip install nltk
   ```

## 3. Starting the Game

To start the game, navigate to the project directory and run the following command:
```
python Guess-game.py
```

## 4. Game Modes and Difficulty Levels

The Word Guessing Game offers four difficulty levels, each with different word lengths and limited attempts:

- **Easy**: Words with 3-5 letters, 10 attempts.
- **Medium**: Words with 6-8 letters, 8 attempts.
- **Hard**: Words with 8-11 letters, 8 attempts.
- **Extreme**: Words with 12-15 letters, 10 attempts.

## 5. Gameplay Instructions

Once you start the game, follow these instructions to play:

1. The game will display the number of blank spaces representing the letters in the target word.

2. Enter your guess for the word by typing it in the prompt box.

3. If any letters in your guess match the target word, they will be filled in the appropriate positions.

4. Continue guessing the word by providing your input until you either guess the correct word or run out of attempts.

5. The game will provide feedback after each guess, indicating if any letters match and their positions.

6. Use your logical thinking and the feedback from the game to narrow down the possibilities and guess the correct word.

## 6. Using Hints

Hints are available to assist you in guessing the word. The number of hints allowed depends on the difficulty level:

- **Easy** and **Medium** modes: 3 hints available.
- **Hard** mode: 2 hints available.
- **Extreme** mode: 1 hint available.

To use a hint, simply type "hint" in the prompt box. The game will provide you with a single randomly selected letter from the target word.

Use hints strategically to make progress in the game, but keep in mind the limited number of hints available.

## 7. Ending the Game

The game will end in one of the following scenarios:

- **Success**: If you correctly guess the target word within the allotted attempts, you win the game!

- **Failure**: If you run out of attempts without guessing the correct word, you lose the game. The target word will be revealed to you.

After the game ends, you can choose to play again or exit the game.

## 8. Contributing and Feedback

Contributions to the Word Guessing Game are welcome! If you have any feedback, bug reports, or suggestions for improvement, please follow the guidelines in the [CONTRIBUTING.md](./CONTRIBUTING.md) file.

We appreciate your support and hope you enjoy playing the Word Guessing Game!

For any inquiries

 or assistance, please contact the project lead, Syed Paiker Hussain Bukhari, or other team members Faseeh ud Din and Munib Ahsan Khan.

Email: [f2020266499@umt.edu.pk](mailto:f2020266499@umt.edu.pk)

---

Please note that this user manual provides a comprehensive guide on playing the game. If you have any further questions or need additional assistance, feel free to reach out to the project lead or consult the game's documentation.

Happy guessing!
