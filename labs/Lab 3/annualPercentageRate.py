# Ashlyn Croft 24 Jul 25
# Lab 2
# APR


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
    
    