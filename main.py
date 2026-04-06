# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
import pandas as pd
from file_manager import FileManager
from random import *
# ---------------------------- PANDAS ------------------------------- #
ascii_table= pd.read_csv("ascii-table.csv")
# print(ascii_table)
ascii_table_characters_dataframe = ascii_table.iloc[33:127]
# print(ascii_table_characters_dataframe)
ascii_table_dictionary = { index:row["Character"] for (index,row) in ascii_table_characters_dataframe.iterrows() }
# print(ascii_table_dictionary)
# ---------------------------- CONSTANTS ------------------------------- #
# ---------------------------- GLOBAL VARIABLES ------------------------------- #
# ---------------------------- FUNCTIONS ------------------------------- #
# ---------------------------- GENERATE_PASSWORD_BUTTON_COMMAND ------------------------------- #
def generate_password():
    # print("Generating Password")
    # print(ascii_table_dictionary)
    generated_password= ""
    password_character_length = int(password_character_length_spinbox.get())
    for i in range (password_character_length):
        random_number = randint(33,126)
        generated_password += ascii_table_dictionary[random_number]
    # Insert randomly generated password into entry field if user doesn't care to make one
    # clear existing entry if user chooses to keep generating new passwords
    password_entry.delete(0, "end")
    password_entry.insert(0,generated_password)
    # ---------------------------- ADD_PASSWORD_BUTTON_COMMAND ------------------------------- #
def add_password():
    # print("Adding Password")
    # Get all entries with helper functions
    website = website_entry_getter()
    email = email_username_entry_getter()
    password = password_entry_getter()
    password_record = website + " | " + email + " | " + password + "\n"
    filemanager = FileManager()
    filemanager.append_to_file("password_data.txt", password_record)

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
    # ---------------------------- PASSWORD_ENTRY_GETTER ------------------------------- #
def password_character_spinbox_getter():
    password_character_length = password_character_length_spinbox.get()
    return password_character_length
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
password_character_length_label = Label(window, text="Password Gen Char Length:")
password_character_length_label.grid(ipadx=20,row=4, column=0, columnspan=1, sticky="ew")

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

# Spinbox
password_character_length_spinbox = Spinbox(from_=0, to=24, justify="center", command=password_character_spinbox_getter)
password_character_length_spinbox.grid(ipadx=20,row=4, column=1, columnspan=2, sticky="ew")

# Buttons
generate_password_button = Button(text="Generate Password", command=lambda: generate_password())
generate_password_button.grid(ipadx=20,row=3, column=2, columnspan=1, sticky="ew")
add_button = Button(width=36,text="Add", command=lambda: add_password())
add_button.grid(ipadx=20,row=5, column=1 , columnspan=2, sticky="ew")
# Keep window object open so it doesn't close
window.mainloop()
