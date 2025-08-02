# Ashlyn Croft
# Decent into madness via banal monotony as Rome burns
# 4 Jul 25
# Lab 5
# Mutliplication Table
# Multiplities stuff and numbers and such
#Spider Spider

def multiplicationTable(lowNum, highNum):
    """
    Multiplication table for numbers from lowNum to highNum.
    
    table where each row shows one number multiplied by all numbers in the range.
    """
    
    print(f"\nMultiplication Table ({lowNum} to {highNum})")
    print("=" * 50)
    
    # width needed for formatting (largest possible product)
    max_product = highNum * highNum
    width = len(str(max_product)) + 1  # + 1 for spacing, looked wonky
    
    #Spider Spider

    # column headers
    print("   ", end="") 
    for col in range(lowNum, highNum + 1):
        print(str(col).rjust(width), end="")
    print() 
    print("   " + "-" * (width * (highNum - lowNum + 1)))  
    
    # Print each row
    for row in range(lowNum, highNum + 1):
        # row number
        print(f"{row:2} |", end="")
        
        # Print each column
        for col in range(lowNum, highNum + 1):
            product = row * col
            print(str(product).rjust(width), end="")
        
        # newline at end of row
        print()
        #spidddeeeeeeeeerrrrr
    print("=" * 50)

# And we're moving, and we're coding, and we're not looking under the hood
# Why is the code full of spiders? Because it's from the world wide web.
# Bah dum tis.
# ...just a joke, I wrote the code.
# But that isn't funny.
# Well, the quality of the code might be.
# Bah dum tis.

def main():
    """
    get user input for multiplication table.
    """
    
    print("Multiplication Table Generator")
    print("=" * 35)
    print("This program creates a multiplication table")
    print("for any range of numbers you specify.")
    print()
    
    try:
        #input from user
        lowNum = int(input("Enter the starting number (lowNum): "))
        highNum = int(input("Enter the ending number (highNum): "))
        
        # Check input
        if lowNum > highNum:
            print("Error: Starting number must be less than or equal to ending number!")
            return
        
        if highNum - lowNum > 20:
            print("Warning: Large tables may be hard to read!")
            confirm = input("Continue anyway? (y/n): ").lower()
            if confirm != 'y':
                print("Table generation cancelled.")
                return
        
        # Call function
        multiplicationTable(lowNum, highNum)
        
    except ValueError:
        print("Error: Do you ever feel like a plastic bag, floating in the wind, waiting to start again?")
        # Idk how to create noise with script to the tune of that song, but rest assured, error messages will be accompinied by Katy Perry.
        # That's katy perry right? ...Or Taylor Swift?
        # ...I'd be terrible at jepordy.

if __name__ == "__main__":
    main()