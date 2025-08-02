# Ashlyn Croft
# 6JUL25
# Lab 6
# Reverse String
# Functions that take user input strings and reverse them.

def reverseStringV1(inputString):
    """
    Reverse a string using string slicing.
    
    inputString - the string to reverse (string)
    
    Returns the reversed string (string)
    """
    return inputString[::-1]


def reverseStringV2(inputString):
    """
    Reverse a string using the built-in reversed() function.
    
    inputString - the string to reverse (string)
    
    Returns the reversed string (string)
    """
    return ''.join(reversed(inputString))

def reverseStringV3(inputString):
    """
    Reverse a string using a for loop with range() function.
    
    inputString - the string to reverse (string)
    
    Returns the reversed string (string)
    """
    reversedString = ""
    # Loop backwards
    for i in range(len(inputString) - 1, -1, -1):
        reversedString += inputString[i]
    return reversedString




def reverseStringV4(inputString):
    """
    Reverse a string using a for loop without range() function.
    
    inputString - the string to reverse (string)
    
    Returns the reversed string (string)
    """
    reversedString = ""
    # Loop through each character
    for char in inputString:
        reversedString = char + reversedString
    return reversedString


def reverseStringV5(inputString):
    """
    Reverse a string using a while loop.
    
    inputString - the string to reverse (string)
    
    Returns the reversed string (string)
    """
    reversedString = ""
    index = len(inputString) - 1
    
    # Loop backwards
    while index >= 0:
        reversedString += inputString[index]
        index -= 1
    
    return reversedString




def main():
    """
    Main function that gets user input and demonstrates all string reversal methods.
    """
    print("String Reversal Demonstration")
    print("=" * 40)
    print("This program shows 5 different ways to reverse a string.")
    print("Example: 'APPLE CAT!' becomes '!TAC ELPPA'")
    print()
    
    # Get input from user
    userString = input("Enter a string to reverse: ")
    print()
    print("Original string:", userString)
    print("-" * 40)
    
    # V 1: String slicing
    result1 = reverseStringV1(userString)
    print(f"Version 1 (String slicing): {result1}")
    
    # V2: reversed() function
    result2 = reverseStringV2(userString)
    print(f"Version 2 (reversed() function): {result2}")
    
    # V3: For loop with range()
    result3 = reverseStringV3(userString)
    print(f"Version 3 (For loop with range): {result3}")
    
    # V4: For loop without range()
    result4 = reverseStringV4(userString)
    print(f"Version 4 (For loop, direct iteration): {result4}")
    
    # V5: While loop
    result5 = reverseStringV5(userString)
    print(f"Version 5 (While loop): {result5}")
    
    print("-" * 40)
    print("All methods should produce identical results!")
    
    # check results are the same
    if result1 == result2 == result3 == result4 == result5:
        print("✓ Success! All reversal methods work correctly. My sanity is intact.")
    else:
        print("⚠ Warning: Methods produced different results! Can someone dim the sun? This is not helping my headache.")

if __name__ == "__main__":
    main()

# They should lock me up for how much of my own code I cannibalize
# ...oh my god. Why havn't I written a script to fill in all the basics on a new file?!
# Put in my name, todays date, Lab X, throw down the "if __name__" line and other lines that are the same layout just need customizing
# I could plop the assignment description into it commented out, and then shift pieces around for easy comments
# And to make sure I'm checking all the boxes
# Omg that would make my life so much easier.