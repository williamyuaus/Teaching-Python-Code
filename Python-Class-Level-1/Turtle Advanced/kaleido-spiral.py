import turtle

from itertools import cycle

colors = cycle(['red', 'orange', 'yellow', 'green', 'blue', 'purple'])
#set background color
# turtle.bgcolor('black')

#set turtle's speed
# turtle.speed('fast')

#set the thinkness of the turtle's trail
# turtle.pensize(4)

#set pen color
# turtle.pencolor('red')

#tell the turtle to draw a circle
# turtle.circle(30)

def draw_circle(size, angle, shift):
    turtle.pencolor((next(colors)))
    turtle.circle(size)
    turtle.right(angle)
    turtle.forward(shift)
    draw_circle(size + 5, angle + 1, shift + 1)

turtle.bgcolor('black')
turtle.speed('fast')
turtle.pensize(4)
draw_circle(30, 0, 1)


