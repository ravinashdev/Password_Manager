# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #
def generate_password():
    print("Generating Password")
def add_password():
    print("Adding Password")

# ---------------------------- UI SETUP ------------------------------- #
# Initialize the window
window = Tk()
window.title("Password Manager")
# Padding to the window
window.config(padx=20, pady=20)
# Create the canvas using the .png
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
# Initialize the image in a PhotoImage class
lock_png = PhotoImage(file="logo.png")
# Create the image using a create_image module
canvas.create_image(100, 100, image=lock_png)
canvas.grid(row=0, column=2)

# Labels
website_entry_label = Label(window, text="Website:")
website_entry_label.grid(ipadx=20,row=1, column=1, columnspan=1, sticky="ew")
email_username_label = Label(window, text="Email/Username:")
email_username_label.grid(ipadx=20,row=2, column=1, columnspan=1, sticky="ew")
password_label = Label(window, text="Password:")
password_label.grid(ipadx=20,row=3, column=1, columnspan=1, sticky="ew")

# Entry Fields
website_entry = Entry(window)
website_entry.grid(ipadx=20,row=1, column=2, columnspan=2, sticky="ew")
email_username_entry = Entry(window)
email_username_entry.grid(ipadx=20,row=2, column=2, columnspan=2, sticky="ew")
password_entry = Entry(window)
password_entry.grid(ipadx=20,row=3, column=2, columnspan=2, sticky="ew")

# Buttons
generate_password_button = Button(text="Generate Password", command=lambda: generate_password())
generate_password_button.grid(ipadx=20,row=3, column=3, columnspan=1, sticky="ew")
add_button = Button(text="Add", command=lambda: add_password())
add_button.grid(ipadx=20,row=4, column=2 , columnspan=4, sticky="ew")
# Keep window object open so it doesn't close
window.mainloop()
