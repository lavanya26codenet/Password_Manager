from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip

#---------------------GENERATE PASSWORD------------------------------------#
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password ="".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

#------------------------SAVES PASSWORD-----------------------------------#
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Opps!!",
                            message="Make sure you haven't left any field empty")

    else:
        is_ok = messagebox.askyesno(title=website, message=f"The Email is {email} and password is {password}."
                                                           f" \nDo you want to save it?: ")

        if is_ok:
            with open("data.txt", "a") as data_field:
                data_field.write(f"{website} | {email} | {password} \n")
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)



# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Canvas for logo
canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=0, columnspan=3)

# Labels
website_label = Label(text="Website:")
website_label.grid(row=1, column=0, pady=5, sticky="e")
email_label = Label(text="Email/Username:")
email_label.grid(row=2, column=0, pady=5, sticky="e")
password_label = Label(text="Password:")
password_label.grid(row=3, column=0, pady=5, sticky="e")

# Entry fields
website_entry = Entry(width=40)
website_entry.grid(row=1, column=1, columnspan=2, pady=5, sticky="w")
website_entry.focus()

email_entry = Entry(width=40)
email_entry.grid(row=2, column=1, columnspan=2, pady=5, sticky="w")
email_entry.insert(0,"abc@gmail.com")

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1, pady=5, sticky="w")

# Buttons
generate_password_button = Button(text="Generate Password", width=15, command = generate_password)
generate_password_button.grid(row=3, column=2, padx=5)

add_button = Button(text="Add", width=34, command=save)
add_button.grid(row=4, column=1, columnspan=2, pady=10)

# Run the main loop
window.mainloop()
