# Ashlyn Croft
# 1 Jul 25
# Lab 4
# Description: Tests if a year is a leap year.

def findLeapYear(year):
    """
    Determine if a given year is a leap year.
    """
    
    # divisible by 400 first
    if year % 400 == 0:
        return True
    
    # divisible by 100 but not 400, NOT a leap year
    elif year % 100 == 0:
        return False
    
    # divisible by 4 but not 100, IS a leap year
    elif year % 4 == 0:
        return True
    
    # not divisible by 4, NOT a leap year
    else:
        return False

def main():
    """
    Main function that gets user input year
    """
    
    print("Leap Year Calculator")
    print("=" * 20)
    
    # input from user
    year = int(input("Enter a year: "))
    
    # call function
    answer = findLeapYear(year)
    
    # Print results
    if answer:
        print(f"{year} is a leap year: YES")
    else:
        print(f"{year} is a leap year: NO")

if __name__ == "__main__":
    main()