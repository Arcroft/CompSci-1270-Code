# Ashlyn Croft
# 1 Jul 25
# Lab 4
# Centralizing shape functions

import math

## Circle Area



def areaOfCircle(radius):
    ""
    # https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/core-mathematics/geometry/geometry-of-a-circle.html
    #accessed 29 Jul 25
    ""
    area = math.pi * (radius ** 2)
    return area

def main():
    try:
        radius = float(input("Please enter the radius value"))

        # Caaarrrrrrlllllll
        answer = areaOfCircle(radius)

        # Resulks
        print(answer)

    except ValueError:
        print("Everytime you misuse the code, a small puppy is kicked.")

if __name__ == "__main__":
    main()



## Circle Circumference



def circleCircumference(radius):
    ""
    # https://www.ncl.ac.uk/webtemplate/ask-assets/external/maths-resources/core-mathematics/geometry/geometry-of-a-circle.html
    # accessed 29Jul 25
    # I've written research papers with 5+ pages of citations, never would I think I'd cite "circumference formula"
    ""
    circumference = 2 * math.pi * radius
    return circumference

def main():
    try:
        radius = float(input("Please enter the radius value"))

        # Call
        answer = circumference = 2 * math.pi * radius

        # Result
        print(answer)
    except ValueError:
        print("Try again with valid numbers")

if __name__ == "__main__":
    main()




## Rectangle Area


def areaOfRectangle(base, height):
    ""
    # https://www.cuemath.com/measurement/area-of-rectangle/
    # Accessed 29 Jul 25
    ""
    area = base * height
    return area

def main():
    try:
        base = float(input("Enter the numeric measurement of the base: "))
        height = float(input("Enter the numeric measurement of the height: "))

        # Call
        answer = areaOfRectangle(base, height)

        # Result
        print(answer)

    except ValueError:
        print("I'll be back. When you use the code the right way")

if __name__ == "__main__":
    main()


## Rectangle Perimeter 


def rectanglePerimeter(length, width):
    ""
    # Perimeter of a Rectangle
    # https://www.cuemath.com/measurement/area-of-rectangle/
    # Accessed 29 Jul 25
    ""
    perimeter = length * width
    return perimeter

def main():
    try:
        length = float(input("Enter the numeric measurement of the length: "))
        width = float(input("Enter the numeric measurement of the width: "))

        # Call
        answer = perimeter = length * width

        # Result
        print(answer)
        
    except ValueError:
        print("PLease restart and enter valid numbers")

if __name__ == "__main__":
    main()