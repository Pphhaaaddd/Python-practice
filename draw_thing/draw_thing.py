import turtle

def draw_square(some_turtle):
    for i in range(4):
        some_turtle.forward(50)
        some_turtle.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("black")
    angie.speed(10)

    angie.circle(100)

def draw_triangle():
    david = turtle.Turtle()
    david.color("yellow")
    david.speed(10)

    for i in range(3):
        david.forward(50)
        david.right(120)

def draw_circleFromSquare(some_turtle):
    for i in range(36):
        draw_square(some_turtle)
        some_turtle.left(10)


# make a window to display the tutles
window = turtle.Screen()
window.bgcolor("black")

brad = turtle.Turtle()
brad.shape("turtle")
brad.color("yellow")
brad.speed(15)

#draw_square(brad)
#draw_circle()
#draw_triangle()
draw_circleFromSquare(brad)

window.exitonclick()
