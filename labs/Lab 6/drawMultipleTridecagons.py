# Ashlyn Croft
# 1 Jul 25
# Lab 4
# Multiple Dragon Turtles in a Row
# This script draws multiple 13-sided polygons
# Which I've since learned how to pronounce, and it's not a cool word at all
# I can see why dragons don't want to be associated with it.

import turtle

def tridecagonTurtle(s, x, y, t):
    """
    Draws a regular tridecagon using turtle graphics.
    
    Parameters:
    s - length of each side of tridecagon
    x - x-coordinate of starting vertex
    y - y-coordinate of starting vertex  
    t - turtle object that will draw the shape
    
    Information about tridecagons and polygon angles from:
    "Regular polygon" Wikipedia. https://en.wikipedia.org/wiki/Regular_polygon
    Accessed: June 29, 2025
    "Wikipedia. It's AI for people over 30. Don't get lied to by an algorhythm, get lied to by another human being."
    
    For a regular polygon with n sides, the exterior angle = 360/n degrees.
    For a tridecagon (13 sides): 360/13 = approximately 27.69 degrees
    """
    
    # Move turtle to start - watching out for bannanas or mario
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    # Calculate the exterior angle for a 13-sided polygon
    exterior_angle = 360 / 13
    
    # Draw tridecagon using a for loop
    for side in range(13):
        t.forward(s)           # Draw one side
        t.left(exterior_angle) # Turn by the exterior angle

def drawMultipleTridecagons(s, x, y, nr, sr, t):
    """
    Draws multiple tridecagons in a line by calling tridecagonTurtle() multiple times.
    
    Parameters:
    s - length of each side of the tridecagons
    x - x-coordinate of the first tridecagon
    y - y-coordinate for all tridecagons (same for all)
    nr - number of tridecagon repetitions to draw
    sr - spacing between tridecagons on the x-axis
    t - turtle object that will draw the shapes
    
    Example: if x=80, nr=3, sr=50, tridecagons will be drawn at x=80, x=130, x=180
    """
    
    print(f"Drawing {nr} tridecagons starting at x={x} with {sr} units spacing...")
    
    # Use a for loop to draw multiple tridecagons
    for i in range(nr):
        # Calculate the x-coordinate for this tridecagon
        current_x = x + (i * sr)
        
        print(f"Drawing tridecagon {i + 1} at position ({current_x}, {y})")
        
        # Call the original tridecagon function with the current position
        tridecagonTurtle(s, current_x, y, t)

def main():
    """
    Main function that gets user input and creates multiple tridecagons.
    I choose you, Tridecagon!
    Tridecagon used tackle!
    It was super effective!
    """
    
    print("Multiple Tridecagon Drawer!")
    print("This will draw multiple 13-sided polygons in a row.")
    print("=" * 50)
    
    # Get input from user
    s = int(input("Enter the length of each side: "))
    x = int(input("Enter the x-coordinate for the first tridecagon: "))
    y = int(input("Enter the y-coordinate for all tridecagons: "))
    nr = int(input("Enter the number of tridecagons to draw: "))
    sr = int(input("Enter the spacing between tridecagons: "))
    
    # Set up the screen
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Multiple Regular Tridecagons")
    screen.setup(width=1000, height=600)  # Make window wider for multiple shapes
    
    # Create turtle object
    my_turtle = turtle.Turtle()
    my_turtle.color("blue")
    my_turtle.speed(6)
    my_turtle.pensize(2)
    
    # Call the function to draw multiple tridecagons
    drawMultipleTridecagons(s, x, y, nr, sr, my_turtle)
    
    print("Done! Click on the window to close. Or stay here forever. No pressure.")
    
    # Keep the window open until clicked
    screen.exitonclick()

# Only runs when the script is executed directly
if __name__ == "__main__":
    main()