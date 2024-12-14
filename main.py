from json import JSONDecodeError
from tkinter import *
import random
import sys
import os
from tkinter import messagebox
import json
###Constants
FONT_NAME = "Courier"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_pass():
    password_entry.delete(0, 'end')
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
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_login():

    website = website_entry.get()
    user = user_entry.get()
    password = password_entry.get()
    new_data = {
        website: {
                "email": user,
                "password": password,
             }
         }
##todo finish day 30 --- was here in video---
    if len(website) == 0 or len(password) ==0:
            messagebox.askokcancel(title='OOPS', message='Please be sure to fill out all fields first!')
    else:
        try:
            with open(data_path, 'r') as data_file:
                # json.dump(new_data, data_file, indent = 4 )
                data = json.load(data_file)
                data.update(new_data)

        except FileNotFoundError:
            with open(data_path, "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        except JSONDecodeError:
            with open(data_path, "w") as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)

            with open(data_path, "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)
        finally:
            website_entry.delete(0, END)
            user_entry.delete(0, END)
            password_entry.delete(0, END)



#----------------------------SEARCH FUNCTION--------------------------#
def search():
    website = website_entry.get()
    try:
        with open(data_path) as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data File Found.")
    except JSONDecodeError:
        messagebox.askokcancel(title='OOPS', message='Database is currently empty.\nPlease save atleast one login before using search.')

    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}\n\nCopied to Clipboard in user:pass format.")
            tk.clipboard_clear()
            tk.clipboard_append(f'{email}:{password}')
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
    finally:
        website_entry.delete(0, END)
        user_entry.delete(0,END)
        password_entry.delete(0, END)
#     website = website_entry.get()
#     if website == '':
#         messagebox.askokcancel(title='Error', message=f'No Website Entered')
#     with open(DATA, "r") as file:
#         lines = file.readlines()
#
#         for line in lines:
#
#             elif website in line:
#                 print(line)
#                 messagebox.askokcancel(title=f'{website}', message=f'Logins Found: {line}')

            # elif website:
            #     no_login =messagebox.askokcancel(title='Error', message=f'No logins Found')
            #     if no_login:
            #         os.execl(sys.executable, sys.executable, *sys.argv)
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

data_path = resource_path('data/data.json')

canvas = Canvas(width=200, height=200)
canvas.grid(column=1,row=0,)
canvas.create_image(100, 100,image=logo,)




# data_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
# data = resource_path(image_path)

#website
website_label = Label(text='Website:', font=('Courier', 10, 'bold'))
website_label.grid(column=0,row=1)

website_entry = Entry(width=32,)
website_entry.grid(column=1,row=1,)
website_entry.focus()

#email/username
user_label = Label(text='Username/Email:', font=('Courier', 10, 'bold'))
user_label.grid(column=0,row=2)

user_entry = Entry(width=50)
user_entry.grid(column=1,row=2,columnspan=3)

#password
password_label = Label(text='Password:', font=('Courier', 10, 'bold'))
password_label.grid(column=0,row=3)

password_entry = Entry(width=32)
password_entry.grid(column=1,row=3,)

#buttons
password_gen = Button(text='Generate Password',borderwidth=.5, highlightcolor='black',command=generate_pass)
password_gen.grid(column=2,row=3,)
# save
add = Button(text='Add to Database',width=42, command=save_login,padx=2)
add.grid(column=1,row=4,columnspan=2)
#search
search = Button(text='Search Database',borderwidth=.5, highlightcolor='black',command=search, padx=8)
search.grid(column=2,row=1)
tk.mainloop()
