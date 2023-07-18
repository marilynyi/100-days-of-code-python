print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

print("\nYou wake up and find yourself on a sandy path.")
print("Dazed and confused, you walk until you come across a fork.")
left_or_right = input('\nWhich way do you want to go? Type "left" or "right".\n').strip().lower()

if left_or_right == "l" or left_or_right == "left":
    print("\nYou take the left path until you come across a river.")
    print("On the other side you see a house.")
    print("There is a bridge down the river but it is far.")
    swim_or_walk = input('\nDo you swim across or make your way to the bridge. Type "swim" or "walk".\n').lower()
    if swim_or_walk == "walk":
        print("\nYou make your way across the bridge and to the house.")
        print("There are three doors at the front.")
        print("Red on the left, yellow in front, and blue on the right.")
        door_color = input('\nWhich door do you choose? Type "red", "yellow", or "blue".\n').lower()
        if door_color in ["y", "yellow"]:
            print("\nYou found the exit. You win!")
        elif door_color in ["r", "red"]:
            print("\nOh no! You've interrupted the warlocks in the middle of their ritual. Game over.")
        elif door_color in ["b", "blue"]:
            print("\nGhostly hands reach out at you and pull you into the room. Game over.")
        else:
            print("\nYou spooked the ogre in the room. Game over.")
    else:
        print("\nA hungry alligator snuck up on you. Game over.")
        
else:
    print("\nYou take the right path and fell into a trap. Game over.")
