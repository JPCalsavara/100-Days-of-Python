#tkinter use
#First GUI used in the mac Lisa and windows 95

import tkinter


window = tkinter.Tk()
window.title("My First GUI program from Xerox")
window.minsize(width=500,height=300)

#Label

label = tkinter.Label(text="I am blue",font=("Arial",24,"bold"))
label.pack(side="bottom")








window.mainloop()