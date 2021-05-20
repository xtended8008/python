from tkinter import *
from datetime import datetime
import pytz
import time

root = Tk()

eastern = pytz.timezone('US/Eastern')
sa = pytz.timezone('Africa/Johannesburg')

def counter():
    global my_text
    starttime = time.time()

    ea_now = datetime.now(eastern)
    sa_now = datetime.now(sa)
    my_text = "Time in NY: %s \nTime in Johannesburg: %s" % (ea_now.strftime('%H:%M:%S'),sa_now.strftime('%H:%M:%S'))
    my_label.config(text = my_text)
    root.after(1000, counter)

my_button = Button(root,
                   text = "PRESS HERE",
                   command = counter)
my_label = Label(root,
                text = "Press button to get time")
my_label.pack()
my_button.pack()
root.mainloop()
