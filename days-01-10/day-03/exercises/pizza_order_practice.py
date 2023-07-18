# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

pepperoni = 0
cheese = 0

if size == "S":
    if add_pepperoni == "Y":
        pepperoni = 2
    price = 15
elif size == "M":
    if add_pepperoni == "Y":
        pepperoni = 3
    price = 20
elif size == "L":
    if add_pepperoni == "Y":
        pepperoni = 3
    price = 25

if extra_cheese == "Y":
    cheese = 1

bill = price + pepperoni + cheese
print(f"Your final bill is: ${bill}.")