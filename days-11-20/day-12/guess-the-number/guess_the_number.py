import random
from art import logo
import sys

#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

def main():
    # Greet user with a welcome message
    print(logo)
    print("Welcome to the Number Guessing Game!")

    # User chooses difficulty
    while True:
        try:
            select_difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower().strip()
            if select_difficulty == "easy":
                guesses = 10
                break
            elif select_difficulty == "hard":
                guesses = 5
                break
            else:
                raise ValueError
        except ValueError:
            pass

    # Randomize number to guess
    print("I'm thinking of a number between 1 and 100.")
    correct_answer = random.randint(1,100)

    # Loop until user runs out of guesses
    while guesses >= 0:
        print(f"You have {guesses} attempts to guess the number.")

        # User enters a number
        guess = int(input("Make a guess: "))

        # Break out of loop if guess is correct
        if guess == correct_answer:
            print(f"You got it! The answer was {correct_answer}.")
            sys.exit()
        elif guess < correct_answer:
            print("Too low.")
        elif guess > correct_answer:
            print("Too high.")
        else:
            print("Invalid input.")
        
        # Remove one from guess count if number is incorrect
        guesses -= 1

        # Break loop if user runs out of attempts
        if guesses == 0:
            sys.exit("You've run out of guesses, you lose.")
        else:
            print("Guess again.")


if __name__ == "__main__":
    main()
