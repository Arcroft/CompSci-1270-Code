# Ashlyn Croft
# 6 Jul 25
# Lab 5
# Last One
# Number Triangle
# Makes a triangle out of numbers from user input                                                          ...and my diminishing sanity.

def sameNumberTriangle(num):
    """
    triangle pattern with ascending numbers on each row.
    
    """
    
    print(f"\nSame Number Triangle (Height: {num})")
    print("-" * 35)
    
    # Print each row of the triangle
    for row in range(1, num + 1):
        # Print numbers from 1 to row number
        for number in range(1, row + 1):
            print(number, end="")
            # Add space between numbers - Forgetting this line is no beuno
            if number < row:
                print(" ", end="")
        print()
    
    print("-" * 35)

def main():
    """
    user input for number triangle.
    """
    
    print("Same Number Triangle Generator")
    print("=" * 35)
    print("This program creates a triangle pattern")
    print("where each row shows numbers from 1")
    print("up to the row number.")
    print()
    
    try:
        # iNpUt FrOm UsEr
        num = int(input("Enter the height of the triangle: "))
        
        # Check input for shenanigans
        if num <= 0:
            print("Error: Triangle height must be a positive number!")
            return
        
        if num > 25:
            print("Warning: Very large triangles may be hard to view!")
            confirm = input("Continue anyway? (y/n): ").lower()
            if confirm != 'y':
                print("Triangle generation cancelled.")
                return
        
        # Call function
        sameNumberTriangle(num)
        
    except ValueError:
        print("Error: Please enter a valid whole number!")

if __name__ == "__main__":
    main()

    # You have now made a triangle from numbers, that is measured by numbers, run by numbers.
    # What are you, a mathmatician?!


    # As an aside
    # Landing a Job in Artificial Intelligence - Will Capella (from the lab reading)
    # Isn't it kind of existentially facinating that by attempting to create a facimile of intelligence
    # We lower overall intelligence?
    # Like a great filter cap on intelligence
    # We got too smart
    # So we engineered a way to stop being smart