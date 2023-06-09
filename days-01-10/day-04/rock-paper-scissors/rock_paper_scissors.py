import random
from art import rock, paper, scissors

# Go to https://replit.com/@appbrewery/rock-paper-scissors-start?v=1


#Write your code below this line 👇
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# User wins if [user, comp]
# 0, 2
# 1, 0
# 2, 1

# Draw if
# 0, 0
# 1, 1
# 2, 2

# User loses if
# 0, 1
# 1, 2
# 2, 0

art = [rock, paper, scissors]

comp_input = random.randint(0, 2)
print(f"You picked {art[user_input]} and the computer picked {art[comp_input]}.")
if [user_input, comp_input] in [[0,2], [1,0], [2,1]]:
    print("You win!")
elif user_input == comp_input:
    print("It's a draw!")
elif [user_input, comp_input] in [[0,1],[1,2],[2,0]]:
    print("You lose!")
else: 
    print("Invalid input. Try again.")

