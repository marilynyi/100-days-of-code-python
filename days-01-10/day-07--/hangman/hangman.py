import random
from word_list import word_list
from art import stages, logo
import os
  
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

print(logo)

#print(f"Debug: The chosen word is {chosen_word}")

lives = 6
stage = stages[lives]

display = []
for blank in range(word_length):
    display += "_"

print("\nThe word is: ", end = "")
print(" ".join(display))

end_of_game = False
while not end_of_game:

    guess = input("\nGuess a letter: ").lower()

    os.system("cls")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(" ".join(display))
    # or print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win!")

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose!")
            print("The word is: " + chosen_word)

    stage = stages[lives]
    print(stage)
    print("-----------------------------------------")
