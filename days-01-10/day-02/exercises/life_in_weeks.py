# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

end_age = 90
years_left = end_age - int(age)
days = 365 * years_left
weeks = 52 * years_left
months = 12 * years_left
print(f"You have {days} days, {weeks} weeks, and {months} months left.")
