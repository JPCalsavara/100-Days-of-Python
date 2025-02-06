BACKGROUND_COLOR = "#B1DDC6"
FONT_NAME = "Ariel"

from tkinter import *
import pandas as pd
import random
all_words = {}
current_card = {}

try:
    df_all_words=pd.read_csv("data/words_to_learn.csv.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    all_words = original_data.to_dict(orient="records")
else:
    all_words = df_all_words.to_dict(orient="records")


# ---------------------------- Create New Flash Cards - French ------------------------------- #
def is_known():
    """Select the words that you have known from the list"""
    all_words.remove(current_card)
    data = pd.DataFrame(all_words)
    data.to_csv("data/words_to_learn.csv",index=False)
    next_card()

# ---------------------------- Create New Flash Cards - French ------------------------------- #
def next_card():
    global current_card,flip_timer
    #Every time you click to another card, it restarts cause use window after
    window.after_cancel(flip_timer)
    current_card = random.choice(all_words)
    french_word_text = current_card["French"]

    canvas_card.itemconfig(card_title, text="French",fill="black")
    canvas_card.itemconfig(card_text, text=f"{french_word_text}",fill="black")

    canvas_card.itemconfig(canvas_image, image=front_image)
    flip_timer=window.after(3000, func=flip_card)
# ---------------------------- Change New Flash Cards - English ------------------------------- #
def flip_card():
    global current_card
    english_word_text = current_card["English"]
    canvas_card.itemconfig(card_title, text="English",fill="white")
    canvas_card.itemconfig(card_text, text=f"{english_word_text}",fill="white")
    canvas_card.itemconfig(canvas_image, image=back_image)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50,pady=50,bg=BACKGROUND_COLOR)

#Wait 3 seconds to execute the function
flip_timer = window.after(3000,func=flip_card)

#Canvas

#Cards
canvas_card = Canvas(width=800,height=526,highlightthickness=0,bg=BACKGROUND_COLOR)

front_image = PhotoImage(file="images/card_front.png")
back_image = PhotoImage(file="images/card_back.png")

canvas_image = canvas_card.create_image(400,263,image=front_image)

card_title = canvas_card.create_text(400,150,text="French",fill="black",font=(FONT_NAME,40,"italic"))
card_text = canvas_card.create_text(400,263,text="word",fill="black",font=(FONT_NAME,60,"bold"))

canvas_card.grid(column=0,row=0,columnspan=2)

#Right or wrong
#Right

right_image = PhotoImage(file="images/right.png")

button_right = Button(image=right_image,highlightthickness=0,command=is_known)


button_right.grid(column=1,row=1,columnspan=1)

#Wrong

wrong_image = PhotoImage(file="images/wrong.png")

button_wrong = Button(image=wrong_image,highlightthickness=0,command=next_card)

button_wrong.grid(column=0,row=1,columnspan=1)

next_card()


window.mainloop()

