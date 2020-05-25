import turtle

BACKGROUND_COLOR = '#9EC388'
CRUST_COLOR = "#ECA84F"
SAUCE_COLOR = "#AD0509"
CHEESE_COLOR = "#FBC70F"
BOX_COLOR = "#E8E8E8"
LOGO_COLOR = "#FFA913"

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
    [81, 90],
    [95, 150]
]

screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Pinewood Builders pizza")
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
move_turtle(0, 25)
draw_circle(125, SAUCE_COLOR, CHEESE_COLOR)
move_turtle(-70, 105)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(-85, 175)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(-25, 50)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(-15, 100)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(-25, 150)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(-30, 205)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(15, 50)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(20, 200)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(60, 156)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(71, 215)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(81, 90)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)
move_turtle(95, 150)
draw_circle(10, SAUCE_COLOR, SAUCE_COLOR)

move_turtle(0, 150)
my_turtle.color(BACKGROUND_COLOR)

for x in range(0, 8):
    my_turtle.pendown()
    my_turtle.left(45)
    my_turtle.forward(150)
    my_turtle.penup()
    my_turtle.backward(150)

my_turtle.left(90)
my_turtle.forward(160)
my_turtle.color(BOX_COLOR)
my_turtle.pendown()
my_turtle.begin_fill()
my_turtle.right(90)
my_turtle.forward(160)
my_turtle.right(90)
my_turtle.forward(320)
my_turtle.right(90)
my_turtle.forward(320)
my_turtle.right(90)
my_turtle.forward(320)
my_turtle.right(90)
my_turtle.forward(160)
my_turtle.end_fill()

my_turtle.left(180)
my_turtle.forward(40)
my_turtle.right(270)
my_turtle.penup()
my_turtle.color(LOGO_COLOR)
my_turtle.forward(160)
my_turtle.pendown()
my_turtle.forward(80)
my_turtle.left(180)
my_turtle.forward(160)
my_turtle.right(180)
my_turtle.forward(80)
my_turtle.left(90)
my_turtle.penup()
my_turtle.forward(40)
my_turtle.pendown()
my_turtle.circle(40)
my_turtle.penup()
my_turtle.forward(10000)

























