# Ashlyn Croft
# 6 Jul 25
# Lab 5
# Number Pyramid
# Pyramid from user input numbers

# Apparently, I forgot to do this. As I checked the list of things to submit.
# Thankfully, it's just the diamond without a bottom - which is done and can be repurposed

def numberPyramid(num):
    """
    centered pyramid pattern using numbers.
    """
    
    print(f"\nNumber Pyramid (Height: {num})")
    print("-" * (num * 2 + 5))
    
    max_width = num * 2 - 1 
    
    # each row
    for row in range(1, num + 1):
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
    Main function for number pyramid.
    """
    
    print("Number Pyramid Generator")
    print("=" * 30)
    print("This program creates a centered pyramid pattern")
    print("using ascending numbers on each row.")
    print()
    
    try:
        # input
        num = int(input("Enter the height of the pyramid: "))
        
        # checkk input
        if num <= 0:
            print("Error: Pyramid height must be a positive number!")
            return
        
        if num > 20:
            print("Warning: Very large pyramids may be hard to view!")
            confirm = input("Continue anyway? (y/n): ").lower()
            if confirm != 'y':
                print("Pyramid generation cancelled. The pharoahs are PISSED.")
                return
        
        # Call the function
        numberPyramid(num)
        
    except ValueError:
        print("Error: Please enter a valid whole number!")

if __name__ == "__main__":
    main()