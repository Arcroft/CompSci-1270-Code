# Ashlyn Croft 24 Jul 25
# Lab 2
# Calculate Resistance

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