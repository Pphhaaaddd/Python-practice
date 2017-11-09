import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(10)

    for i in range(4):
        brad.forward(50)
        brad.right(90)

def draw_circle():
    angie = turtle.Turtle()
    angie.shape("arrow")
    angie.color("black")
    angie.speed(10)

    angie.circle(100)

def draw_triangle():
    david = turtle.Turtle()
    david.color("red")
    david.speed(10)

    for i in range(3):
        david.forward(50)
        david.right(120)

# make a window to display the tutles
window = turtle.Screen()
window.bgcolor("blue")
draw_square()
draw_circle()
draw_triangle()

window.exitonclick()
