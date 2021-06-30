import turtle
turtle.bgcolor("black")

turtle.speed(0)
turtle.pensize(4)
turtle.pencolor("blue")

def drawcircle(redius):
    for i in  range(10):
        turtle.circle(redius)
        redius=redius-4

def drawdesign():
    for i in range(10):
        drawcircle(150)
        turtle.right(36)

drawdesign()
turtle.done()