from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #
# def start_pomodoro():
#

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#Label title
label_title = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
label_title.grid(column=1,row=0)

#To import and show an image

#Canvas is the class used and needed to be initialized with the width and height of the image
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)

#PhotoImage is used to import the image to put in a canvas
tomato_img = PhotoImage(file="tomato.png")

#Put the image inside the canvas
canvas.create_image(100,112,image=tomato_img)

#Put text in the image
canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

#Put in the canvas in the interface
canvas.grid(column=1,row=1)


#Button to start
button_start = Button(text="Start",highlightthickness=0 )
button_start.grid(column=0,row=3)

#Button to reset
button_reset = Button(text="Reset",highlightthickness=0 )
button_reset.grid(column=2,row=3)

#Timer counter
label_counter = Label(text="✔",fg=GREEN,font=(FONT_NAME,20,"bold"),bg=YELLOW)
label_counter.grid(column=1,row=4)


window.mainloop()