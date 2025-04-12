import random

def hangman():
    # List of words to choose from
    words = ['python', 'javascript', 'developer', 'hangman', 'coding', 'internet']

    # Pick a random word
    word = random.choice(words)
    word_letters = set(word)  # Unique letters in the word
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    used_letters = set()  # What the player has guessed

    lives = 6

    print("Welcome to Hangman!")

    # Game loop
    while len(word_letters) > 0 and lives > 0:
        # Show used letters
        print("You have", lives, "lives left. You have used these letters: ", ' '.join(used_letters))

        # Display current word status
        word_display = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", ' '.join(word_display))

        # Take user input
        user_letter = input("Guess a letter: ").lower()

        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Good job!")
            else:
                lives -= 1
                print("Wrong guess.")
        elif user_letter in used_letters:
            print("You have already used that letter. Try again.")
        else:
            print("Invalid character. Please guess a letter.")

    # Game over conditions
    if lives == 0:
        print("You died! The word was", word)
    else:
        print("Congratulations! You guessed the word:", word)

# Start the game
hangman()
