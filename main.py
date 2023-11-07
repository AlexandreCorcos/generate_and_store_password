from tkinter import *
from tkinter import messagebox
import random
import pyperclip


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
    website = str(e_website.get())
    username = str(e_username.get())
    password = str(e_password.get())

    if len(website) == 0 or len(password) == 0:
        messagebox.showwarning(title="Error", message="Please make sure you haven't left any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \n"
                                                              f"Email: {username}\nPassword: {password}\nIs it ok to save?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(f"{website} | {username} | {password}\n")
                e_website.delete(0, END)
                e_password.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Label
l_website = Label(text="Website")
l_website.grid(column=0, row=1)
l_username = Label(text="Email/Username:")
l_username.grid(column=0, row=2)
l_password = Label(text="Password")
l_password.grid(column=0, row=3)

# Button
b_generatep = Button(text="Generate Password", command=generate_password)
b_generatep.grid(column=2, row=3)
b_add = Button(text="Add", width=36, command=save_password)
b_add.grid(column=1, row=4, columnspan=2)

# Entry
e_website = Entry(width=35)
e_website.grid(column=1, row=1, columnspan=2)
e_website.focus()
e_username = Entry(width=35)
e_username.grid(column=1, row=2, columnspan=2)
e_username.insert(0, "acorcos@gmail.com")
e_password = Entry(width=21)
e_password.grid(column=1, row=3)

window.mainloop()
