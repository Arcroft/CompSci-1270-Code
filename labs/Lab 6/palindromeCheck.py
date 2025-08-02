# Ashlyn Croft
# 7Jul25
# Lab 6
# Palindrome
# Check if a word is a palindrome: a word that's the same forwards or backwards. "Mom"

# I try to make these ~fun, or at least engaging. Same with papers or whatever assignments. It sucks to read 100 variations of
# The exact same thing with no deviation
# But I'm hitting burnout -hard-, sorry.

import reverseString



def palindromeCheckV1(inputString):
    """
    Check if a string is a palindrome
    """
    # Use one of the reverse string functions from imported module
    reversedString = reverseString.reverseStringV1(inputString)
    
    # Compare original string with its reverse
    return inputString == reversedString

def palindromeCheckV2(inputString):
    """
    Check if a string is a palindrome by comparing characters iteratively.
    By iteration? Is iteratively a word? I'm so tired words are starting to look alien in their spelling.
    """
    # Get the length of the string
    stringLength = len(inputString)
    
    # Compare characters from outside working inward
    for i in range(stringLength // 2):
        # Compare character at position i with character at position (length - 1 - i)
        if inputString[i] != inputString[stringLength - 1 - i]:
            return False
    
    # If we made it through all comparisons, it's a palindrome
    return True



def main():
    """
    Main function that gets user input and demonstrates both palindrome checking methods.
    """
    print("Palindrome Checker")
    print("=" * 40)
    print("This program checks if a string reads the same forwards and backwards.")
    
    # Get input
    userString = input("Enter a string to check: ")
    print()
    print("Original string:", userString)
    print("-" * 40)

    

    # V1: reverse string function
    result1 = palindromeCheckV1(userString)
    if result1:
        print("Version 1 (Using reverse function): ✓ PALINDROME")
    else:
        print("Version 1 (Using reverse function): ✗ NOT a palindrome")
    
    # V2: Iterative comparison
    result2 = palindromeCheckV2(userString)
    if result2:
        print("Version 2 (Character comparison): ✓ PALINDROME")
    else:
        print("Version 2 (Character comparison): ✗ NOT a palindrome")
    
    print("-" * 40)
    
    # CVcheck both methods agree
    if result1 == result2:
        print("✓ Both methods agree on the result!")
    else:
        print("⚠ Warning: Methods produced different results!"
              )
    

    # Show the comparison
    reversedVersion = reverseString.reverseStringV1(userString)
    print(f"\nComparison for Version 1:")
    print(f"Original:  '{userString}'")
    print(f"Reversed:  '{reversedVersion}'")
    print(f"Match:     {userString == reversedVersion}")

if __name__ == "__main__":
    main()


