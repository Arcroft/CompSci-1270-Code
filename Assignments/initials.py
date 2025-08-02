# Ashlyn Croft
# Lab 2
# Initials w/ turtle
# 24 JUN 25

import turtle

# My initials are ARC
# I've decided I hate turtle from this assignment

# This will require drawing exactly two letters - the first letter of your first name, and the first
# letter of your last name.
# ¡ Each letter of your initials should have an 'outline' that has a distinct color of your choosing.
# ¡ The 'outline' of your initials should be 'filled in' with different colors of your choosing, such
# that the inner portions are clearly different from the 'outlines.'
# ¡ The background of the drawing should be a different color than anything used in your
# letters.
# ¡ The two letters should be separate from one another. Meaning you will have to 'pick up' the
# pen/ turtle after drawing the first letter, move it to a new location, and start drawing the
# second letter.
# ¡ Use your imagination for how to accomplish all of this

# How the hell do I "fill in" a C?

import turtle

# Setup
turtle.bgcolor("lightblue")
turtle.pensize(5)
turtle.speed(5)

# A
turtle.pencolor("red")
turtle.fillcolor("yellow")
turtle.begin_fill()
turtle.goto(0, 0)
turtle.goto(20, 60)
turtle.goto(40, 0)
turtle.goto(30, 0)
turtle.goto(25, 20)
turtle.goto(15, 20)
turtle.goto(10, 0)
turtle.goto(0, 0)
turtle.end_fill()

# Transition
turtle.penup()
turtle.goto(80, 0)
turtle.pendown()

# C
turtle.pencolor("blue")
turtle.goto(80, 60)
turtle.goto(100, 60)
turtle.penup()
turtle.goto(80, 0)
turtle.pendown()
turtle.goto(100, 0)

turtle.done()

# Yup, I hate turtle now. It makes base R look artistic.
# Sure, AI will eventually consume unsustainable, catastrophic levels of heavy metals, water, electiricity; and, sure, it'll decimate entry level positions
# and companies are too short sided to do anything but insist everyone has 10 years experience, even if no jobs exist to provide it.
# and sure, AI will likely be used nefariously for facial recognition, electoral infleuncing, and create technofuedal autocracies.
# and okay, there's even a chance it will corrupt the epistomology of science, medicine, higher learning leading to a breakdown in understanding beyond function.
# and maybe it'll do a fun skynet thing.
# But, at least I won't have to use turtle again.