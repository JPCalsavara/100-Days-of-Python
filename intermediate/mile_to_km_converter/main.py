from tkinter import *

window = Tk()
window.title("Miles to Km Converter")
# window.minsize(width=300,height=200)
window.config(padx=20,pady=20)

def mile_to_km():
    miles = float(mile_input.get())
    km = round(miles * 1.609)
    label_result.config(text=f"{km}")


# Input Miles
mile_input = Entry(width=10)
mile_input.insert(END, string="0")
mile_input.grid(column=1,row=0)

#Labels
label_miles = Label(text="Miles")
label_miles.config(text="Miles")
label_miles.grid(column=2,row=0)

label_Km = Label(text="Km")
label_Km.config(text="Km")
label_Km.grid(column=2,row=1)

label_text = Label(text="is equal to")
label_text.config(text="is equal to")
label_text.grid(column=0,row=1)

#Button
button = Button(text="Calculate",command=mile_to_km)
button.grid(column=1,row=2)

#Result
label_result = Label(text="0")
label_result.config(text="0")
label_result.grid(column=1,row=1)

window.mainloop()