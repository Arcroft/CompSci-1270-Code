# Ashlyn Croft 24 Jul 25
# Lab 2
# Calculate Resistance


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


