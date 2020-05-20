from tkinter import Tk,Button

def hello():
    print('hello there')

tk = Tk()
btn = Button(tk, text="click me", command=hello)
btn.pack()
tk.mainloop()