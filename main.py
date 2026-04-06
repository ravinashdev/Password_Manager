# ---------------------------- IMPORTS ------------------------------- #
from tkinter import *
from tkinter import messagebox
import pandas as pd
from file_manager import FileManager
from random import *
import json
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
    generated_password= ""
    password_character_length = int(password_character_length_spinbox.get())
    for i in range (password_character_length):
        random_number = randint(33,126)
        generated_password += ascii_table_dictionary[random_number]
    # Insert randomly generated password into entry field if user doesn't care to make one
    # clear existing entry if user chooses to keep generating new passwords
    password_entry.delete(0, "end")
    password_entry.insert(0,generated_password)
    # ---------------------------- ADD_PASSWORD_BUTTON_COMMANDS ------------------------------- #
def add_password_record_to_data_file():
    # print("Adding Password")
    # Get all entries with helper functions
    website = website_entry_getter()
    email = email_username_entry_getter()
    password = password_entry_getter()
    # Create a type of form validation so user cannot add a record unless all fields all filled out
    # Return booleans TRUE/FALSE
    if not website.strip() or not email.strip() or not password.strip():
        messagebox.showerror("Missing Data", "Please enter all required information")
    else:
        # Ask user to confirm submission to give them a chance to edit mistakes
        # Create a validator so duplicate entries are not written to the file
        # Read the existing file if it exists function moves to else condition
        filemanager = FileManager()
        # Return booleans TRUE/FALSE
        confirmation = messagebox.askyesno("Confirmation", f"Do you wish to continue? \n Website: {website}\nEmail: {email}\nPassword: {password}")
        if confirmation:
            try:
                file_content = filemanager.read_file("password_data.txt")
            except FileNotFoundError:
                # Error handling
                # print("Error: The file was not found.")
                messagebox.showerror("File Not Found", "Existing file not found new file being created")
                # Create a new file if it's the users first time using the application
                # If so create a new file
                password_record = website + " | " + email + " | " + password + "\n"
                filemanager.append_to_file("password_data.txt", password_record)
            else:
                password_record = website + " | " + email + " | " + password + "\n"
                # Prevent user from entering the same record twice
                if password_record in file_content:
                    messagebox.showerror("Duplicate Record", "Duplicate Record")
                elif password_record not in file_content:
                    filemanager.append_to_file("password_data.txt", password_record)
            finally:
                # raise
                file_content.close()
def add_password_record_to_json_file():
    # print("Adding Password")
    # Get all entries with helper functions
    website = website_entry_getter()
    email = email_username_entry_getter()
    password = password_entry_getter()
    # Create a type of form validation so user cannot add a record unless all fields all filled out
    # Return booleans TRUE/FALSE
    if not website.strip() or not email.strip() or not password.strip():
        messagebox.showerror("Missing Data", "Please enter all required information")
    else:
        # Ask user to confirm submission to give them a chance to edit mistakes
        # Create a validator so duplicate entries are not written to the file
        # Read the existing file if it exists function moves to else condition
        # Return booleans TRUE/FALSE
        confirmation = messagebox.askyesno("Confirmation", f"Do you wish to continue? \n Website: {website}\nEmail: {email}\nPassword: {password}")
        if confirmation:
            password_record_dictionary = {
                website: {
                    "Email": email,
                    "Password": password
                }
            }
            try:
                # Read the existing file
                with open("password_data.json", "r") as password_data_json_file:
                    json_data = json.load(password_data_json_file)
                # Update json_data to the file and save to it
                json_data.update(password_record_dictionary)
                # Open and write back that updated data to the existing file
                with open("password_data.json", "w") as password_data_json_file:
                    json.dump(json_data, password_data_json_file)
                    # Delete the entry fields so user doesn't add the same record again'
                    website_entry.delete(0, "end")
                    password_entry.delete(0, "end")
            except (FileNotFoundError, json.JSONDecodeError):
                # This is the exception for when the user creates the first record
                with open("password_data.json", "w") as password_data_json_file:
                    json.dump(password_record_dictionary, password_data_json_file)
                    website_entry.delete(0, "end")
                    password_entry.delete(0, "end")


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
website_entry = Entry(window,width=21)
website_entry.grid(ipadx=20,row=1, column=1, columnspan=1, sticky="ew")
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
# add_button = Button(width=36, text="Add", command=lambda: add_password_record_to_data_file())
add_button = Button(width=36, text="Add", command=lambda: add_password_record_to_json_file())
add_button.grid(ipadx=20,row=5, column=1 , columnspan=2, sticky="ew")
search_button = Button(text="Search")
search_button.grid(ipadx=20,row=1, column=2, columnspan=1, sticky="ew")
# Keep window object open so it doesn't close
window.mainloop()
