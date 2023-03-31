from tkinter import *
import tkinter as tk
root = Tk()
root.title("Movie Recommender")
root.geometry('350x200')
lbl = Label(root, text="Personalized Movie Recommender")
lbl.grid()

# creating a commmened for when button is clicked


def clicked():
    btn['state'] = 'disabled'
    btn['text'] = 'blank'
    btn['bg'] = 'white'
    lbl2 = Label(root, text="Test Label")
    lbl2.grid()


# changes backgound color
root.configure(bg='lightblue')

btn = Button(root, text="blank", fg="white", bg="red", command=clicked)
btn.grid(column=1, row=0)
root.mainloop()
