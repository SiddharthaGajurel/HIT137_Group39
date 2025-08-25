

import turtle

# Recursive function to draw fractal edge
def draw_fractal_edge(length, depth):
    if depth == 0:
        turtle.forward(length)
    else:
        length /= 3
        draw_fractal_edge(length, depth - 1)
        turtle.left(60)
        draw_fractal_edge(length, depth - 1)
        turtle.right(120)
        draw_fractal_edge(length, depth - 1)
        turtle.left(60)
        draw_fractal_edge(length, depth - 1)

# ---------------- Main Program ----------------
# Ask user for inputs
sides = int(input("Enter the number of sides: "))
side_length = int(input("Enter the side length (pixels): "))
depth = int(input("Enter the recursion depth: "))

# Setup turtle
turtle.speed("fastest")  # makes drawing faster
turtle.bgcolor("white")  # background color
turtle.pencolor("blue")  # line color

# Draw the polygon with fractal edges
for _ in range(sides):
    draw_fractal_edge(side_length, depth)
    turtle.right(360 / sides)

turtle.hideturtle()  # hide the turtle pointer
turtle.done()
