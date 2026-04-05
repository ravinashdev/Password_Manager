# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

# ---------------------------- GLOBAL VARIABLES ------------------------------- #

# ---------------------------- FUNCTIONS ------------------------------- #
def generate_password():
    print("Generating Password")
def add_password():
    print("Adding Password")
    # Get all entries with helper functions
    website = website_entry_getter()
    email = email_username_entry_getter()
    password = password_entry_getter()
    print("Website:", website)
    print("Email:", email)
    print("Password:", password)

# ---------------------------- WEBSITE_ENTRY_GETTER ------------------------------- #
def website_entry_getter():
    website = website_entry.get()
    return website
    # ---------------------------- EMAIL/USERNAME_ENTRY_GETTER ------------------------------- #
def email_username_entry_getter():
    email = email_username_entry.get()
    return email
    # ---------------------------- PASSWORD_ENTRY_GETTER ------------------------------- #
def password_entry_getter():
    password = password_entry.get()
    return password
# ---------------------------- UI SETUP ------------------------------- #
# Initialize the window
window = Tk()
window.title("Password Manager")
# Padding to the window
window.config(padx=50, pady=50)
# Create the canvas using the .png
canvas = Canvas(window, width=200, height=200, highlightthickness=0)
# Initialize the image in a PhotoImage class
lock_png = PhotoImage(file="logo.png")
# Create the image using a create_image module
canvas.create_image(100, 100, image=lock_png)
canvas.grid(row=0, column=1)

# Labels
website_entry_label = Label(window, text="Website:")
website_entry_label.grid(ipadx=20,row=1, column=0, columnspan=1, sticky="ew")
email_username_label = Label(window, text="Email/Username:")
email_username_label.grid(ipadx=20,row=2, column=0, columnspan=1, sticky="ew")
password_label = Label(window, text="Password:")
password_label.grid(ipadx=20,row=3, column=0, columnspan=1, sticky="ew")

# Entry Fields
website_entry = Entry(window,width=35)
website_entry.grid(ipadx=20,row=1, column=1, columnspan=2, sticky="ew")
# Place cursor in first entry box
website_entry.focus()
email_username_entry = Entry(window, width=35)
email_username_entry.grid(ipadx=20,row=2, column=1, columnspan=2, sticky="ew")
email_username_entry.insert(0, "ryan@email.com")
password_entry = Entry(window, width=21)
password_entry.grid(ipadx=20,row=3, column=1, columnspan=1, sticky="ew")

# Buttons
generate_password_button = Button(text="Generate Password", command=lambda: generate_password())
generate_password_button.grid(ipadx=20,row=3, column=2, columnspan=1, sticky="ew")
add_button = Button(width=36,text="Add", command=lambda: add_password())
add_button.grid(ipadx=20,row=4, column=1 , columnspan=2, sticky="ew")
# Keep window object open so it doesn't close
window.mainloop()
