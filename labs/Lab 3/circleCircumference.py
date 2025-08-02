# Ashlyn Croft 24 Jul 25
# Lab 2
# Circle Circumference


import math

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