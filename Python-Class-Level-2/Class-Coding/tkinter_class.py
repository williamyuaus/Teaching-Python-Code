from tkinter import Canvas,Tk
import time

tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)

def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(1, 0, -3)


canvas.bind_all('<KeyPress-Up>', movetriangle)
