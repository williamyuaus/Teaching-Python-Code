import time
from tkinter import Canvas,Tk

tk = Tk()
canvas = Canvas(tk, width=400, height=200)
canvas.pack()
canvas.create_polygon(10, 10, 10, 60, 50, 35)
canvas.create_polygon(100, 100, 100, 120, 150, 135)
for x in range(0, 60):
   canvas.move(2, 5, 0)
   tk.update()
   time.sleep(0.1)
