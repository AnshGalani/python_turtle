#NOT WOREKING
import turtle

t=turtle.Turtle()
turtle.bgcolor('black')
t.speed(0)
t.width(2)
t.pencolor('blue')

def shape(angle,side,limit):
    reverse_direction=200
    t.forward(side)

    if side%(reverse_direction*2)==0:
        angle=angle+2
        print(side)
    elif side% reverse_direction==0:
         angle=angle-2
         print(side)
         t.right(angle)
         side=side+2
         if side<limit:
            shape(angle,side,limit)
angle=119
side=0
limit=600
shape(angle,side,limit)
turtle.done()