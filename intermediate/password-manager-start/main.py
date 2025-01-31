#Learned attributes and functions
#.grid(rowspan=) to make an object fill two or more columns
#label.focus() to make the cursor starts in the object
#label.insert(index of the start of the data in the array, string inserted)
#label.delete(index of the start of the data in the array, last character like END)
#pyperclip.clip to copy a string

#JSON
#Type of data that organize information like a dictionary
#Main methods
#json.write(dictionary that you want to write, file) to write in the file.json
#json.load(file) - to import a json like a dictionary

import json
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- SEARCH WEBSITE ------------------------------- #
def search_website():
    website = entry_website.get().title()

    if len(website)==0:
        messagebox.showinfo(title="Oops",message="Don´t put the website name")

    else:
        try:
            with open("data.json", "r") as data_file:
                    #Read old data
                    data = json.load(data_file)
        except FileNotFoundError:
            messagebox.showinfo(title="Oops", message="No Data File Found")

        else:
            try:
                website_data = data[website]
            except KeyError:
                messagebox.showinfo(title="Oops", message="No details for the website exits")
            else:
                messagebox.showinfo(title=f"{website}´s password", message=f"Email: {website_data["email"]}\nPassword: {website_data["password"]}\n")


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

    new_data = {
        website:{
            "email": email_username,
            "password":password
        }
    }

    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="Oops",message="Don't leave any field empty!!!")
        is_ok = False
    else:
        try:
            with open("data.json", "r") as data_file:
                    #Read old data
                    data = json.load(data_file)

        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)

        else:
            #Uptading old to new data to continue to be an order dictionary
            data.uptade(new_data)

            with open("data.json", "w") as data_file:
                #Saving updated data
                json.dump(data,data_file,indent=4)

        finally:
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
entry_website =  Entry(width=32)
entry_website.grid(column=1,row=1)
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

button_search_website = Button(text="Search",width=15,command=search_website)
button_search_website.grid(column=2,row=1)


window.mainloop()