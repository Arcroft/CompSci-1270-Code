# Ashlyn Croft 24 Jul 25
# Lab 2
# Calculate Voltage


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
