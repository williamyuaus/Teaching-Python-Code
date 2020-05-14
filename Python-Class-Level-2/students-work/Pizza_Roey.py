import turtle
t = turtle.Pen()

BACKGROUND_COLOR = "#9EC388"
CRUST_COLOR = "#FF9B69"
SAUCE_COLOR = "#B70000"
CHEESE_COLOR = "#FFEB79"
PEPPERONI_COLOR = "#FF8267"
OLIVE_COLOR = "#000000"
PEPPERONI_LOCATIONS = [
    [-60, 111],
    [-75, 169],
    [-29, 60],
    [-22, 105],
    [-25, 150],
    [-30, 205],
    [15, 50],
    [25, 209],
    [69, 157],
    [79, 225],
    [70, 95],
    [100, 155]
]
OLIVE_LOCATION = [
    [-55, 91],
    [-70, 159],
    [-39, 65],
    [-29, 115],
    [-35, 140],
    [-37, 215],
    [17, 53],
    [24, 194],
    [57, 152],
    [89, 215],
    [71, 97],
    [110, 145]
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
    
draw_circle(150, CRUST_COLOR, CRUST_COLOR)
move_turtle(0,25)
draw_circle(125, SAUCE_COLOR, CHEESE_COLOR)

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


for location in PEPPERONI_LOCATIONS:
    move_turtle(location[0], location[1])
    draw_circle(10, PEPPERONI_COLOR, PEPPERONI_COLOR)

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

for location in OLIVE_LOCATION:
    move_turtle(location[0], location[1])
    draw_circle(5, OLIVE_COLOR, OLIVE_COLOR)
    
move_turtle(0,150)
my_turtle.color(BACKGROUND_COLOR)

for x in range (0,9):
    my_turtle.forward(150)
    my_turtle.backward(300)
    my_turtle.forward(150)
    my_turtle.left(45)
  
