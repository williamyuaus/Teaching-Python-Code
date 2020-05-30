import turtle

t = turtle.Pen()
t.speed(0)
BACKGROUND_COLOR = "#000000" 
PIZZA_COLOR1 = "#FE0000"
PIZZA_COLOR2 = "#FF8300"
PIZZA_COLOR3 = "#B3FF00"
PIZZA_COLOR4 = "#69FF00"
PIZZA_COLOR5 = "#00FF40"
PIZZA_COLOR6 = "#00FF7A"
PIZZA_COLOR7 = "#00FFDE"
PIZZA_COLOR8 = "#0091FF"
PIZZA_COLOR9 = "#0021FF"
PIZZA_COLOR10 = "#7500FF"
PIZZA_COLOR11 = "#D900FF"
PIZZA_COLOR12 = "#FF00CC"
PIZZA_COLOR13 = "#FF0096"
PIZZA_COLOR14 = "#FF0059"
turtle.speed(10)

screen = turtle.Screen()
screen.bgcolor(BACKGROUND_COLOR)
screen.title("Rainbow Pizza")
my_turtle = turtle.Turtle()



def draw_circle(radius, line_color, fill_color):
    my_turtle.color(line_color)
    my_turtle.fillcolor(fill_color)
    my_turtle.begin_fill()
    my_turtle.circle(radius)
    my_turtle.end_fill()

def move_turtle(x, y):
    my_turtle.up()
    my_turtle.goto(x, y)
    my_turtle.down

my_turtle.pensize(1)
draw_circle(150, PIZZA_COLOR1, PIZZA_COLOR1)
draw_circle(140, PIZZA_COLOR2, PIZZA_COLOR2)
draw_circle(130, PIZZA_COLOR3, PIZZA_COLOR3)
draw_circle(120, PIZZA_COLOR4, PIZZA_COLOR4)
draw_circle(110, PIZZA_COLOR5, PIZZA_COLOR5)
draw_circle(100, PIZZA_COLOR6, PIZZA_COLOR6)
draw_circle(90, PIZZA_COLOR7, PIZZA_COLOR7)
draw_circle(80, PIZZA_COLOR8, PIZZA_COLOR8)
draw_circle(70, PIZZA_COLOR9, PIZZA_COLOR9)
draw_circle(60, PIZZA_COLOR10, PIZZA_COLOR10)
draw_circle(50, PIZZA_COLOR11, PIZZA_COLOR11)
draw_circle(40, PIZZA_COLOR12, PIZZA_COLOR12)
draw_circle(30, PIZZA_COLOR13, PIZZA_COLOR13)
draw_circle(20, PIZZA_COLOR14, PIZZA_COLOR14)
draw_circle(10, PIZZA_COLOR1, PIZZA_COLOR1)
draw_circle(5, PIZZA_COLOR2, PIZZA_COLOR2)
draw_circle(2.5, PIZZA_COLOR3, PIZZA_COLOR3)
draw_circle(1.25, PIZZA_COLOR4, PIZZA_COLOR4)

x = 1
while x < 13:
    if x == 1:
        move_turtle(-70, 105)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR1)
        x += 1
    if x == 2:
        move_turtle(-85, 175)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR2)
        x += 1
    if x == 3:
        move_turtle(-25, 50)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR3)
        x += 1
    if x == 4:
        move_turtle(-15, 100)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR4)
        x += 1
    if x == 5:
        move_turtle(-25, 150)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR5)
        x += 1
    if x == 6:
        move_turtle(-30, 204)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR6)
        x += 1
    if x == 7:
        move_turtle(15, 50)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR7)
        x += 1
    if x == 8:
        move_turtle(20, 200)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR8)
        x += 1
    if x == 9:
        move_turtle(60, 156)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR9)
        x += 1
    if x == 10:
        move_turtle(71, 215)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR10)
        x += 1
    if x == 11:
        move_turtle(80, 90)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR11)
        x += 1
    if x == 12:
        move_turtle(95, 150)
        draw_circle(13, PIZZA_COLOR1, PIZZA_COLOR12)
        x += 1
my_turtle.pensize(10)
my_turtle.up()
move_turtle(0, 150)
my_turtle.begin_fill()
my_turtle.color(BACKGROUND_COLOR)
my_turtle.forward(160)
my_turtle.right(180)
my_turtle.forward(320)
move_turtle(0, 150)
my_turtle.left(90)
my_turtle.forward(160)
my_turtle.right(180)
my_turtle.forward(320)
move_turtle(0, 150)
my_turtle.left(45)
my_turtle.forward(160)
my_turtle.right(180)
my_turtle.forward(320)
move_turtle(0, 150)
my_turtle.right(90)
my_turtle.forward(160)
my_turtle.right(180)
my_turtle.forward(320)

move_turtle(0, 0)


    

