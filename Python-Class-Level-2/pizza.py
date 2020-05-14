import turtle

BACKGROUND_COLOR = "#9EC388"
CRUST_COLOR = "#ECA84F"
SAUCE_COLOR = "#AD0509"
PINEAPPLE_COLOR = "#FFEC89"
CHEESE_COLOR = "#FBC70F"
PEPPERONI_LOCATIONS = [
    [-70, 105],
    [-85, 175],
    [-25, 50],
    [-15, 100],
    [-25, 150],
    [-30, 205],
    [15, 50],
    [20, 200],
    [60, 156],
    [71, 215],
    [80, 90],
    [95, 150]
]

screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("My Pizza")

my_turtle = turtle.Turtle()
my_turtle.pensize(5)
my_turtle.shape("circle")

def draw_circle(radius, line_color, fill_color):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

def move_turtle(x, y):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down()

def draw_rectangle(x, y, width, height):
  turtle.up()
  turtle.goto(x, y)
  turtle.down()
  turtle.forward(width)          
  turtle.left(90)
  turtle.forward(height)
  turtle.left(90)
  turtle.forward(width)
  turtle.left(90)
  turtle.forward(height)
  turtle.left(90)

draw_circle(150, CRUST_COLOR, CRUST_COLOR)
move_turtle(0, 25)
draw_circle(125, SAUCE_COLOR, CHEESE_COLOR)

for location in PEPPERONI_LOCATIONS:
    move_turtle(location[0], location[1])
    draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
    # draw_rectangle(-70, 105, 10, 10)

move_turtle(0, 150)
my_turtle.color(BACKGROUND_COLOR)

for x in range(0, 8):
    my_turtle.pendown()
    my_turtle.left(45)
    my_turtle.forward(150)
    my_turtle.penup()
    my_turtle.backward(150)

turtle.done()