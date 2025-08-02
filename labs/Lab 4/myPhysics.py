# Ashlyn Croft
# 1 Jul 25
# Lab 4
# Centralizing Physics functions


## Velocity & Acceleration Function


def velocityAcceleration(initial_velocity, acceleration, time):
    ""
    # final_velocity = initial_velocity + (acceleration * time)
    # https://physics.info/motion-equations/
    # accessed 29Jul25
    ""
    final_velocity = initial_velocity + (acceleration * time)
    return final_velocity

def main():
    try:
        initial_velocity = float(input("Enter initial velocity (Meters Per Second):"))
        acceleration = float(input("Enter the Accelertion (Meters Per Second Squared): "))
        time = float(input("Enter the time elapsed (Seconds): "))

        #Call
        answer = velocityAcceleration(initial_velocity, acceleration, time)

        #Result
        print(answer)
    except ValueError:
        print("Please restart with valid numbers.")

if __name__ == "__main__":
    main()


## Distance = Speed * Time Function

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