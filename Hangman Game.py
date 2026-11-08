import random

# Words for the game
words = ["python", "computer", "college", "student", "coding"]

# Select a random word
word = random.choice(words)

guessed_letters = []
wrong_guesses = 0
max_guesses = 6

print("Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while wrong_guesses < max_guesses:

    # Show the current word
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Wrong guesses:", wrong_guesses, "/", max_guesses)

    # Check if the word is completed
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter only one alphabet.")
        continue

    if guess in guessed_letters:
        print("You already guessed this letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        print("Wrong guess!")
        wrong_guesses += 1

if wrong_guesses == max_guesses:
    print("\nGame Over!")
    print("The correct word was:", word)

print("\nThanks for playing!")