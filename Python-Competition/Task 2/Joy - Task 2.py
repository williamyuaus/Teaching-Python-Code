import turtle
t=turtle.Pen()
t.color('blue')
t.begin_fill()
t.forward(100)
t.left(90)
t.forward(20)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(60)
t.left(90)
t.forward(20)
t.right(90)
t.forward(20)
t.left(90)
t.forward(20)
t.end_fill()
t.color('black')
t.up()
t.forward(10)
t.down()
t.begin_fill()
t.circle(10)
t.end_fill()
t.setheading(0)
t.up()
t.forward(90)
t.right(90)
t.forward(10)
t.setheading(0)
t.begin_fill()
t.circle(10)
t.end_fill()
t.penup()
t.goto(50,100)
t.pendown()
t.pensize(5)
t.color('blue')
t.begin_fill()
t.circle(60)
t.end_fill()
t.right(90)
t.forward(100)
t.hideturtle()
turtle.mainloop()