# paola vazquez
# worked on feb 28 
# Problem 5: Draw a pattern of squares using Turtle

import turtle

def draw_squares(size, num_squares):
    turtle.speed(3)  # Set turtle speed
    for _ in range(num_squares):  
        for _ in range(4):  # Draw a square
            turtle.forward(size)  
            turtle.right(90)
        size -= 20  # Reduce the size for the next inner square
        turtle.penup()  # Lift pen to move without drawing
        turtle.forward(10)  # Move inward
        turtle.right(90)
        turtle.forward(10)
        turtle.left(90)
        turtle.pendown()  # Put pen down to start drawing again

    turtle.done()  # Finish drawing

# Call function to draw nested squares
draw_squares(100, 5)  # Start with size 100, draw 5 nested squares
