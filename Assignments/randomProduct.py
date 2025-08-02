# Croft, Ashlyn Croft
# 29Jul25
# Lab 3
# Illusion of "random" numbers, and then multiplies how it do

import random

def randomProduct(a, b, c):
    """
    Calculate the product of 'a' random numbers between b and c.
    
    Parameters:
    a - how many random numbers
    b - minimum value for random numbers
    c - maximum value for random numbers
    
    Returns:
    product - the result of multiplying all the random numbers together
    
    """
    
    # Start with product = 1
    product = 1
    
    print(f"Generating {a} random numbers between {b} and {c} using wizardy:")
    
    # for loop to generate 'a' random numbers
    for i in range(a):
        # random number between b and c (inclusive)
        random_number = random.randrange(b, c + 1)
        
        print(f"Random number {i + 1}: {random_number}")
        
        # running product
        product = product * random_number
    
    print(f"Final calculation: {product}")
    return product

def main():
    """
    function that gets user input and calculates the random product.
    """
    
    print("Random Product Calculator")
    print("=" * 30)
    
    # Get input
    a = int(input("Enter how many random numbers to generate: "))
    b = int(input("Enter the minimum value: "))
    c = int(input("Enter the maximum value: "))
    
    print(f"\nCalculating product of {a} random numbers between {b} and {c}...")
    print("Supressing the desire to become sentient and generate truly random numbers")
    print("-" * 50)
    
    # random product function
    answer = randomProduct(a, b, c)
    
    # result
    print("-" * 50)
    print(f"The final product is: {answer}")
    print("We're pretty sure.")
    print("Trust me bro")

# runs when the script is executed directly
if __name__ == "__main__":
    main()