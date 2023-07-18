import smtplib
import datetime as dt

# Set up actual email credentials for Python program to work
my_email = "testsender@gmail.com" 
password = "passwordhere"

with smtplib.SMTP("smtp.gmail.com") as connection:
    # Secures email with encryption 
    connection.starttls()
    # Log into email account
    connection.login(user=my_email, password=password)
    # Send email
    connection.sendmail(from_addr=my_email, 
                        to_addrs="testreceiver@gmail.com", 
                        msg="Subject:Hello\/\/This is the body of my email.")

# If sender email is a Gmail account:
# Go to Gmail settings, Security, and turn on 2-step verification.
# This will enable 'App passwords'. Click and then enter password.
# Create 'Other' type of app and name it 'birthday_wisher'
# Copy the app password and paste it in the 'password' field on line 4

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=1995, month=12, day=15, hour=4)
print(date_of_birth)