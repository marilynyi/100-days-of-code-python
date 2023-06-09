import random
import os
from art import logo, vs
from game_data import data

os.system("clear")

def main():

    game_over = False
    score = 0
    person = person_info()

    print(logo)

    # Loop while answer is correct
    while not game_over:

        # Pick two people
        person1 = person
        person2 = person_info()

        # Pick a new second person if it is the same as the first
        while person1 == person2:
            person2 = person_info()

        # Compare two persons and ask user to select one
        user_input = compare_persons(person1, person2)
        
        # Clear terminal and print project header
        os.system("clear")
        print(logo)

        # Check if user answered correctly then return selected person and new score
        person, score = is_answer_correct(user_input, person1, person2, score)

        # If user answered incorrectly, terminate the program
        if person == 0:
            os.system("clear")
            print(logo)
            print(f"Sorry that is wrong. Final score: {score}") 
            game_over = True  


def is_answer_correct(user_input, person1, person2, score):
    """Check if player answered correctly then return selected person and new score"""
    if user_input == 1 and person1['follower_count'] > person2['follower_count']:
        score += 1
        print(f"You're right! Current score: {score}")
        person = person1
    elif user_input == 2 and person2['follower_count'] > person1['follower_count']:
        score += 1 
        print(f"You're right! Current score: {score}")
        person = person2
    else:
        person = 0
    return person, score 


def compare_persons(person1, person2):
    """Compare two persons and ask user to select one"""
    while True:
        try:
            print(f"Compare 1: {person1['name']}, a {person1['description']}, from {person1['country']}.")
            print(f"{vs}")
            print(f"Compare 2: {person2['name']}, a {person2['description']}, from {person2['country']}.")

            # For testing, comment block above and uncomment block below
            # print(f"Compare 1: {person1['name']}, a {person1['description']}, from {person1['country']}, with {person1['follower_count']}.")
            # print(f"{vs}")
            # print(f"Compare 2: {person2['name']}, a {person2['description']}, from {person2['country']}, with {person2['follower_count']}.")

            # Ask user to pick the (1)st or (2)nd person
            user_input = int(input(f"\nWho has more followers? Type 1 or 2: "))

            # Break loop if user provides valid input
            if user_input in [1,2]:
                return user_input
        
        except ValueError:
            pass


def person_info():
    """Randomize a person"""
    person_details = random.choice(data)
    return person_details


if __name__ == "__main__":
    main()