# Ashlyn Croft 24 Jul 25
# Lab 2
# Calculate Area of Rectangle


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

