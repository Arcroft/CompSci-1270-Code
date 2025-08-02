# Ashlyn Croft 27JUN25
# Assignment 2
# Lucky Calculator
# I'm actually proud of this one. I sepnt a lot of time trying to break it, and then
# building rails to prevent breaking. (In the ways I know how)

print("Welcome to Lucky Calculator!\n"
    "By Ashlyn Croft \n"
    "Com S 127 - A \n ")


import random
import operator

def c(): # Calculator
    print("C-C-Calculator Mooode!")
    operation = input("Choose +, -, *, /, //, %, **, or l for lucky: ")

    if operation == "l":
        lucky = l() #calling lucky function
        print(f"Your lucky number is: {lucky}")
    else:
        num1 = input("First number: (or l for lucky)")
        if num1 == "l":
            num1 = l()
            print(f"Using lucky number: {num1}")
        else:
            num1 = float(num1)

        num2 = input("Second number: (or l for lucky)")
        if num2 == "l":
            num2 = l()
            print(f"Using lucky number: {num2}")
        else: num2 = float(num2)


        # Dictionary map - googlin so I don't have to do 500 if = X
        ops = {
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.truediv,
            '//': operator.floordiv,
            '%': operator.mod,
            '**': operator.pow
        }

        # Divide by zero issue
        if operation in ['/', '//', '%'] and num2 == 0:
            print("Cannot divide by zero")
            while True:
                try:
                    num2 = float(input("Second number: "))
                    if num2 == 0:
                        print("That's still zero!")
                        continue
                    else:
                        break

                except ValueError:
                    print("Invalid Operation! Do not pass go, do not collect $200!")
                

        if operation in ops:
            answer = ops[operation](num1, num2)
            print(f"Result: {answer}")
        
        else:
            print("Invalid Operation! Do not pass go, do not collect $200!")

def l(): # Lucky
    lucky = random.randint(1, 100)
    print(lucky)
    return lucky

def q(): # Quit
    print("Lator Gator!")
    exit()

# Non function stuffs
while True:
    choice = input("Select [c]alculator, [l]ucky number, or [q]uit: ").lower()
    if choice == "c":
        c()
    elif choice == "l":
        l()
    elif choice == "q":
        q()
    else:
        print("Wut?")
    