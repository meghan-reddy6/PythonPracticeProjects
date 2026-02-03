import random

# Hangman ASCII art stages (index = attempts left)
HANGMAN_PICS = [
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """
]

print("🎉 Welcome to Hangman! 🎉")

words = ['python', 'hangman', 'challenge', 'programming', 'developer']
word_to_guess = random.choice(words)

guessed_letters = set()
max_attempts = 6
attempts_left = max_attempts
display_word = ['_'] * len(word_to_guess)

def display_current_state():
    print(HANGMAN_PICS[attempts_left])
    print("Current word: " + ' '.join(display_word))
    print(f"Attempts left: {attempts_left}")
    print("Guessed letters: " + ' '.join(sorted(guessed_letters)))
    print("-" * 30)

while attempts_left > 0 and '_' in display_word:
    display_current_state()
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter a single alphabetical character.")
        continue

    if guess in guessed_letters:
        print("⚠️ You have already guessed that letter. Try again.")
        continue

    guessed_letters.add(guess)

    if guess in word_to_guess:
        print(f"✅ Good job! '{guess}' is in the word.")
        for index, letter in enumerate(word_to_guess):
            if letter == guess:
                display_word[index] = guess
    else:
        attempts_left -= 1
        print(f"❌ Sorry, '{guess}' is not in the word.")

# Game result
if '_' not in display_word:
    print("\n🎉 Congratulations! You've guessed the word:", word_to_guess)
else:
    print(HANGMAN_PICS[0])
    print("\n💀 Game over! The word was:", word_to_guess)
