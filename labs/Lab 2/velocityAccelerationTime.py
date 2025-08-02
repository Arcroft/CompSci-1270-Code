# Ashlyn Croft 24 Jul 25
# Lab 2
# Calculate Resistance

initial_velocity = float(input("Enter initial velocity (Meters Per Second):"))
acceleration = float(input("Enter the Accelertion (Meters Per Second Squared): "))
time = float(input("Enter the time elapsed (Seconds): "))
final_velocity = initial_velocity + (acceleration * time)
print(final_velocity)