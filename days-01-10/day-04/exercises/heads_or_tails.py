#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

face = [0, 1]
computer_coin = random.choice(face)
if computer_coin == 0:
    print("Tails")
else:
    print("Heads")