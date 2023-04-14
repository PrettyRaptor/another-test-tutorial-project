from tkinter import *
from itertools import cycle

# setting Tk object
window = Tk()
window.geometry('420x420')
window.title('gui-testing')

# create special icon object from png pic
# then set created icon object as window logo
icon = PhotoImage(file='logo.png')
window.iconphoto(True, icon)

label = Label(window)
label.config(text='опа')
label.place(x=0, y=0)

window.mainloop()