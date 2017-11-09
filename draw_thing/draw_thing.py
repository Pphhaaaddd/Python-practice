import turtle

def draw_square():
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(1)

    for i in range(4):
        brad.forward(50)
        brad.right(90)

# make a window to display the tutles
window = turtle.Screen()
window.bgcolor("blue")
draw_square()
#draw_circle()
#draw_triangle()

window.exitonclick()
