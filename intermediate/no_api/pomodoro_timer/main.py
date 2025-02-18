from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
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
def start_timer():
    global reps
    reps += 1
    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN* 60
    work_sec = 10
    short_break_sec = 5
    long_break_sec = 10

    if reps % 8 == 0:
        label_title.config(text="Break",fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        label_title.config(text="Break", fg=PINK)
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
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

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