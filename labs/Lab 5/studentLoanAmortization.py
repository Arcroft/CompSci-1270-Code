# Ashlyn Croft
# 5 Jul 25
# Lab 5
# Student Loan Amortization
# shows how loan payments are split between interest and principal over time

def studentLoanAmortization(principal, yearlyInterestRate, numberOfYears):
    """
    Calculate and print the amortization schedule for a student loan.
    
    principal - the initial loan amount (float)
    yearlyInterestRate - annual interest rate as decimal (e.g., 0.05 for 5%)
    numberOfYears - loan term in years (int)
    
    Prints amortization table
    """
    
    # Convert to monthly values
    monthlyInterestRate = yearlyInterestRate / 12
    numberOfPayments = numberOfYears * 12
    
    # Calculate monthly payment using standard formula
    # M = P * [r(1+r)^n] / [(1+r)^n - 1]
    if monthlyInterestRate == 0:
        # incase 0 is input
        monthlyPayment = principal / numberOfPayments
    else:
        monthlyPayment = principal * (monthlyInterestRate * (1 + monthlyInterestRate)**numberOfPayments) / ((1 + monthlyInterestRate)**numberOfPayments - 1)
    
    # header information
    print(f"\nStudent Loan Amortization Schedule")
    print(f"=" * 50)
    print(f"Loan Amount: ${principal:,.2f}")
    print(f"Annual Interest Rate: {yearlyInterestRate * 100:.2f}%")
    print(f"Loan Term: {numberOfYears} years ({numberOfPayments} payments)")
    print(f"Monthly Payment: ${monthlyPayment:.2f}")
    print(f"Total Amount Paid: ${monthlyPayment * numberOfPayments:,.2f}")
    print(f"Total Interest Paid: ${(monthlyPayment * numberOfPayments) - principal:,.2f}")
    print()
    
    # table header
    print(f"{'Period':<8} {'Total Payment':<15} {'Interest Due':<15} {'Principal Due':<15} {'Principal Balance':<18}")
    print("-" * 75)
    
    # remaining balance
    remainingBalance = principal
    
    # print each payment period
    for period in range(1, numberOfPayments + 1):
        # interest due this period
        interestDue = remainingBalance * monthlyInterestRate
        
        # principal due this period
        principalDue = monthlyPayment - interestDue
        
        # Update remaining balance
        remainingBalance = remainingBalance - principalDue
        
        # Handle potential floating point issues for final payment
        if remainingBalance < 0.01:
            remainingBalance = 0.00
        
        # this period's information
        print(f"{period:<8} ${monthlyPayment:<14.2f} ${interestDue:<14.2f} ${principalDue:<14.2f} ${remainingBalance:<17.2f}")
    
    print("-" * 75)
    print("Amortization schedule complete? Wait, no, it is done. My bad. Wait... Okay, yup. Good to go. ...probably.")

def main():
    """
    get user input and generates the amortization schedule.
    """
    
    print("Student Loan Amortization Calculator")
    print("=" * 40)
    print("This calculator shows how your loan payments")
    print("are split between interest and principal over time.")
    print()
    
    try:
        # Get input from user
        principal = float(input("Enter the loan amount (principal): $"))
        yearlyInterestRate = float(input("Enter the annual interest rate as decimal (e.g., 0.05 for 5%): "))
        numberOfYears = int(input("Enter the loan term in years: "))
        
        # Validate input
        if principal <= 0:
            print("Error: Loan amount must be positive!")
            return
        if yearlyInterestRate < 0:
            print("Error: Interest rate cannot be negative!")
            return
        if numberOfYears <= 0:
            print("Error: Loan term must be positive!")
            return
        
        # Call amortization function
        studentLoanAmortization(principal, yearlyInterestRate, numberOfYears)
        
    except ValueError:
        print("Error: Please enter valid numbers!")
        print("Loan amount and interest rate should be decimal numbers.")
        print("Number of years should be a whole number.")

if __name__ == "__main__":
    main()

    # I'm utterly exhausted and have little spark for sassafrass in my code.