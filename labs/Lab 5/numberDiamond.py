# Ashlyn Croft

# Sixth Day of July, Anno Domini 2025
# Lab 5
# Number Diamond

# It makes a diamond
# With numbers
# That look like a diamond

# Except My first attempt was a stupid hill - flat on left side


def numberDiamond(num):
    """
    diamond pattern using numbers.
    
    """
    
    print(f"\nNumber Diamond (Size: {num})")
    print("-" * (num * 2 + 5))
    
    #  maximum width
    max_width = num * 2 - 1 
    
    # First stage--Ascending from 1 to num
    for row in range(1, num + 1):
        current_width = row * 2 - 1
        
        #center this row
        spaces_needed = (max_width - current_width) // 2
        
        # leading spaces for centering
        print(" " * spaces_needed, end="")
        
        # numbers from 1 to row
        for number in range(1, row + 1):
            print(number, end="")
            # Add space between numbers
            if number < row:
                print(" ", end="")
        print()
    
    # Second stage
    for row in range(num - 1, 0, -1):
        current_width = row * 2 - 1 
        spaces_needed = (max_width - current_width) // 2
        print(" " * spaces_needed, end="")

        for number in range(1, row + 1):
            print(number, end="")

            if number < row:
                print(" ", end="")
        print()  
    
    print("-" * (num * 2 + 5))

def main():
    """
    user input number diamond.
    """
    
    print("Number Diamond Generator")
    print("=" * 30)
    print("This program creates a diamond pattern")
    print("using ascending numbers.")
    print()
    
    try:
        # Get input
        num = int(input("Enter the size of the diamond: "))
        
        # Check input
        if num <= 0:
            print("Error: Diamond size must be a positive number!")
            return
        
        if num > 20:
            print("Warning: Very large diamonds may be hard to view!")
            confirm = input("Continue anyway? (y/n): ").lower()
            if confirm != 'y':
                print("Diamond generation cancelled.")
                return
        
        # Call function - I am tempted to make an Its always sunny reference every.single.time I type this. "You will call heeeeeerrr!"
        numberDiamond(num)
        
    except ValueError:
        print("Error: Please enter a valid whole number!")

if __name__ == "__main__":
    main()


    # It lives!
    # This was... More compliated than I thought it'd be.
    # This frankenstein monster of code.