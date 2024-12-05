from turtle import *

def walk():
    forward(200)

def fall_back():
    left(180)
    forward(200)
    left(180)


def walk_and_come_back():
    walk()
    fall_back()

walk_and_come_back()
exitonclick