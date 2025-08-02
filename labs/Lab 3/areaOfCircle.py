# Ashlyn Croft 24 Jul 25
# Lab 2
# Circle Area


import math

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


