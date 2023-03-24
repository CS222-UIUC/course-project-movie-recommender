from tkinter import *
root = Tk()
root.title("welcome")
root.geometry('350x200')
lbl = Label(root, text="random")
lbl.grid()


def clicked():
    btn['state'] = 'disabled'
    btn['text'] = 'blank'
    btn['bg'] = 'white'
    lbl2 = Label(root, text="Random")
    lbl2.grid()


btn = Button(root, text="blank", fg="white", bg="red", command=clicked)
btn.grid(column=1, row=0)
root.mainloop()
