from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
               'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    password = "".join(password_list)
    # same as below
    # password = ""
    # for char in password_list:
    #     password += char

    e_password.delete(0, END)
    e_password.insert(0, f"{password}")
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save_password():
    website = str(e_website.get()).capitalize()
    username = str(e_username.get())
    password = str(e_password.get())
    new_data = {
        website: {
            "email": username,
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Reading old data
                data = json.load(data_file)
                # Updating old data with new data
                data.update(new_data)
            with open("data.json", "w") as data_file:
                # Saving updated data
                json.dump(data, data_file, indent=4)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        finally:
            e_website.delete(0, END)
            e_password.delete(0, END)


def find_password():
    s_website = e_website.get().capitalize()
    print(s_website)
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showwarning(title="Error", message="No data file found.\nInsert some data first!")

    else:
        if s_website in data:
            email = data[s_website]["email"]
            password = data[s_website]["password"]
            messagebox.showinfo(title=s_website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Not found", message=f"No details for {s_website} exists.")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Label
l_website = Label(text="Website", width=10)
l_website.grid(column=0, row=1)
l_username = Label(text="Email/Username:", width=10)
l_username.grid(column=0, row=2)
l_password = Label(text="Password", width=10)
l_password.grid(column=0, row=3)

# Button
b_generatep = Button(text="Generate Password", command=generate_password)
b_generatep.grid(column=2, row=3)
b_add = Button(text="Add", width=36, command=save_password)
b_add.grid(column=1, row=4, columnspan=2)
b_search = Button(text="Search", width=13, command=find_password)
b_search.grid(column=2, row=1)

# Entry
e_website = Entry(width=21)
e_website.grid(column=1, row=1)
e_website.focus()
e_username = Entry(width=35)
e_username.grid(column=1, row=2, columnspan=2)
e_username.insert(0, "acorcos@gmail.com")
e_password = Entry(width=21)
e_password.grid(column=1, row=3)

window.mainloop()
