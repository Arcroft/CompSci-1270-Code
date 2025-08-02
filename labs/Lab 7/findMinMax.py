# Ashlyn Croft
# 16 Jul 25
# Lab 7
# Find Min Max Functions
# Takes user input numbers and finds minimum and maximum values




def getNumberList():
    """
    Uses a while loop to collect string input until user enters *
    
    Returns a list of string integers.
    """
    numbers = []
    
    print("Enter integers one at a time. Type * when done.")
    
    while True:
        user_input = input("Enter a number (or * to finish): ")
        
        if user_input == "*":
            break
        else:
            numbers.append(user_input)
    
    return numbers




def findMin(numberList):
    """
    Finds the minimum value in a list
    """
    # first number as our minimum
    minimum = numberList[0]
    
    # Check each number in list
    for number in numberList:
        if number < minimum:
            minimum = number
    
    return minimum

def findMax(numberList):
    """
    Finds the maximum value in a list
    """
    # Start with maximum
    maximum = numberList[0]
    
    # Check each number
    for number in numberList:
        if number > maximum:
            maximum = number
    
    return maximum

def main():
    """
    input collection and min/max finding.
    """
    print("Min/Max Number Finder")
    print("=" * 30)
    print("This program finds the smallest and largest numbers from your input.")
    print()
    
    # Get the list of string numbers
    string_numbers = getNumberList()
    
    # Check if user entered any numbers
    if len(string_numbers) == 0:
        print("You didn't enter anything. Later Gator!")
        return
    
    print(f"\nYou entered: {string_numbers}")
    
    #strings to integers
    numbers = []
    for string_num in string_numbers:
        numbers.append(int(string_num))
    
    print(f"Converted to integers: {numbers}")
    


    # minimum and maximum values
    minimum_value = findMin(numbers)
    maximum_value = findMax(numbers)
    

    print()
    print("Results:")
    print("-" * 20)
    print(f"Minimum value: {minimum_value}")
    print(f"Maximum value: {maximum_value}")
    print(f"Range: {maximum_value - minimum_value}")

if __name__ == "__main__":
    main()