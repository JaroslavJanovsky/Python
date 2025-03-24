import random

def play_game():
    # Generate a random letter
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    secret_letter = random.choice(alphabet)

    # Prompt the player for guesses
    print("Welcome to the Letter Guessing Game!")
    print("I've chosen a letter from the alphabet. Can you guess it?")
    
    while True:
        guess = input("Enter your guess (a single letter): ").lower()

        # Check if the guess is valid
        if len(guess) != 1 or guess not in alphabet:
            print("Please enter a valid single letter.")
            continue

        # Check if the guess is correct
        if guess == secret_letter:
            print("Congratulations! You guessed the letter {}!".format(secret_letter))
            break
        else:
            print("Incorrect guess. Try again!")

if __name__ == "__main__":
    play_game()
