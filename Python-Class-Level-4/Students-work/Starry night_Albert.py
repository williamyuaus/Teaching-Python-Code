import turtle
import random
turtle.Screen().bgcolor('dark blue')

t = turtle.Turtle()
colors = ['red', 'purple', 'blue', 'yellow', 'green', 'orange']

def draw_star(line_color, fill_color):
    t.color(line_color)
    t.fillcolor(fill_color)
    t.begin_fill()
    t.forward(20)
    t.left(76)
    t.forward(20)
    t.right(152)
    t.forward(20)
    t.left(76)
    t.forward(20)
    t.right(152)
    t.forward(20)
    t.left(76)
    t.forward(20)
    t.right(152)
    t.forward(20)
    t.left(92)
    t.forward(20)
    t.right(152)
    t.forward(20)
    t.left(76)
    t.forward(20)
    t.end_fill()

def move_turtle(x, y):
    t.up()
    t.goto(x, y)
    t.down()



number_Stars = random.randint(10, 20)

while number_Stars > 0:
    draw_star(random.choice(colors), random.choice(colors))
    move_turtle(random.randint(-500, 500), random.randint(-300,300))
    number_Stars = number_Stars - 1
    
