#Masande Gontyeleni____Class=3
from tkinter import *



def create_GUI():
    root = Tk()
    root.geometry("800x500")
    root.title("Ecception form")

    ntry3 = IntVar()

    label1 = Label(text="please enter your name and surname :")
    label1.grid(row=1, column=0)

    entry1 = Entry(root)
    entry1.grid(row=1, column=1)

    label2 = Label(text="Please enter nationality:")
    label2.grid(row=2, column=0)

    entry2 = Entry(root)
    entry2.grid(row=2, column=1)

    label3 = Label(text="Please enter your age :")
    label3.grid(row=3, column=0)

    entry3 = Entry(root, textvariable=ntry3)
    entry3.grid(row=3, column=1)

    root.mainloop()


create_GUI()
