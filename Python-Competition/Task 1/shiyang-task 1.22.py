import turtle
hi = turtle.Turtle()
hi.pensize(10)
Colors1 = ["blue", "black", "red"] 
for i in range(3):
  hi.penup()
  hi.pencolor(Colors1[i])
  hi.goto(i*110, 0)
  hi.pendown()
  hi.circle(50)
Colors2 = ["", "yellow", "", "green"]
for i in range(1, 4, 2):
  hi.penup()
  hi.pencolor(Colors2[i])
  hi.goto(i*55, -50)
  hi.pendown()
  hi.circle(50)
