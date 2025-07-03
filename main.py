from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# ------------------------- PASSWORD GENERATOR ---------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    # Combine letters, symbols, numbers all together to shuffle
    password_list = password_letters + password_symbols + password_numbers
    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password) # Copy the password

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_file():
    save_web = website_input.get()
    save_username = username_input.get()
    save_password = password_input.get()
    new_data = {
        save_web: {
            "username": save_username,
            "password": save_password
        }
    }

    if len(save_web) == 0 or len(save_username) == 0 or len(save_password) == 0:
        messagebox.showerror(title="Error", message="Please fill all fields")
    else:
        with open("data.json", mode="r") as file:
            data = json.load(file)  # Read old data
            data.update(new_data) # Update with new data

        with open("data.json", mode="w") as file:
            json.dump(new_data, file, indent=4) # Write data to json file
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

logo = PhotoImage(file="logo.png")
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1, sticky=EW)

# Labels
website = Label(window, text="Website:")
website.grid(row=1, column=0, sticky=EW)
username = Label(text="Email/Username:")
username.grid(row=2, column=0, sticky=EW)
password = Label(text="Password:")
password.grid(row=3, column=0, sticky=EW)

# Entries
website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky=EW)
website_input.focus() # Automatically put cursor at this entry
username_input = Entry(width=35)
username_input.grid(row=2, column=1, columnspan=2, sticky=EW)
username_input.insert(0, "pham@gmail.com") # Pre populate e-mail
password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky=EW)

# Buttons
generate = Button(text="Generate Password", command=generate_password)
generate.grid(row=3, column=2, sticky=EW)
add = Button(text="Add", width=36, command=save_file)
add.grid(row=4, column=1, columnspan=2, sticky=EW)


window.mainloop()
