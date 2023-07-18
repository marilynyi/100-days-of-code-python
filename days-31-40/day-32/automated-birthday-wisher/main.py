import datetime as dt
import random
import pandas as pd
import smtplib
import config

TODAY = dt.datetime.now()
TODAY_TUPLE = (TODAY.month, TODAY.day)
# Uncomment below and add actual email credentials for Python program to work
MY_EMAIL = config.email
PASSWORD = config.password

data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if TODAY_TUPLE in birthdays_dict:
    birthday_person = birthdays_dict[TODAY_TUPLE]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])
        
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, 
                            to_addrs=birthday_person["email"],
                            msg=f"Subject:Happy Birthday!\n\n")
        
# To run the program every day, start an account on pythonanywhere.com.
# Upload this main program, the letter template, and the birthday list.
# Click on the Consoles tab and create a new Bash console.
# Type 'python3 main.py' and press Enter
# If you encounter a smtplib.SMTPAuthenticationError, click on the support link provided.
# Unlock the captcha then rerun 'python3 main.py' in the bash console again.
# Then click on the Tasks tab to schedule a task.
# Type in 'python3 main.py' and set the time in UTC.

# Only one task is allowed in the free tier of pythonanywhere.com

