"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle


if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    t = turtle.Turtle()
    def square():
        t.square(150,150)
    def triangle():
        t.circle(150, 360,3)
    def circle():
        t.circle(150, 360,150)
    q = simpledialog.askstring("","do you want to draw a triangle, square, or circle?")
    if q == "triangle":
        triangle()
    elif q == "square":
        square()
    else:
        circle()
    turtle.done()
    # TODO)
    #   1. Create a turtle.
    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.
    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    pass
