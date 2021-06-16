import turtle as t
from typing import AsyncGenerator

t.bgcolor('black')
t.pencolor('yellow')
t.speed(0)

def shape(angle,side,lin):
    rev_dir=200
    t.forward(side)

    if side % (rev_dir+2)==0:
        angle=angle+2
    t.right(angle)
    side=side+2
    if side < lin:
        shape(angle,side,lin)

angle=119
side=0
lin=600
shape(angle,side,lin)
t.done()