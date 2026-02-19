# By: 3lmkrew
# Date: 7/11/2021
# Project: Password Generator that saves data into text file.

from tkinter import *
import random
import pyperclip
from tkinter import messagebox
import pygame  # Using for sound effects
import json

# --------------------------------- PASSWORD GENERATOR ------------------------------------------------------------ #

alpha = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"
]  # lower case alphabet list
upper_alpha = [letter.upper() for letter in alpha]  # Creating an alphabet list with all capital letters
nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # string number list
symbols = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "?", "=", "_"]  # symbols list


def password_generator():  # first password generator
    password = ""  # empty string container
    for num in range(random.randint(3, 4)):  # random range from 3-4
        password += random.choice(alpha)  # add random lower case letter
        password += random.choice(nums)  # add random number
        password += random.choice(symbols)  # add random symbol
        password += random.choice(upper_alpha)  # add random upper case letter
    scrambled = "".join(random.sample(password, len(password)))
    pyperclip.copy(scrambled)  # copies the password and ready to paste
    password_entry.delete(0, END)  # replace existing value instead of appending a new password
    password_entry.insert(END, scrambled)  # inserts the password into password Entry box
    play_boxing_bell()


def another_password_generator():  # another password generator
    random_alpha = [random.choice(alpha) for letter in
                    range(random.randint(4, 5))]  # creates list with 4-5 lower case letters
    random_upper = [random.choice(upper_alpha) for letter in
                    range(random.randint(4, 5))]  # creates list with 4-5 upper case letters
    random_nums = [random.choice(nums) for num in range(random.randint(2, 4))]  # creates list with 2-4 numbers
    random_symbols = [random.choice(symbols) for symbol in range(random.randint(2, 4))]  # creates list with 2-4 symbols
    pass_code = random_alpha + random_upper + random_nums + random_symbols  # create new list from all previous list combined
    random.shuffle(pass_code)  # shuffles the combined list
    code = "".join(pass_code)  # creates a string instead of list
    pyperclip.copy(code)  # copies list to allow for paste
    password_entry.delete(0, END)  # replace existing value instead of appending a new password
    password_entry.insert(END, code)  # inserts the password into the password Entry box
    play_boxing_bell()


# ---------------------------------- SAVE PASSWORD ----------------------------------------------------------------- #

def add_to_file():
    website_input = website_entry.get()  # get the web entry and save to var
    user_name_input = user_name_entry.get()  # get user name entry and save to var
    pass_input = password_entry.get()  # get password entry and save to var
    new_data = {website_input: # Crate a dictionary using 3 entry's
        {
            "Email": user_name_input,
            "Password": pass_input
        }
    }
    if len(website_input) != 0 and len(user_name_input) != 0 and len(pass_input) != 0:  # if all entry's have at least one item
        # if file exist, open in read mode, load json to data, update data with new entry
        try:
            file = open("data.json", "r")  # open json file in read mode 
            data = json.load(file)  # create data load object passing file as argument, will create a python dictionary
            data.update(new_data)  # update the data OBJECT using .update() method and passing the new entered values
            file.close()
        # if FileNotFoundError occurs, create new file in write mode and add new data entry (instead of crashing)
        except FileNotFoundError:
            file = open("data.json", "w")
            json.dump(new_data, file, indent=4)
            file.close()  # close the file
        # if file exist, open in write mode and add all the data to json file.
        else:
            file = open("data.json", "w")
            json.dump(data, file, indent=4)
            file.close()  # close the file

            # messagebox.showinfo(title="Successful.", message="Data has been saved to data.txt file") # show successfully saved box
    else:
        messagebox.showerror("Warning.", "You left an empty field")  # if at least one entry is empty, show warning box


# ---------------------------------SEARCH BY WEBSITE----------------------------------------------------------------#

def find_password():
    web = website_entry.get()  # get the web entry and save to a var
    try:
        file = open("data.json", "r")  # open json file in read mode
        data = json.load(file) # load json file into data variable, creates a python dictionary
        #print(data)
        file.close() # close file after search is complete

    except FileNotFoundError:
        messagebox.showinfo(
            title="Not Found",
            message="File named data.json does not exist"
        )


    else:
        if web in data:  # if the search entry is in the json data dic
            email = data[web]["Email"]  # email is retrieved
            password = data[web]["Password"]  # password is retrieved
            messagebox.showinfo(title=f"{web} information Found", message=f"Email:  {email}\nPassword:  {password} ")
        else:
            messagebox.showinfo(title="Not Found", message=f"Sorry File Not Found")


# -----------------------------------------CLEAR ALL ENTRYS--------------------------------------------------------#

def clear_all():
    website_entry.delete(0, END)
    user_name_entry.delete(0, END)
    password_entry.delete(0, END)
    play_flash_sound()


# -------------------------------------SOUNDS-----------------------------------------------------------------#

pygame.mixer.init()


def play_boxing_bell():
    pygame.mixer.music.load("boxing_bell.mp3")
    pygame.mixer.music.play(loops=0)


def play_flash_sound():
    pygame.mixer.music.load("flash_sound.mp3")
    pygame.mixer.music.play(loops=0)


def play_chime_bell():
    pygame.mixer.music.load("chime_bell.mp3")
    pygame.mixer.music.play()


# ---------------------------------------- UI SETUP ------------------------------------------------------------ #

# Window Object
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Image Object
photo = PhotoImage(file="logo.png")

# Canvas Object
canvas = Canvas()
canvas.config(width=200, height=200, bg="white", highlightthickness=0)
canvas.create_image(100, 100, image=photo)
canvas.grid(row=0, column=1)

# ------------Labels------------------------------------#
website_label = Label()
website_label.config(text="Website:", fg="black", bg="white", font=("monaco", 10, "bold"))
website_label.grid(row=1, column=0)

user_name_label = Label()
user_name_label.config(text="Email/Username:", fg="black", bg="white", font=("monaco", 10, "bold"))
user_name_label.grid(row=2, column=0)

password_label = Label()
password_label.config(text="Password:", fg="black", bg="white", font=("monaco", 10, "bold"))
password_label.grid(row=3, column=0)

# Entry's/Input's
website_entry = Entry()
website_entry.config(width=22)
website_entry.focus_set()
website_entry.grid(row=1, column=1)

user_name_entry = Entry()
user_name_entry.config(width=42)
user_name_entry.grid(row=2, column=1, columnspan=2)

password_entry = Entry()
password_entry.config(width=22)
password_entry.grid(row=3, column=1)

# --------------------------------Buttons---------------------------------------------------#

# Generate Button
generate_button = Button()
generate_button.config(text="Generate Password", bg="light blue", width=16, command=password_generator)
generate_button.grid(row=3, column=2)

# Add Button
add_button = Button()
add_button.config(text="Add", width=36, bg="orange", command=add_to_file)
add_button.grid(row=4, column=1, columnspan=2)

# Search button
search_button = Button()
search_button.config(text="Search", bg="gold", width=15, command=find_password)
search_button.grid(row=1, column=2)

# clear All Button
clear_button = Button()
clear_button.config(text="Clear All", width=36, bg="light green", command=clear_all)
clear_button.grid(row=5, column=1, columnspan=2)

window.mainloop()
