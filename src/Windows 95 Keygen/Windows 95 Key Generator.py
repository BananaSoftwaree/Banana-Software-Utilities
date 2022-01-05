from tkinter import *
from tkinter import ttk
import random
import datetime

top = Tk()
top.geometry("320x150")
top.iconbitmap('Windows 95.ico')
top.title('Windows 95 Key Generator')
top.resizable(width=False, height=False)

def buttonClick():
	first = str(random.randint(1, 367)).zfill(3) + random.choice(["95", "96", "97", "98", "99", "00", "01", "02", "03"])
	
	second = "0"
	multiple7 = random.choice([i for i in range(7, 55, 7)]) # Only until 54, because the largest digit sum from a 6 digit number is 9+9+9+9+9+9 = 54
															# Also 0 is not included, because the only number whose digit sum is 0 is 0 and it's not allowed
	for i in range(5):
		randomDigit = random.randint(0, 9)
		if randomDigit + sum([int(j) for j in second]) >= multiple7:
			randomDigit -= (randomDigit + sum([int(j) for j in second])) - multiple7 + 1
		elif randomDigit + sum([int(j) for j in second]) + ((4-i)*9 + 7) < multiple7:
			randomDigit += multiple7 - (randomDigit + sum([int(j) for j in second]) + ((4-i)*9 + 7))
		second += str(randomDigit)
	second += str(multiple7 - sum([int(j) for j in second]))
	
	third = str(random.randint(0, 99999)).zfill(5)

	key = f'{first}-OEM-{second}-{third}'
	keylabel = ttk.Label(top, text=f'Key: {key}').place(x = 70, y = 57.5)

title = ttk.Label(top, text='Windows 95 Key Generator').place(x = 85, y = 10)
creator = ttk.Label(top, text='Creator: Banana Software').place(x = 87.5, y = 30)
keylabel = ttk.Label(top, text='Press \'Generate\' to generate key!').place(x = 70, y = 57.5)
genbutton = ttk.Button(top, text = " Generate ", command=buttonClick).place(x = 70, y = 87.5)
exit_button = ttk.Button(top, text="	 Exit	 ", command=top.destroy).place(x = 165, y = 87.5)
now = datetime.datetime.now()
keylabel = ttk.Label(top, text=f'Version 1.11 - Copyright © {now.year} by Banana Software™').place(x = 20, y = 125)
top.mainloop()
