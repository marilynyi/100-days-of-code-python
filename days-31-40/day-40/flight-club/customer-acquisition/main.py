import sheety

print("Welcome to the Flight Club.")
print("We find the best flight deals and email them to you.\n")
first_name = input("What is your first name? ").title()
last_name = input("What is your last name? ").title()

email = "email"
email_confirm = "email2"
email_needs_confirm = True

while email != email_confirm:
  email = input("What is your email? ")
  email_confirm = input("Verify your email: ")
  
  if email_confirm.lower() != email.lower():
    print("The emails don't match. Please try again.")

print("You are now in the club.")

sheety.post_new_row(first_name, last_name, email)