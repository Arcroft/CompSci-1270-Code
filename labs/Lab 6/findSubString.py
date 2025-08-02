# Ashlyn Croft
# 8 Jul 25
# Lab 6
# Sub String
# Finding substrings - Honestly this one doesn't make a lot of sense to me in theory
# It helps me to think of use case, and I can't for this one
# Googled - basically constantly. CTRL F, google, email filters, huh!
# That helps it not feel abstract




def findSubStringV1(originalString, subString):
    """
    Find a substring using the built-in .find()
    """
    return originalString.find(subString)



def findSubStringV2(originalString, subString):
    """
    Find a substring using the built-in .index()
    """
    if subString in originalString:
        return originalString.index(subString)
    else:
        return -1



def findSubStringV3(originalString, subString):
    """
    Find a substring using manual iterative character comparison.
    """
    if len(subString) == 0:
        return 0 
    if len(subString) > len(originalString):
        return -1
    
    for i in range(len(originalString) - len(subString) + 1):
        match = True
        for j in range(len(subString)):
            if originalString[i + j] != subString[j]:
                match = False
                break
        
        if match:
            return i
    
    return -1




def main():
    """
    Main function that gets user input and uses each method.
    """
    print("Substring Finder")
    print("=" * 40)
    print("This program finds the index of a substring within a string.")
    print("Examples:")
    print("  String: 'APPLE CAT!' Substring: 'CAT' -> Index: 6")
    print("  String: 'APPLE CAT!' Substring: 'PIZZA' -> Index: -1 (not found)")
    print()
    
    # Get input
    originalString = input("Enter the original string: ")
    subString = input("Enter the substring to search for: ")
    
    print()
    print(f"Original string: '{originalString}'")
    print(f"Searching for: '{subString}'")
    print("-" * 40)
    
    # V1: Using .find() method
    result1 = findSubStringV1(originalString, subString)
    if result1 != -1:
        print(f"Version 1 (.find() method): Found at index {result1}")
    else:
        print("Version 1 (.find() method): Not found (returned -1)")
    
    # V2: Using .index() method
    result2 = findSubStringV2(originalString, subString)
    if result2 != -1:
        print(f"Version 2 (.index() method): Found at index {result2}")
    else:
        print("Version 2 (.index() method): Not found (returned -1)")
    
    # V3: iterative comparison
    result3 = findSubStringV3(originalString, subString)
    if result3 != -1:
        print(f"Version 3 (Manual search): Found at index {result3}")
    else:
        print("Version 3 (Manual search): Not found (returned -1)")
    
    print("-" * 40)
    
    # Verify
    if result1 == result2 == result3:
        print("✓ All methods agree on the result!")
    else:
        print("⚠ Warning: Methods produced different results!")
    
    # This part is cool af, showing it visually
    if result1 != -1:
        print(f"\nVisual representation:")
        print(f"String: {originalString}")
        print(f"Index:  {' ' * result1}{'↑' * len(subString)}")
        print(f"Match:  {' ' * result1}{subString}")

if __name__ == "__main__":
    main()