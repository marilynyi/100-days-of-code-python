from tkinter import Tk, Label, Button, Entry, Text

KM_IN_ONE_MILE = 1.609344

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=300, height=150)
window.config(padx=30, pady=30)

# Labels

is_equal_to = Label(text="is equal to")
is_equal_to.grid(column=0, row=1)

miles_text = Label(text="Miles")
miles_text.grid(column=2, row=0)

km_text = Label(text="Km")
km_text.grid(column=2, row=1)

km_output = Label(text="0")
km_output.grid(column=1, row=1)

# Entry

miles_input = Entry(width=5)
miles_input.grid(column=1, row=0)

# Button

def calculate(event=None):
    miles_float = float(miles_input.get())
    input_km = round(miles_float * KM_IN_ONE_MILE, 2)
    km_output.config(text=f"{input_km}")

calc = Button(text="Calculate", command=calculate)
calc.grid(column=1, row=2)

window.bind('<Return>', calculate)


window.mainloop()