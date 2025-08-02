# Ashlyn Croft 24 Jul 25
# Lab 2
# Perimeter of a Rectangle
# https://www.cuemath.com/measurement/area-of-rectangle/
# Accessed 24 Jul 25
# I don't know if this is another reading comprehension check for this class, but cite perimeter? Seriously?
# I would much rather spend my time in this class practicing coding, not googling for elementary formulas to check frivolous boxes.
# Going back to school in my 30's has fully developed being a grouchy old lady.

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


