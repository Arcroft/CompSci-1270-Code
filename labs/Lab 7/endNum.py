# Ashlyn Croft
# 16 Jul 25
# I'm so burnt out
# Lab 7
# End num
# Puts numbers at the end of a list

def getIntegerList():
    """
    Uses a while loop to collect integer input
    """
    integers = []
    
    print("Enter integers one at a time. Type '*' when done.")
    
    while True:
        user_input = input("Enter an integer (or '*' to finish): ")
        
        if user_input == "*":
            break
        else:
            integers.append(int(user_input))
    
    return integers

def endNum(intList, num):
    """
    Moves all instances of num to the end of the list while otherwise maintaining order.
    """
    new_list = []
    
    # First pass: add all numbers that are NOT equal to num
    for number in intList:
        if number != num:
            new_list.append(number)
    
    # Second pass: count how many times num appears and add them to the end
    for number in intList:
        if number == num:
            new_list.append(number)
    
    return new_list

def main():
    """
    Main function that coordinates input collection and number rearrangement.
    """
    print("Move Numbers to End")
    print("=" * 30)
    print("This program moves all instances of a number to the end of your list.")
    
    # list of integers from user
    intList = getIntegerList()
    
    # Check if user entered any numbers
    if len(intList) == 0:
        print("Goodbye!")
        return
    
    print(f"\nYour list: {intList}")
    
    # Get the number to move to the end
    num = int(input("Enter the number to move to the end: "))
    
    # Move the specified number to the end
    result_list = endNum(intList, num)
    
    print()
    print("Results:")
    print("-" * 20)
    print(f"Original list: {intList}")
    print(f"Number to move: {num}")
    print(f"New list: {result_list}")
    
    # Count how many instances were moved
    count = 0
    for number in intList:
        if number == num:
            count += 1
    
    if count > 0:
        print(f"Moved {count} instance(s) of {num} to the end.")
    else:
        print(f"Number {num} was not found in the list - no changes made.")

if __name__ == "__main__":
    main()
