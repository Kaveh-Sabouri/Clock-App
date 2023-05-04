# Kaveh Sabouri

from tkinter import *
from time import strftime

window = Tk()
window.title("Clock App")
window.geometry("500x500")
window.resizable(False,False)
window.config(bg="#00ADB5")

def clock():
    string = strftime('%H:%M:%S %p')
    lbl_clock.config(text=string)
    lbl_clock.after(1000, clock)


lbl_clock = Label(window, font=("",45, "bold"),fg="#EEEEEE",bg="#00ADB5")
lbl_clock.place(x=105,y=205)

clock()

window.mainloop()