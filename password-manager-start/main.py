#Learned attributes and functions
#.grid(rowspan=) to make an object fill two or more columns
#.focus() to make the cursor starts in the object
#.insert(index of the start of the data in the array, string inserted)
#.delete(index of the start of the data in the array, last character like END)
#pyperclip.clip to copy a string

from tkinter import *
from tkinter import messagebox
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  from random import choice, randint,shuffle
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  password_list = password_letters+password_symbols+password_numbers

  shuffle(password_list)

  password = "".join(password_list)

  entry_password.insert(0,password)
  pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    website = entry_website.get().title()
    email_username = entry_email.get()
    password = entry_password.get()

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Don't leave any field empty!!!")
        is_ok = False
    else:
        is_ok = messagebox.askokcancel(title="website",message=f"These are the data inserted:"
                                                      f"\nEmail:{email_username}"
                                                      f"\nPassword:{password}"
                                                      f"\nIs it ok to save?")


    if is_ok:
        with open("data.txt","a") as data:
            data.write(f"{website} | {email_username} | {password}\n")

        entry_website.delete(0,END)
        entry_password.delete(0, END)
        entry_website.focus()


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=60,pady=60)

#Import and put image in the UI with canvas
canvas = Canvas(width=200,height=200,highlightthickness=0)

logo_img = PhotoImage(file="logo.png")

canvas.create_image(100,100,image=logo_img)

canvas.grid(column=1,row=0)

#Labels

label_website = Label(text="Website:")
label_website.grid(column=0,row=1)

label_email = Label(text="Email/Username:")
label_email.grid(column=0,row=2)

label_password = Label(text="Password:")
label_password.grid(column=0,row=3)

#Entries
entry_website =  Entry(width=50)
entry_website.grid(column=1,row=1,columnspan=2)
entry_website.focus()

entry_email =    Entry(width=50)
entry_email.grid(column=1,row=2,columnspan=2)
entry_email.insert(0,"jpcalsavara@gmail.com")

entry_password = Entry(width=32)
entry_password.grid(column=1,row=3)

#Buttons
button_generate_password = Button(text="Generate Password",command=generate_password)
button_generate_password.grid(column=2,row=3)

button_add_password = Button(text="Add Password",width=43,command=save_password)
button_add_password.grid(column=1,row=4,columnspan=3)


window.mainloop()