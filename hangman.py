import random

def choose_word():
    words = ["apple", "banana", "cherry", "durian", "elderberry", "fig", "grapefruit", "honeydew"]
    return random.choice(words)

def play_hangman():
    word = choose_word()
    word_letters = set(word)
    guessed_letters = set()
    attempts = 6

    while attempts > 0:
        # Display current state of the word with underscores for unknown letters
        display_word = ''.join([letter if letter in guessed_letters else '_' for letter in word])
        print("Word:", display_word)

        if display_word == word:
            print("Congratulations! You guessed the word:", word)
            return

        print("Attempts remaining:", attempts)
        guess = input("Enter a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word_letters:
            print("Good guess!")
            guessed_letters.add(guess)
        else:
            print("Wrong guess!")
            attempts -= 1

        print("")

    print("You ran out of attempts. The word was:", word)

play_hangman()
