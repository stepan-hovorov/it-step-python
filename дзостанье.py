import random
import turtle

t = turtle.Turtle()
t.shape("turtle")
t.speed(1)
turtle.pensize(5)
turtle.color('Yellow')
a=0
for i in range(10):
    a = a+25
    for j in range(5):
        t.forward(a)
        t.right(180-36)
        t.forward(a)
        t.left(70)
    t.penup()
    t.left(55)
    t.forward(10)
    t.pendown()
    t.right(45)




