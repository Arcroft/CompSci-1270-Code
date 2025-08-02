# Ashlyn Croft
# 29Jun25 Because I am an idiot and forgot
# Lab 3
# Shape that I can't not read as "dragon turtle"
# in theory, this creates said dragon shape

import turtle

def tridecagonTurtle(s, x, y, t):
    """
    Draws a regular tridecagon using turtle graphics.
    
    Parameters:
    s - length of each side of tridecagon
    x - x-coordinate of starting vertex
    y - y-coordinate of starting vertex  
    t - turtle object that will draw the shape
    
    Citation: Information about tridecagons and polygon angles from:
    "Regular polygon" Wikipedia. https://en.wikipedia.org/wiki/Regular_polygon
    Accessed: June 29, 2025
    
    For a regular polygon with n sides, the exterior angle = 360/n degrees.
    For a tridecagon (13 sides): 360/13 = approximately 27.69 degrees
    """
    
    # Move turtle to starting position
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Calculate the exterior angle for a 13-sided polygon
    exterior_angle = 360 / 13
    
    # draw tridecagon using a for loop
    for side in range(13):
        t.forward(s)           # Draw one side
        t.left(exterior_angle) # Turn by the exterior angle

def main():
    """
    Main function that gets user input and creates the tridecagon.
    """
    
    # Get input
    print("Let's draw a tridecagon (13-sided polygon)! I know it sounds like a dragon, but really it's much less exciting.")
    s = int(input("Enter the length of each side: "))
    x = int(input("Enter the x-coordinate for the starting point: "))
    y = int(input("Enter the y-coordinate for the starting point: "))
    

    # Set up screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Regular Tridecagon")
    
    # turtle-y turtle-y turtle
    my_turtle = turtle.Turtle()
    my_turtle.color("blue")
    my_turtle.speed(5)
    
    # Call the function to draw it
    tridecagonTurtle(s, x, y, my_turtle)
    
    # Keep the window open until clicked
    screen.exitonclick()

# only runs when the script is executed directly
if __name__ == "__main__":
    main()