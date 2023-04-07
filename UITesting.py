from tkinter import simpledialog
from tkinter import *
import tkinter as tk

root = tk.Tk()
root.title("Movie Recommender")
root.geometry('1200x700')
# title of the UI
title = Label(root, text="Personalized Movie Recommender",
              bg="lightblue", font=('Helvetica', 30), justify="center", anchor="n")
title.pack(fill=tk.X)
# title.grid(column=500, row=1)
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
    # the input dialog

    genre_input = simpledialog.askstring(
        "Genre", "What is your favorite Genre?:")
    genre.config(text=genre_input)

    quest1_button.destroy()


genre = tk.Label(root, text="1)", bg="lightblue",
                 anchor="w", font=('Helvetica', 15))
genre.pack(side="left", padx=20, pady=0)

# changes backgound color
root.configure(bg='lightblue')

# btn = Button(root, text="blank", fg="white",
#              bg="red", command=clicked, width=15, height=2)
# btn.pack()

# ask user for input
quest1_button = Button(root, text="Begin", fg="white", bg="orange",
                       command=question1, width=15, height=2)
quest1_button.pack()


# User input results
# input_data = Label(root, text=genre,
#                    bg="lightblue", font=('Times', 12))
# input_data.pack()
root.mainloop()
