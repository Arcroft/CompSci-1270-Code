# Ashlyn Croft 29Jul25
# Lab 3
# Let's see if I have any idea what I'm doing

# Compound Amount PY
# PERT - Percentage Return over Time
# First assignment, so it gets more tender loving care than the ones I'm just ready to be done with
# Citation for PERT feels wildly unnecessary, but


def compoundAmount(principal, interest, length):
    ""
    # https://www.mathwords.com/c/continuously_compounded_interest.htm
    # updated 15 JUL 23
    # Accessed 29JUL 25
    ""
    accrued = principal * (1 + (interest/100)) ** length
    return accrued

def main():
    try: 
        principal = int(input("Enter principal amount (whole dollars): "))
        interest = int(input("Enter annual interest rate (whole number, e.g., 5 for 5%): "))
        length = int(input("Enter time period (years): "))

        # Call
        answer = compoundAmount(principal, interest, length)

        # Results
        print(f"This compounds to ${answer:.2f}")
        print(f"You've made ${answer - principal:.2f} in interest.")
    except ValueError:
        print("Please restart and enter valid numbers only.")

if __name__ == "__main__":
     main()



   
    
   
    
   




# Used some things we havn't covered that I've found trying to find ways to write neater/cleaner code
# Like the f formatted string piece w/ curly brackets. I was doing it str(int variable) in print
# The .2f was trying to figure out how to do decimals. .Xf is how many decimal places. Standard for statisticians is 2.
# I'm not sure how yet, but I think this will be helpful for summary statistics. 

## This is how it'd look in R
# This feels more intuitive than R

## Get user input
# principal <- as.numeric(readline("Enter principal amount (whole dollars): "))
# interest <- as.numeric(readline("Enter annual interest rate (whole number, e.g., 5 for 5%): "))
# length <- as.numeric(readline("Enter time period (years): "))

## Calculate compound interest
# accrued <- principal * (1 + (interest/100)) ^ length

## Display results
# cat("This compounds to $", sprintf("%.2f", accrued), "\n")
# cat("You've made $", sprintf("%.2f", accrued - principal), " in interest.\n")