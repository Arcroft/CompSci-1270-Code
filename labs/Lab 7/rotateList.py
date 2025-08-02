#Ashlyn Croft
# 16jul25
# Lab 7
# Rotate List
# ...rotating stuff in a list

def getIntegerList():
    """
    Uses a while loop to collect integer input until user enters '*'.
    
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

def rotateList(intList, rot):
    """
    Rotates a list left or right by the specified amount.
    
    """
    # empty list or no rotation
    if len(intList) == 0 or rot == 0:
        return intList.copy()
    
    # cases where rotation amount is larger than list length
    rot = rot % len(intList)
    
    # After operation, if rot becomes 0, no rotation needed
    if rot == 0:
        return intList.copy()
    
    # Rotate the list using slicing
    # For positive rot: take last rot elements and move to front
    # For negative rot: converts to equivalent positive rotation
    rotated_list = intList[-rot:] + intList[:-rot]
    
    return rotated_list

def main():
    """
    Main function that coordinates input collection and list rotation.
    """
    print("List Rotation")
    print("=" * 25)
    print("This program rotates your list left or right.")
    print("Positive rotation = right, Negative rotation = left")
    
    # list of integers from user
    intList = getIntegerList()
    
    # Check if user entered any numbers
    if len(intList) == 0:
        print("Goodbye!")
        return
    
    print(f"\nYour list: {intList}")
    
    # rotation amount
    rot = int(input("Enter rotation amount (positive=right, negative=left): "))
    
    # Rotate
    rotated_list = rotateList(intList, rot)
    

    print()
    print("Results:")
    print("-" * 25)
    print(f"Original list: {intList}")
    print(f"Rotation amount: {rot}")
    
    if rot > 0:
        print(f"Direction: Right")
    elif rot < 0:
        print(f"Direction: Left")
    else:
        print(f"Direction: No rotation")
    
    print(f"Rotated list: {rotated_list}")
    

    if rot != 0 and len(intList) > 0:
        actual_rot = rot % len(intList)
        if actual_rot != 0:
            if rot > 0:
                print(f"\nExplanation: Moved last {actual_rot} element(s) to the front")
            else:
                original_rot = abs(rot) % len(intList)
                print(f"\nExplanation: Moved first {original_rot} element(s) to the end")

if __name__ == "__main__":
    main()


    # Alright, my brain is fried. It runs, but jesus, I normally play around with it more and I 
    # JUst want to turn my brain off