# Ashlyn Croft 24 Jul 25
# Lab 2
# APR
# citation for apr feels unneeded
# https://www.capitalone.com/learn-grow/money-management/how-to-calculate-apr-on-credit-card/
# accessed: 24 Jun 25

try:
    principal = int(input("Enter principal amount (whole dollars): "))
    interest = int(input("Enter total interest paid over lifetime of loan (whole dollars): "))
    fees = int(input("Enter the fees associated (whole dollars): "))
    length = int(input("Enter the number of days in loan term: "))
    
    apr = ((interest + fees) / principal) * (365 / length) * 100
    
    print(f"The APR comes out to {apr:.2f}%")
    
except ValueError:
    print("Please restart and enter valid numbers only")

