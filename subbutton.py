from tkinter import *

root = Tk()

root.title("Subscription App")
root.geometry("400x400")
lbl = Label(root, text="My hacking experience")
lbl.grid()


def clicked():
    btn['state'] = 'disabled'
    btn['text'] = 'Susbcribed'
    btn['bg'] = 'white'
    lbl2 = Label(root, text="you subscribed!")
    lbl2.grid(column=2,row=0)

btn = Button(
    root,
    text = "subscribe",
    fg = "white",
    bg = "red",
    command=clicked
)
btn.grid(column=1,row=0)

root.mainloop()