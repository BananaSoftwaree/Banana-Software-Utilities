from tkinter import *
from tkinter import ttk
import random
from abc import ABC
import datetime

top = Tk()
top.geometry("320x150")
top.iconbitmap('Windows 95.ico')
top.title('Windows 95 Key Generator')
top.resizable(width=False, height=False)

class KeyGenerator(ABC):
    @staticmethod
    def num_digits(num):
        ct = 0
        while num > 0:
            ct += 1
            num //= 10
        return ct

    @staticmethod
    def sum_of_digits(num):
        sm = 0
        while num > 0:
            rem = num % 10
            sm += rem
            num //= 10
        return sm

def buttonClick():
    doy = random.randint(1, 367)
    length = KeyGenerator.num_digits(doy)
    doystring = ""
    for i in range(0, 3 - length):
        doystring += "0"
    doystring += str(doy)
    ystring = random.choice(["95", "96", "97", "98", "99", "00", "01", "02", "03"])
    x2 = 1
    x2str = "0"
    while KeyGenerator.sum_of_digits(x2) % 7 != 0:
        x2 = random.randint(0, 1000000)
        while x2 % 10 == 0 or x2 % 10 == 8 or x2 % 10 == 9:
            x2 = random.randint(0, 1000000)
    length = KeyGenerator.num_digits(x2)
    for i in range(0, 6 - length):
        x2str += "0"
    x2str += str(x2)
    x3 = random.randint(0, 100000)
    x3str = ""
    for i in range(0, 5 - length):
        x3str += "0"
    x3str += str(x3)

    key = f'{doystring}{ystring}-OEM-{x2str}-{x3str}'
    keylabel = ttk.Label(top, text=f'Key: {key}').place(x = 70, y = 57.5)

title = ttk.Label(top, text='Windows 95 Key Generator').place(x = 85, y = 10)
creator = ttk.Label(top, text='Creator: Banana Software').place(x = 87.5, y = 30)
keylabel = ttk.Label(top, text='Press \'Generate\' to generate key!').place(x = 70, y = 57.5)
genbutton = ttk.Button(top, text = " Generate ", command=buttonClick).place(x = 70, y = 87.5)
exit_button = ttk.Button(top, text="     Exit     ", command=top.destroy).place(x = 165, y = 87.5)
now = datetime.datetime.now()
keylabel = ttk.Label(top, text=f'Version 1.1 - Copyright © {now.year} by Banana Software™').place(x = 20, y = 125)
top.mainloop()