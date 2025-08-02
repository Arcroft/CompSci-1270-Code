
# Ashlyn Croft 24 Jul 25
# Lab 2
# Calculate Current


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

