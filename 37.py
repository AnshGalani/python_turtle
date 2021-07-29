import turtle

def draw_diamond(some_turtle):
    some_turtle.left(30)
    some_turtle.forward(300)
    some_turtle.right(60)
    some_turtle.forward(300)
    some_turtle.right(120)
    some_turtle.forward(300)
    some_turtle.right(60)
    some_turtle.forward(300)
    some_turtle.right(150)

def draw_art():
    window=turtle.Screen()
    window.bgcolor("black")

    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("purple","blue")
    brad.speed(0)
    for i in range(0,36):
        draw_diamond(brad)
        brad.right(10)

    brad.right(90)
    brad.forward(800)

    window.exitonclick()
draw_art()