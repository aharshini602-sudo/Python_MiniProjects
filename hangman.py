import random

print("================================")
print("HANGMAN GAME")
print("================================")

name = input("Enter your name: ")

print("\nHello", name, "!")
print("Let's start the game.")
print("You have 6 chances.\n")

words = ["python", "computer", "developer", "programming", "keyboard"]

secret_word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_guesses = 6

while wrong_guesses < max_guesses:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter
        else:
            display_word += "_"

    print("Word:", display_word)
    print("Chances left:", max_guesses - wrong_guesses)

    if "_" not in display_word:
        print("\nCongratulations", name, "!")
        print("You guessed the word:", secret_word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in secret_word:
        print("Correct guess!\n")
    else:
        wrong_guesses += 1
        print("Wrong guess!\n")

else:
    print("\nGame Over,", name)
    print("The word was:", secret_word)

print("\nThanks for playing!")