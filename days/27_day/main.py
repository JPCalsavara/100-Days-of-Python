#tkinter use
#First GUI used in the mac Lisa and windows 95

from tkinter import *
import random

#3 ways to position items
# 1-pack(bottom,top,right,left) - but is to not precise
# 2- place(x,y) - but is to precise
# 3 - grid(column, row)

window = Tk()
window.title("My First GUI program from Xerox")
window.minsize(width=500,height=300)
window.config(padx=50,pady=50)

#Label

label = Label(text="I am blue",font=("Arial",24,"bold"))
label.pack()
label.grid(column=0,row=0)

#Button

def button_click():
    # word_list = ["Blue","Yellow","Love", "American Idiot"]
    # word = random.choice(word_list)
    word = input.get()
    # label["text"] = f"I am the {word}"
    label.config(text=f"I am the {word}")

button = Button(text="Don´t Click", command=button_click)
button.grid(column=1,row=1)

button2 = Button(text="Don´t Click too", command=button_click)
button2.grid(column=2,row=0)

#Entry

input = Entry()
input.grid(column=3,row=2)









window.mainloop()