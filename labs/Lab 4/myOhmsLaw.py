# Ashlyn Croft
# 1 Jul 25
# Lab 4
# Centralizing Ohms Law functions


## Solving for Voltage

def calculateVoltage(current, resistance):
    ""
    # I'm doing these reverse order, just swapping around values for voltage/resistance/current. Nothing special.
    # https://study.com/academy/lesson/flow-of-electric-charge-equation-application.html
    # accessed 29Jul 25
    # Just copy and pasting info in these sections, updating date
    ""
    voltage = current * resistance
    return voltage

def main():
    try:
        current = float(input("Input the current value: "))
        resistance = float(input("Input the resistance level: "))

        # Caaaaaalllll
        answer = calculateVoltage(current, resistance)

        # Result
        print(answer)
    except ValueError:
        print("Please enter the right numbers and try, try again.")

if __name__ == "__main__":
    main()



## Solving for Resistance

def calculateResistance(current, voltage):
    ""
    # https://study.com/academy/lesson/flow-of-electric-charge-equation-application.html
    # accessed 24 Jul 25
    ""
    resistance = voltage / current
    return resistance

def main():
    try:
        current = float(input("Input the current value: "))
        voltage = float(input("Input the voltage level: "))

        # Call (is coming from inside the house)
        answer = calculateResistance(current, voltage)

        # Results
        print(answer)

    except ValueError:
        print("You for realz-y gotta use the correct values")

if __name__ == "__main__":
    main()



## Solve for Current

def calculateCurrent(resistance, voltage):
    ""
    # https://study.com/academy/lesson/flow-of-electric-charge-equation-application.html
    # accessed 29Jul 25
    # Feel like I'm starting to get sloppy
    ""
    current = voltage/ resistance
    return current

def main():
    try:
        resistance = float(input("Input the resistence value: "))
        voltage = float(input("Input the voltage level: "))

        # Ring Ring
        answer = calculateCurrent(resistance, voltage)

        # Resalts
        print(answer)

    except ValueError:
        print("Now what you entering nonsense to break my code for?")

if __name__ == "__main__":
    main()
