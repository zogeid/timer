import time
from tkinter import *

# creating Tk window
import winsound

root = Tk()

# setting geometry of tk window
root.geometry("300x250")

hour = StringVar()
minute = StringVar()
second = StringVar()

hour.set("00")
minute.set("03")
second.set("00")

# Use of Entry class to take input from the user
hourEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=hour)
hourEntry.place(x=80, y=20)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=minute)
minuteEntry.place(x=130, y=20)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""), textvariable=second)
secondEntry.place(x=180, y=20)

# def bindings(self):
#     self.master.bind('a', lambda event: print("A was pressed"))
#     self.master.bind('<Space>', lambda event: submit())
#     self.frame.bind('<Enter>', lambda event: print("Entered Frame"))


def reset():
    submit(180)


def start():
    submit(0)


def submit(ptemp):
    temp = 0

    try:
        # the input
        if ptemp == 0:
            temp = int(hour.get()) * 3600 + int(minute.get()) * 60 + int(second.get())

        # bindings()

    except Exception as excep:
        print(type(excep))  # the exception instance
        print(excep.args)  # arguments stored in .args
        print(excep)
        print("Please input the right value")

    while temp > -1:

        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours, mins ,secs
        hours = 0
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue = temp%60)
            hours, mins = divmod(mins, 60)

        # using format () method to store the value up to two decimal places
        hour.set("{0:2d}".format(hours))
        minute.set("{0:2d}".format(mins))
        second.set("{0:2d}".format(secs))

        # updating the GUI window after decrementing the temp value every time
        root.update()
        time.sleep(1)

        if temp == 0:
            winsound.Beep(2500, 1000)
            minute.set("03")

        # after every one sec the value of temp will be decremented by one
        temp -= 1

        if ptemp != 0:
            temp = ptemp
            root.quit()


btn = Button(root, text='Set Time Countdown', bd='5', command=start)
btn.place(x=70, y=120)

btn2 = Button(root, text='reSet', bd='5', command=reset)
btn2.place(x=200, y=120)

root.mainloop()
