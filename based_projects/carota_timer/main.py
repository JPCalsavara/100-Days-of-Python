from tkinter import *
import math
from PIL import Image,ImageTk
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
work_min = 25
short_break_min = 5
long_break_min = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    label_title.config(text="Timer", fg=GREEN)
    label_counter.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- #
def work_time_changer():
    work_time_value = work_time.get()
    if work_time_value == 1:
        global work_min
        work_min = 25
    elif work_time_value == 2:
        global work_min
        work_min = 35
    elif work_time_value == 3:
        global work_min
        work_min = 50

def short_break_changer():
    work_time_value = work_time.get()
    if work_time_value == 1:
        global work_min
        work_min = 5
    elif work_time_value == 2:
        global work_min
        work_min = 7
    elif work_time_value == 3:
        global work_min
        work_min = 10






def start_timer():
    global reps
    global work_min
    global short_break_min
    global long_break_min
    reps += 1
    work_sec = work_min * 60
    short_break_sec = short_break_min * 60
    long_break_sec = long_break_min* 60

    if reps % 8 == 0:
        label_title.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_title.config(text="Short Break", fg=PINK)
        count_down(short_break_sec)
    else:
        label_title.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000,count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            work_sessions = math.floor(reps/2)
            checkmark = "✔"
            mark = ""
            for _ in range(work_sessions):
                mark += checkmark

            label_counter.config(text=mark, fg=GREEN, font=(FONT_NAME, 20, "bold"), bg=YELLOW)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Carota")
window.config(padx=75,pady=30,bg=YELLOW)

menubar = Menu()

settings_menu = Menu(menubar,tearoff=False)

work_time_menu = Menu(menubar,tearoff=False)
work_time = IntVar()
work_time.set(1)
work_time_menu.add_radiobutton(
    label="25 min",
    variable= work_time,
    value=1,
    command=work_time_changer

)
work_time_menu.add_radiobutton(
    label="35 min",
    variable= work_time,
    value=2,
    command=work_time_changer

)
work_time_menu.add_radiobutton(
    label="50 min",
    variable= work_time,
    value=3,
    command=work_time_changer

)

short_break_menu = Menu(menubar,tearoff=False)
short_break = IntVar()
short_break.set(1)
short_break_menu.add_radiobutton(
    label="5 min",
    variable= work_time,
    value=1,
    command=short_break_changer

)
short_break_menu.add_radiobutton(
    label="7 min",
    variable= work_time,
    value=2,
    command=short_break_changer

)
short_break_menu.add_radiobutton(
    label="20 min",
    variable= work_time,
    value=3,
    command=short_break_changer

)

settings_menu.add_cascade(menu=work_time_menu, label="Work Time")
settings_menu.add_cascade(menu=short_break_menu, label="Short Time")
settings_menu.add_cascade(menu=work_time_menu, label="Long Time")
menubar.add_cascade(menu=work_time_menu, label="Settings")

#Label title
label_title = Label(text="Timer",fg=GREEN,font=(FONT_NAME,50,"bold"),bg=YELLOW)
label_title.grid(column=1,row=0)

#To import and show an image

#Canvas is the class used and needed to be initialized with the width and height of the image
canvas = Canvas(width=250,height=250,bg=YELLOW,highlightthickness=0)

#PhotoImage is used to import the image to put in a canvas
img = Image.open("carota2.png")
resized_image = img.resize((380,380))
new_image = ImageTk.PhotoImage(resized_image, Image.Resampling.LANCZOS)


#Put the image inside the canvas
canvas.create_image(105,130,image=new_image)

#Put text in the image
timer_text=canvas.create_text(120,125,text="00:00",fill="white",font=(FONT_NAME,33,"bold"))

#Put in the canvas in the interface
canvas.grid(column=1,row=1)


#Button to start
button_start = Button(text="Start",highlightthickness=0, command=start_timer )
button_start.grid(column=0,row=3)

#Button to reset
button_reset = Button(text="Reset",highlightthickness=0,command=reset_timer )
button_reset.grid(column=2,row=3)

#Timer counter
label_counter = Label(fg=GREEN,bg=YELLOW)
label_counter.grid(column=1,row=4)


window.mainloop()