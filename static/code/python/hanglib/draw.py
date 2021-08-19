#!/usr/bin/env python3

import turtle

def stand():
    turtle.penup()
    turtle.home()
    turtle.left(180)
    turtle.forward(100)
    turtle.right(90)
    turtle.pendown()
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(20)

def head():
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.forward(140)
    turtle.right(90)
    turtle.pendown()
    turtle.circle(20)

def body():
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.forward(50)
    turtle.pendown()
    turtle.forward(90)

def leftarm():
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.forward(120)
    turtle.left(45)
    turtle.pendown()
    turtle.forward(50)

def rightarm():
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.forward(120)
    turtle.right(45)
    turtle.pendown()
    turtle.forward(50)

def leftleg():
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.forward(50)
    turtle.left(135)
    turtle.pendown()
    turtle.forward(50)

def rightleg():
    turtle.penup()
    turtle.home()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(135)
    turtle.pendown()
    turtle.forward(50)

if __name__ == "__main__":
    stand()
    head()
    body()
    leftarm()
    rightarm()
    leftleg()
    rightleg()
    input('Press any key to exit.')
