import tkinter
import random
import pyperclip
import json
from tkinter import messagebox
from tkinter import END

FONT_NAME = "Arial"

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for item in range(nr_letters)]
    password_symbols = [random.choice(symbols) for item in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for item in range(nr_numbers)]

    password_list = password_letters + password_symbols + password_numbers
    
    random.shuffle(password_list)

    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- ADD PASSWORD ------------------------------- #
def add():
    website = website_entry.get()
    email = email_user_entry.get()
    password = password_entry.get()
    new_data = {website: {
        "email": email,
        "password": password
        }
    }
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops!", message=f"Please don't leave any fields empty.")   
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)   
        except FileNotFoundError:
            with open("data.json", "w") as data_file:             
                # Creating new file and saving new data to it
                json.dump(new_data, data_file, indent=4)            
        else:
            # Updating old data with new data
            data.update(new_data)
            
            with open("data.json", "w") as data_file:             
                # Saving updated data
                json.dump(data, data_file, indent=4)    
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
            messagebox.showinfo(title="Error", message="File not found.")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"Record {website} not found.")

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=70, bg="white")

canvas = tkinter.Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = tkinter.PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=0, row=0, columnspan=3)

# Labels

website_label = tkinter.Label(text="Website:", fg="black", bg="white", font=(FONT_NAME, 14))
website_label.grid(column=0, row=1)

email_user_label = tkinter.Label(text="Email/Username:", fg="black", bg="white", font=(FONT_NAME, 14))
email_user_label.grid(column=0, row=2)

password_label = tkinter.Label(text="Password:", fg="black", bg="white", font=(FONT_NAME, 14))
password_label.grid(column=0, row=3)

# Entries

website_entry = tkinter.Entry(width=25, fg="black", bg="white", font=(FONT_NAME, 14), highlightthickness=0)
website_entry.grid(column=1, row=1)
website_entry.focus()

email_user_entry = tkinter.Entry(width=45, fg="black", bg="white", font=(FONT_NAME, 14), highlightthickness=0)
email_user_entry.grid(column=1, row=2, columnspan=2)
email_user_entry.insert(0, "insertemailhere@gmail.com")

password_entry = tkinter.Entry(width=22, fg="black", bg="white", highlightthickness=0)
password_entry.grid(column=1, row=3)

# Buttons

search_button = tkinter.Button(text="Search", fg="black", command=search, highlightbackground="white", width = 15, font=(FONT_NAME, 14), highlightthickness=0)
search_button.grid(column=2, row=1)

generate_button = tkinter.Button(text="Generate Password", fg="black", command=generate, highlightbackground="white", font=(FONT_NAME, 14), highlightthickness=0)
generate_button.grid(column=2, row=3)

add_button = tkinter.Button(width=40, text="Add", fg="black", command=add, highlightbackground="white", font=(FONT_NAME, 14), highlightthickness=0)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()