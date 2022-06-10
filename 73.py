from turtle import*
import turtle
bgcolor("black")
shape("turtle")
leng=36
h=2
pu();home();rt(110);rt(45);fd(-700);pd()
for i in range(h):
    for i in range(leng):
        turtle.stamp();turtle.fd(30);
        turtle.dot(20,'#006600');turtle.fd(40);
        turtle.dot(40,'#ffffff')
        turtle.forward(h)
    turtle.rt(270)
    turtle.fd(leng)
    turtle.lt(90)
    
pu();home();rt(110);rt(100);fd(-700);pd()
for i in range(h):
    for i in range(leng):
        turtle.dot(20,'#ffffff');turtle.fd(40);
        turtle.dot(40,'#006600')
        turtle.fd(h)
    turtle.rt(270)
    turtle.fd(leng)
    turtle.lt(90)
    
pu();lt(90);fd(20);home();fd(-700);pd()
for i in range(h):
    for i in range(leng):
        turtle.dot(20,'#ffffff');turtle.fd(40);
        turtle.dot(40,'#003300')
        turtle.fd(h)
    turtle.rt(270)
    turtle.fd(leng)
    turtle.lt(90)
        
pu();home();lt(90);fd(-400);pd()
for i in range(h):
    for i in range(leng):
        turtle.dot(20,'#003300');turtle.fd(40);
        turtle.dot(40,'#ffffff')
        turtle.fd(h)
    turtle.rt(270)
    turtle.fd(leng)
    turtle.lt(90)