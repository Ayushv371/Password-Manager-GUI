import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json

def add():
    website = web_entry.get()
    password = pass_entry.get()
    email = Email_entry.get()

    web_entry.delete(0, END)
    pass_entry.delete(0, END)
    Email_entry.delete(0, END)

    file_data = {
        website: {
            "email": email,
            "password": password,
        }
    }

    if website == "" or password == "" or email == "":
        messagebox.showwarning(title="Warning", message="Fill all fields")
    else:
        try:
            with open("data.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            data = {}

        data.update(file_data)

        with open("data.json", "w") as f:
            json.dump(data, f, indent=4)

        messagebox.showinfo(title="Info", message="Website added successfully")


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = [random.choice(letters) for _ in range(8)]
    password_list += [random.choice(numbers) for _ in range(2)]
    password_list += [random.choice(symbols) for _ in range(2)]
    random.shuffle(password_list)
    new_password = "".join(password_list)
    pass_entry.delete(0, END)
    pass_entry.insert(0, new_password)
    pyperclip.copy(new_password)


window = Tk()
window.title("Password Manager")
window.minsize(width=500, height=400)
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200)
photo = PhotoImage(file="pass_logo.png")

canvas.create_image(100,100,image=photo)
canvas.grid(row=0, column=1)
canvas.config(bg="white", highlightthickness=0)

web_label = Label(text="Website:", bg="white")
web_label.grid(row=1, column=0)

Email_label = Label(text="Email/Username:", bg="white")
Email_label.grid(row=2, column=0)

pass_label = Label(text="Password:", bg="white")
pass_label.grid(row=3, column=0)

web_entry = Entry(width=35)
web_entry.grid(row=1, column=1, columnspan=2)
web_entry.focus()

Email_entry = Entry(width=35)
Email_entry.grid(row=2, column=1, columnspan=2)

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1)

generate_btn = Button(text="Generate Password",highlightthickness=0, bd=0, bg="white", command=generate_password)
generate_btn.grid(row=3, column=2)

add_btn = Button(text="Add", width=36, highlightthickness=0, bd=0, bg="white", command=add)
add_btn.grid(row=4, column=1, columnspan=2)

window.mainloop()