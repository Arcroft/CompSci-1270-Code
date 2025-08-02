# Ashlyn Croft
# Sometime in July, the 4th I think


# One wonders where the time goes
# Where youthful splendor fades
# Where bitter age gives us the smug self satisfaction to think our code comments are funny

# Lab 5
# Right triangle with stars
# Does ...that? Makes a right triangle with stars.

def starRightTriangle(num):
    """
    right triangle pattern using asterisks
    Personally, I wouldn't want a triangle made of cat buttholes
    Prints a triangle where each row has an additional star.
    
    """
    
    print(f"\nStar Right Triangle (Height: {num})")
    print("-" * 30)
    
    # row of the triangle
    for row in range(1, num + 1):
        for star in range(row):
            print("*", end="")
        print()
    
    print("-" * 30)

def main():
    """
   user input and generates the star triangle
    """
    
    print("Star Right Triangle Generator")
    print("=" * 35)
    print("This program creates a right triangle pattern")
    print("using asterisks (*) characters.")
    print()
    
    try:
        # Get input from user - refraining from vulgar language on the front end
        # Vulgarity is only for backend
        num = int(input("Enter the height of the triangle: "))
        
        # Validate input
        if num <= 0:
            print("Error: Triangle height must be a positive number! That was a complaining number!")
            return
        
        if num > 50:
            print("Warning: Very large triangles may be hard to view with your pitiful human eyes!")
            confirm = input("Continue anyway? (y/n): ").lower()
            if confirm != 'y':
                print("Triangle generation cancelled.")
                return
        
        # Callfunction
        starRightTriangle(num)
        
    except ValueError:
        print("Error: Please enter a valid whole number! ...Or else.")

if __name__ == "__main__":
    main()