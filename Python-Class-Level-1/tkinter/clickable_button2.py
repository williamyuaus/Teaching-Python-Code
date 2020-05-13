def hello():
    print('hello there')

from tkinter import Tk,Button
tk = Tk()
btn = Button(tk, text="click me", command=hello)
btn.pack()
