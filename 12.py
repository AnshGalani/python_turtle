import turtle

a=turtle.Turtle()
screen=turtle.Screen()
screen.bgcolor('black')
col=('pink','yellow','red','blue')
a.speed(0)
for i in range(150):
    a.pencolor(col[i%4])
    a.setheading(i*95)
    for b in range(4):
        a.forward(i*1)
        a.right(300)