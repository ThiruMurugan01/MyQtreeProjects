import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Move the turtle forward and turn it right four times to draw a square
for _ in range(9):
    my_turtle.forward(400)
    my_turtle.right(50)
    my_turtle.left(100)
    my_turtle.right(150)
    my_turtle.left(200)
    my_turtle.right(250)
    my_turtle.left(300)
    my_turtle.right(350)

    # Close the turtle graphics window
turtle.done()