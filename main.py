from tkinter import *
import random
import sys
import os
from tkinter import messagebox
###Constants
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    clear()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = 8
    nr_numbers = 8
    nr_symbols = 8
    password = random.sample(letters, nr_letters) + random.sample(symbols, nr_symbols) + random.sample(numbers, nr_numbers)
    characters = nr_numbers+nr_symbols+nr_letters
    randomize = random.sample(password, characters)
    final_pass =''.join(randomize)
    password_entry.insert(END, string= final_pass)
    #copy to clipboard auto
    tk.clipboard_clear()
    tk.clipboard_append(final_pass)

def clear():
    password_entry.delete(0, 'end')
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_login():
    with open(data, 'a') as file:
        website = website_entry.get()
        user = user_entry.get()
        password = password_entry.get()

        is_ok = messagebox.askokcancel(title=website, message=f'Confirm Details: \nEmail: {user} \nPassword: {password}')
        if is_ok:
            file.writelines(f'{website} | {user} | {password}\n')
            website_entry.delete(0,END)
            user_entry.delete(0, END)
            password_entry.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #
tk = Tk()
tk.title('Password Manager - by SneezeGUI')
tk.config(padx=20, pady=20)


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
image_path = resource_path('logo/logo.png')
logo = PhotoImage(file=image_path)

canvas = Canvas(width=200, height=200)
canvas.grid(column=1,row=0, columnspan=2)
canvas.create_image(100, 100,image=logo,)

data ='data.txt'

#website

website_label = Label(text='Website:', font=('Courier', 10, 'bold'))
website_label.grid(column=0,row=1)
website_entry = Entry(width=40,)
website_entry.grid(column=1,row=1, columnspan=4)
website_entry.focus()

#email/username
user_label = Label(text='Username/Email:', font=('Courier', 10, 'bold'))
user_label.grid(column=0,row=2)

user_entry = Entry(width=40)
user_entry.grid(column=1,row=2,columnspan=4)

#password
password_label = Label(text='Password:', font=('Courier', 10, 'bold'))
password_label.grid(column=0,row=3)


password_entry = Entry(width=21)
password_entry.grid(column=1,row=3)

#buttons
password_gen = Button(text='Generate Password',borderwidth=.5, highlightcolor='black',command=generate_pass)
password_gen.grid(column=2,row=3,columnspan=3)


add = Button(text='Add to Database',width=30, command=save_login)
add.grid(column=1,row=4,columnspan=3)


tk.mainloop()
