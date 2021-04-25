"""
Have the turtle draw a row of houses.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle
import random

if __name__ == '__main__':
    t = turtle.Turtle()
    def draw_house(height):
        if height == 1:
            height = 60
        elif height == 2:
            height = 120
        else:
            height = 250
        for i in range(4):

            t.forward(height)
            t.left(90)
        t.forward(height)
        t.color("green")
        t.pensize(10)
        t.forward(10)
        t.color("black")
        t.pensize(1)
    t.penup()
    t.goto(-600, 0)
    t.pendown()
    for i in range (10):
        s = random.randint(1,3)
        draw_house(s)
    # TODO)
    #   1) Move the turtle to the left side of the window near the bottom.
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.
    turtle.done()
    pass
