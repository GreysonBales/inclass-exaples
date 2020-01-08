#Bales
#using turtle

import turtle
import random
turtle.setup(width=1000, height=1000)
x = turtle.Pen() #first object in this class!!!
x.shape("turtle")
x.color("blue")
x.speed(0)
x.width(1)



for i in range (4):
    x.forward(250)
    x.left(90)
x.up()
x.setposition(0,250)
x.down()
for i in range(3):
    x.fd(250)
    x.left(120)

x.up()
x.setposition(150,0)
x.down()
x.left(90)
x.forward(75)
x.left(90)
x.forward(50)
x.left(90)
x.forward(75)

x.up()
x.setposition(75,125)
x.down()
x.fd(50)
x.right(90)
x.fd(50)
x.right(90)
x.fd(50)
x.right(90)
x.fd(50)
