# Masande Gontyeleni____Class=3
from tkinter import *
from tkinter import messagebox


def create_gui():
    root = Tk()
    root.geometry("500x200")
    root.title("Ecception form")
    root.configure(bg="orange")

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

    def in_or_out():
        age = int(entry3.get())
        if age < 18:
            messagebox.showinfo("SORRY", "persons under the age of 18 don't qualify")
        if age >= 18:
            messagebox.showinfo("Congratulations!!!!", "Please click continue button to play")

    btn = Button(root, text="enter", command=in_or_out)
    btn.grid(row=4, column=1)

    def new_window():
        from random import randint

        new = Tk()
        new.title("lotto app")
        new.geometry('600x500')
        new.configure(bg="yellow")

        my_var1 = IntVar()
        my_var2 = IntVar()
        my_var3 = IntVar()
        my_var4 = IntVar()
        my_var5 = IntVar()
        my_var6 = IntVar()

        randoya = randint(0, 49)
        randoy = randint(0, 49)
        rando = randint(0, 49)
        rand = randint(0, 49)
        ran = randint(0, 49)
        ra = randint(0, 49)

        my_var1.set(randoya)
        my_var2.set(randoy)
        my_var3.set(rando)
        my_var4.set(rand)
        my_var5.set(ran)
        my_var6.set(ra)

        my_list = [randoya, randoy, rando, rand, ran, ra]
        my_list2 = []

        def pick():

            winnerlabel = Label(new, text=randoya, font=("Helvetica", 24), textvariable=my_var1)
            winnerlabel.grid(row=7, column=1)
            win = Label(new, text=randoy, font=("Helvetica", 24), textvariable=my_var2)
            win.grid(row=8, column=1)
            wind = Label(new, text=rando, font=("Helvetica", 24), textvariable=my_var3)
            wind.grid(row=9, column=1)
            wink = Label(new, text=rand, font=("Helvetica", 24), textvariable=my_var4)
            wink.grid(row=10, column=1)
            winc = Label(new, text=ran, font=("Helvetica", 24), textvariable=my_var5)
            winc.grid(row=11, column=1)
            winf = Label(new, text=ra, font=("Helvetica", 24), textvariable=my_var6)
            winf.grid(row=12, column=1)

        winbutton = Button(new, text="PLAY LOTTO PLUS", font=("Helvetica", 24), command=pick)
        winbutton.grid(row=3, column=1)

        label = Label(new, text="Please enter your numbers")
        label.grid(row=6, column=0)
        ntry1 = Entry(new, bd=20, width="5")
        ntry1.grid(row=6, column=1)
        ntry2 = Entry(new, bd=20, width="5")
        ntry2.grid(row=6, column=2)
        ntry3 = Entry(new, bd=20, width="5")
        ntry3.grid(row=6, column=3)
        ntry4 = Entry(new, bd=20, width="5")
        ntry4.grid(row=6, column=4)
        ntry5 = Entry(new, bd=20, width="5")
        ntry5.grid(row=6, column=5)
        ntry6 = Entry(new, bd=20, width="5")
        ntry6.grid(row=6, column=6)

        def enter_numbers():
            def make_list():
                my_list2.append(ntry1.get())
                my_list2.append(ntry2.get())
                my_list2.append(ntry3.get())
                my_list2.append(ntry4.get())
                my_list2.append(ntry5.get())
                my_list2.append(ntry6.get())

                print(my_list2)
                print(my_list)
            make_list()

            numbers = set(my_list2).intersection(set(my_list))
            print(numbers)
            didn_win = Label(new, text="Sorry you didn't win", font=("Helvetica", 24))
            didn_win.grid(row=14, column=1)

            if len(numbers) == 6:
                didn_win.config(text="Congrats you got  reward=R10,000,000.00")
            if len(numbers) == 5:
                didn_win.config(text="Congrats you got one reward=R8,584,00")
            if len(numbers) == 4:
                didn_win.config(text="Congrats you got one reward=R2,384.00")
            if len(numbers) == 3:
                didn_win.config(text="Congrats you got one reward=R100.50")
            if len(numbers) == 2:
                didn_win.config(text="Congrats you got one reward=R20.00")
            if len(numbers) == 1:
                didn_win.config(text="Unfortunately you won nothing")
            if len(numbers) == 0:
                didn_win.config(text="unfortunately you won nothing")

            file = open("hey.txt", "w+")
            file.write(entry1.get())
            for line in entry2.get():
                file.write(line + "/n")
            for line in entry3.get():
                file.write(line + "/n")
            for line in ntry1.get():
                file.write(line + "/n")
            for line in ntry2.get():
                file.write(line + "/n")
            for line in ntry3.get():
                file.write(line + "/n")
            for line in ntry4.get():
                file.write(line + "/n")
            for line in ntry5.get():
                file.write(line + "/n")
            for line in ntry6.get():
                file.write(line + "/n")
            file.close()

        toplabel = Label(new, text="Win", font=("Helvetica", 24))
        toplabel.grid(row=1, column=1)

        b = Button(new, text="check result", command=enter_numbers)
        b.grid(row=9, column=0)
    btn1 = Button(root, text="CONTINUE", command=new_window)
    btn1.grid(row=5, column=1)

    root.mainloop()

    root.mainloop()


create_gui()
