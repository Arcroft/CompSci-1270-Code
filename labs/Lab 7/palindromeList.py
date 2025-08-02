#Ashlyn Croft
# 16JUL25
# Lab 7
# Palindrome list
# Checking if elements ar epalindromes



# Is it normal to add tons of blank lines?
# I feel like all of this can really run togeather sometimes

def getStringList():
    """
    Uses a while loop to collect string input until user enters *
    """
    strings = []
    
    print("Enter strings one at a time. Type * when done.")
    
    while True:
        user_input = input("Enter a string (or * to finish): ")
        
        if user_input == "*":
            break
        else:
            strings.append(user_input)
    
    return strings






def palindromeList(stringList):
    """
    Checks if a list is palindromic
    """
    list_length = len(stringList)
    
    # Compare elements
    for i in range(list_length // 2):
        if stringList[i] != stringList[list_length - 1 - i]:
            return False
    
    # If we made it through all comparisons, it's palindromic
    # Palindromic is starting to sound weird and made up, I've read it too many times.
    return True






def main():
    """
    Main function that coordinates input and palindrome checking.
    """
    print("List Palindrome Checker")
    print("=" * 30)
    print("This program checks if your list of strings reads the same forwards and backwards.")

    # Get the list
    palList = getStringList()
    
    # Check if user entered any strings
    if len(palList) == 0:
        print("No strings entered!")
        return
    
    print(f"\nYour list: {palList}")
    
    # Check if the list is palindromic
    is_palindromic = palindromeList(palList)
    
    print()
    print("Results:")
    print("-" * 20)
    if is_palindromic:
        print("✓ TRUE - Your list is palindromic!")
        print("  (It reads the same forwards and backwards)")
    else:
        print("✗ FALSE - Your list is not palindromic.")
        print("  (It does not read the same forwards and backwards)")
    
    # comparison
    print(f"\nYour list: {palList}")
    print(f"Length: {len(palList)} elements")

if __name__ == "__main__":
    main()