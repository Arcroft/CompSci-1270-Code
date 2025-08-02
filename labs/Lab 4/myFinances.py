# Ashlyn Croft
# 1 Jul 25
# Lab 4
# Centralizing FInance Functions



## APR

def annualPercentageRate(principal, interest, fees,length):
    ""
    # citation for apr feels unneeded
    # https://www.capitalone.com/learn-grow/money-management/how-to-calculate-apr-on-credit-card/
    # accessed: 24 Jun 25
    ""
    apr = ((interest + fees) / principal) * (365 / length) * 100
    return apr

def main():
    try:
        principal = int(input("Enter principal amount (whole dollars): "))
        interest = int(input("Enter total interest paid over lifetime of loan (whole dollars): "))
        fees = int(input("Enter the fees associated (whole dollars): "))
        length = int(input("Enter the number of days in loan term: "))
    
        #Call
        answer = annualPercentageRate(principal, interest, fees, length)

        # Results
        print(f"The APR comes out to {answer:.2f}%")

    except ValueError:
        print("This is my last code to write tonight, please stop breaking it/n" \
        "I have at least one math, a paper, or code assignment/n" \
        "due every single day. I'm so tired. /n" \
        "all I do is learn all day. Like an idiot.")

if __name__ == "__main__":
    main()





## Compounding Function

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