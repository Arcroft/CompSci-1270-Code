# Ashlyn Croft 25 Jul 25
# Lab 2
# Distance relative to time and speed
# This and velocityaccelaration left
# ugh, I started with the interesting one first
# bleeeehhhhh


def distanceSpeedTime(speed, time):
    ""
     # https://www.calculatorsoup.com/calculators/math/speed-distance-time-calculator.php
    # updated 21 Oct 23
    # accessed 29jun25
    ""
    distance = speed * time
    return distance

def main():
    try:
        speed = float(input("Speed (Meters Per Second): "))
        time = float(input("Time (Seconds): "))

        #Call
        answer = distance = speed * time

        # Result
        print(answer)

    except ValueError:
        print("Please restart with valid numbers")

if __name__ == "__main__":
    main()



