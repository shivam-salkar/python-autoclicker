'''
python version: 3.9.1
tkinter version: 8.6
code is on github: github.com/sCube2428/python-projects/tkinter-autoclicker.py
'''

from tkinter import *
import pyautogui
from time import sleep

def auto_click():
    sleep(3)
    clicks = int(no_of_clicks_to_make.get())
    for i in range(clicks):
        pyautogui.click(pyautogui.position())


root = Tk()
root.geometry('360x180')
root.resizable(False, False)
root.title('AutoClicker | Python | Tkinter')

Label(root, text='AutoClicker', font='ubuntu 26 bold', pady=10, padx=70).pack()
Label(root, text='How many clicks do u want? ', pady=1, padx=70, font='ubuntu 12').pack()
no_of_clicks_to_make = StringVar()

e = Entry(root, textvariable=no_of_clicks_to_make).pack()
b = Button(root, text='Start Clicking!', command=auto_click).pack(pady=10, padx=10)

root.mainloop()
