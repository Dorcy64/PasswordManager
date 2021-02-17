from tkinter import *
from tkinter import messagebox
import random
import pyperclip

LETTERS = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
DIGIT = "0123456789"
SYMBOLS = "!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password():
    password_entry.delete(0, END)
    generated_password = []
    for _ in range(4):
        generated_password.append(random.choice(LETTERS))
        generated_password.append(random.choice(LETTERS))
        generated_password.append(random.choice(DIGIT))
        generated_password.append(random.choice(SYMBOLS))

    random.shuffle(generated_password)
    new_password = "".join(generated_password)
    pyperclip.copy(new_password)
    password_entry.insert(0, new_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password_object = password_entry.get()

    if len(website) <= 0 or len(email) <= 0 or len(password_object) <= 0:
        messagebox.showerror(message="Please fill in the blanks")
    else:
        save_ok = messagebox.askokcancel(title=website, message=f"These are the credentials you want to save: \n"
                                                                f"Email: {email}\nPassword: {password_object}\n"
                                                                f"Do you want to save?")
        if save_ok:
            with open("data.txt", mode="a") as file:
                file.write(f"{website} | {email} | {password_object}\n")
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
photo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=photo_image)
canvas.grid(column=2, row=1)

# Labels
website_label = Label(text="Website:", justify="left")
website_label.grid(column=1, row=2)

email_label = Label(text="Email/Username:", justify="left")
email_label.grid(column=1, row=3)

password_label = Label(text="Password:", justify="left")
password_label.grid(column=1, row=4)

# Entry Boxes
website_entry = Entry(width=36)
website_entry.grid(column=2, row=2, columnspan=2)

email_entry = Entry(width=36)
email_entry.grid(column=2, row=3, columnspan=2)
email_entry.insert(0, "tugirimanadorcy64@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(column=2, row=4)

# Buttons
generate = Button(text="Generate Password", command=password)
generate.grid(column=3, row=4)

add = Button(text="Add", width=37, command=save)
add.grid(column=2, row=5, columnspan=2)

window.mainloop()
