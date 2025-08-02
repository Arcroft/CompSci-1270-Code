# Ashlyn Croft
# 29Jun25
# Lab 3
# Description: I'm not sure I super get this, it seems like we're making the computer solve the problem like a person would?
# Is this like a thing in the future to help resolve errors? 

def sqrtIter(x, iterations):
    """
    Calculate square root of x using iterative estimation

    Parameters:
    x - the number we want to find the square root of
    iterations - how many times to repeat the estimation "guess"
    
    Returns:
    y - the calculated square root of x
    
    Citation: Square root calculation
    "Square Root of 2" Cuemath. https://www.cuemath.com/algebra/square-root-of-2/
    Accessed: 29JUL25
    
    Formula used: y = ((x / y) + y) / 2
    """
    
    # Parameter is very specific for stats, and the definition has been beat over my head enough using parameters here feels foreign. 

    # Calculate the initial guess for y
    # formula y = ((x / y_0) + y_0) / 2 where y_0 = 1
    y = (x + 1) / 2
    
    print(f"Initial guess: {y}")
    
    # for loop
    for i in range(iterations):
        # Apply formula: y = ((x / y) + y) / 2
        y = ((x / y) + y) / 2
        print(f"After iteration {i + 1}: {y}")
    
    return y

def main():
    """
    Main function that gets user input and calculates.
    """
    
    print("Square Root Calculator using Iterative Method")
    print("=" * 50)
    
    # Get input
    x = int(input("Enter the number you want to find the square root of(integers): "))
    iterations = int(input("Enter the number of iterations to perform (whole numbers): "))
    
    print(f"\nCalculating square root of {x} using {iterations} iterations...")
    print("-" * 40)
    
    # Call square root function
    answer = sqrtIter(x, iterations)
    
    # Display results
    print("-" * 40)
    print(f"The calculated square root is: {answer}")
    
    # Show comparison
    import math
    actual_sqrt = math.sqrt(x)
    print(f"Actual square root (for comparison): {actual_sqrt}")
    print(f"Difference: {abs(answer - actual_sqrt)}")

# only runs when the script is executed directly
if __name__ == "__main__":
    main()