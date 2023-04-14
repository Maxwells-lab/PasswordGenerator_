from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle

import pyperclip

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_shuffle():
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_letters + password_numbers + password_symbols
    shuffle(password_list)

    passwordMe= "".join(password_list)
    password.insert(0,passwordMe )
    pyperclip.copy(passwordMe)

window = Tk()
window.config(padx=100, pady=50)
window.minsize(width=600, height=900)
window.title("Password Manager")
image = PhotoImage(file="logo.png")
canvas = Canvas(height=300, width=350)
canvas.create_image(250, 200, image=image)


def save():
    website = site_entry.get()
    email = site_email.get()
    password1 = password.get()
    if len(website) == 0 or len(site_email.get()) == 0 or len(password.get()) == 0:
        messagebox.showinfo(title="Oops", message=f"Some entries are empty!!!")
    else:
        is_ok = messagebox.askokcancel(title=site_entry.get(),
                                       message=f"Are u satisfied with your entry please!\n {site_email.get()}\n {site_entry.get()}\n {password.get()}\n")
        if is_ok:
            with open("save_data", "a") as data_file:
                data_file.write(f"website:{website} | Email_Account:{email} | Password: {password1}\n ")
                site_entry.delete(0, END)
                site_email.delete(0, END)
                password.delete(0, END)


# components
label_site = Label(text="Website")
label_site.grid(row=1, column=0, columnspan=1)
label_email = Label(text="Email/Username:")
label_email.grid(row=2, column=0, columnspan=1)
label_pass = Label(text="Password:")
label_pass.grid(row=3, column=0, columnspan=1)

button_pass = Button(text="Generate Password", command=password_shuffle)
button_pass.grid(row=3, column=2)

add_buton = Button(text="Add", command=save)
add_buton.grid(row=4, column=1, columnspan=2)

site_entry = Entry(width=35)
site_entry.focus()
site_entry.grid(row=1, column=1, columnspan=2)

site_email = Entry(width=35)
site_email.insert(0, "name@gmail.com")
site_email.grid(row=2, column=1, columnspan=2)

password = Entry(width=35)
password.grid(row=3, column=1, columnspan=2)

canvas.grid(row=0, column=1)
window.mainloop()
