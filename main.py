from tkinter import *


def calculate():
    Km_val.config(text=round((float(entry_mile.get())*1.609),3))

# Screen
window=Tk()
window.title("Mile to Km Convertor")
window.minsize(width=300,height=100)

# Label
miles=Label(text="Miles")
Km=Label(text="Km")
Km_val=Label(text=0)

equal=Label(text="is equal to")
miles.grid(row=1,column=3)
Km.grid(row=2,column=3)
equal.grid(row=2,column=1)
Km_val.grid(row=2,column=2)

#button
button=Button(text="Calculate",width=20,command=calculate)
button.grid(row=3,column=2)

#entry
entry_mile = Entry(width=20)

entry_mile.grid(row=1,column=2)







window.mainloop()