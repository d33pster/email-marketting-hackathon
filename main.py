#!/usr/bin/env python3

from tkinter import *
from modules.menu import generate

def menu():
    global rootwindow
    menucontrol = generate(rootwindow, title='Wikiprospects')
    menucontrol._menu()

if __name__=="__main__":
    rootwindow = Tk()
    menu()
    rootwindow.mainloop()