from tkinter import simpledialog
from tkinter import *
import tkinter as tk
root = Tk()
root.title("Movie Recommender")
root.geometry('350x200')
# title of the UI
title = Label(root, text="Personalized Movie Recommender", bg="lightblue")
title.grid()

# creating a commmened for when button is clicked

# command for when btn gets clicked


def clicked():
    btn['state'] = 'disabled'
    btn['text'] = 'blank'
    btn['bg'] = 'white'
    lbl2 = Label(root, text="Test Label")
    lbl2.grid()

# will take user input when button is clicked


def question1():
    root.withdraw()
    # the input dialog
    name = simpledialog.askstring(
        title="Test", prompt="What's your Name?:")


# changes backgound color
root.configure(bg='lightblue')

btn = Button(root, text="blank", fg="white", bg="red", command=clicked)
btn.grid(column=1, row=0)

# ask user for input
quest1 = Button(root, text="input", fg="white", bg="orange", command=question1)
quest1.grid(column=4, row=0)


root.mainloop()
