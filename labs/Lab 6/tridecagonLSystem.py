#Ashlyn Croft
# 9Jul25
# Lab 6
# Tridecagon ...thing?
# Modifying runestone code and using the previous tridecagon script.

# Honestly, I hate turtle. I don't know if that's making this harder to get, but hopefully this is right.
# The key takeaway is automation? That is, generating many iterations and reducing script length at the same time?

import turtle
import random
import drawMultipleTridecagons

# Modification of Code-copyright belonging to Brad Miller & David Ranum using Runestone interactive
# https://runestone.academy/ns/books/published/iowastateuniversity_thinkcspy_summer25/Strings/TurtlesandStringsandLSystems.html
# Copyright 2014
# Accessed 9Jul25

def createLSystem(numIters, axiom):

    startString = axiom
    endString = ""
    for i in range(numIters):
        endString = processString(startString)
        startString = endString
    return endString

def processString(oldStr):

    newstr = ""
    for ch in oldStr:
        newstr = newstr + applyRules(ch)
    return newstr

def applyRules(ch):

    newstr = ""
    if ch == 'F':
        newstr = 'F-F++F-H'     # Added H
    elif ch == 'H':
        newstr = 'HP+F'
    elif ch == 'P':
        newstr = 'P++'          # Random position
    else:
        newstr = ch             
    return newstr




def drawLsystem(aTurtle, instructions, angle, distance):

    for cmd in instructions:
        if cmd == 'F':
            aTurtle.forward(distance)
        elif cmd == 'B':
            aTurtle.backward(distance)
        elif cmd == '+':
            aTurtle.right(angle)
        elif cmd == '-':
            aTurtle.left(angle)
        elif cmd == 'H':
            current_x = aTurtle.xcor()
            current_y = aTurtle.ycor()
            drawMultipleTridecagons.tridecagonTurtle(distance * 3, current_x, current_y, aTurtle)
        elif cmd == 'P':

            aTurtle.penup()

            random_x = random.randint(-300, 300)
            random_y = random.randint(-200, 200)
            aTurtle.goto(random_x, random_y)
            aTurtle.pendown()

def main():
    print("Tridecagon L-System Generator")
    print("=" * 40)
    print("This creates fractal patterns with 13-sided polygons - in theory.")
    print()
    

    inst = createLSystem(3, "F")
    print("L-System Instructions:")
    print(inst)
    print()
    print("Command meanings:")
    print("F = Forward, + = Right turn, - = Left turn")
    print("H = Draw tridecagon, P = Random position")
    print()
    
    # Create turtle
    t = turtle.Turtle()
    wn = turtle.Screen()
    wn.bgcolor("black")  #contrast
    wn.setup(800, 600)
    

    t.up()
    t.goto(-200, 0)      # Start
    t.down()
    t.speed(8)           # Faster drawing - because it takes forever to keep testing it
    t.color("cyan")
    t.pensize(2)         # Thicc lines
    

    drawLsystem(t, inst, 75, 8)
    
    print("Click to close.")
    wn.exitonclick()

if __name__ == "__main__":
    main()


    # This was... taxing. I think I'd be enjoying this alot more if I wasn't buried under several stem courses compressed into 8 weeks.

    # Okay! So! I felt like I was phoning this in here and didn't have total understanding. So I took a break and came back to it.
    # It's like generating songs on a piano. Every letter in the alphabet is assigned 10 keys and different time intervals.
    # Maybe upper case letters shorter time intervals - whatever
    # Then, any given word is generative of an entire song.

    # THIS is how I could do an inventory system for the CYOA text game. Inventory interaction with random rolls, etc.
    # Each letter choice might be assigned to backend strings
    # those strings can run checks on other functions, "Is X in inventory", "Is X perk taken", "Is xp gained?"
    # So the strings and reversals and everything -isn't- about wordplay so much, or counting letters, as it is
    # recognizing the framework to create massively generative commands with "simple" strings. 
    # Even the same strings, analyzed in differnt ways.
    # Oooooookaaaaayyyy. I still don't like turtle, BUT, I did learn and understand what this is moving towards
    # ...I wonder what games are made in python? 
    # Coding is probably my least favorite part of statistics
    # I think, as much as I hate turtle, turtle was just responsible for helping me to look at some R problems in new ways
    # And dislike coding less. I'm a "why" learner, not a "what" learner. Memorizing formulas or commands is miserable for me.
    # Which, is what a lot of coding is early on. This might have been a step into "why".