# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


# leap year if divisible by 4 AND
# (1) not 100, or
# (2) 100 and 400

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else: 
                return False
        else:
            return True
    else:
        return False

if is_leap(year):
    print("Leap year.")
else:
    print("Not leap year.")