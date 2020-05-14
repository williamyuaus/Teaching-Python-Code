import turtle

BACKGROUND_COLOR = "#9EC388"
CRUST_COLOR = "#ECA84F"
SAUCE_COLOR = "#AD0509"
CHEESE_COLOR = "#FBC70F"
PINEAPPLE_COLOR = "#FFEC89"
HAM_COLOR = "#EEA5A7"
HAM_LOCATIONS = [
    [-70, 105],
    [-85, 175],
    [-25, 50],
    [-15, 100],
    [-25, 160],
    [-30, 205],
    [15, 50],
    [20, 200],
    [60, 156],
    [71, 215],
    [80, 90],
    [95, 150],
    [40, 240],
    [45, 130]
    
]

PINEAPPLE_LOCATIONS = [
    [-60, 220],
    [42, 68],
    [-20, 80],
    [-50, 80],
    [0, 240],
    [-80, 140],
    [80, 125],
    [50,150],
    [-40, 175],
    [10, 90],
    [40, 180]
    
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

def draw_pineapple(base, length, line_color, fill_color):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.forward(base)
    my_turtle.right(100)
    my_turtle.forward(length)
    my_turtle.right(150)
    my_turtle.forward(length)
    my_turtle.end_fill()

def draw_ham(length, turn, line_color, fill_color, width):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.pensize(width)
    my_turtle.begin_fill()
    my_turtle.forward(length)
    my_turtle.right(turn)
    my_turtle.end_fill()


def move_turtle(x,y):
    my_turtle.up()
    my_turtle.goto(x,y)
    my_turtle.down()

draw_circle(150, CRUST_COLOR, CRUST_COLOR)
move_turtle(0,25)
draw_circle(125, SAUCE_COLOR, CHEESE_COLOR)

for location in HAM_LOCATIONS:
    move_turtle(location[0], location[1])
    draw_ham(20, 90, HAM_COLOR, HAM_COLOR, 10)

for location in PINEAPPLE_LOCATIONS:
    move_turtle(location[0], location[1])
    draw_pineapple(12, 25, PINEAPPLE_COLOR, PINEAPPLE_COLOR)

move_turtle(0, 150)
my_turtle.color(BACKGROUND_COLOR)

my_turtle.left(95)

for x in range(0,8):
    my_turtle.forward(150)
    my_turtle.back(150)
    my_turtle.left(45)

#FFEC89
#EEA5A7
