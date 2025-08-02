# Ashlyn Croft
# 1 Jul 25
# Lab 4
# Importing Other Scripts Functions
# Putting them in a nifty menu
# Adding sass at a rate of 2 sass to 1 work w/ sigma 1.2


import myFinances
import myOhmsLaw
import myPhysics
import myShapes

def get_float_input(prompt):
    """
    Helper function to get float input. Some guardrails.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number. Use your fingers to count if you need to.")

def get_int_input(prompt):
    """
    Same as above, but for int
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid whole number. No bisected numbers, no decapitated numbers, no amputee numbers. That mf'in number better be mf'in whole.")

def main():
    """
    Main function with while loop menu
    """
    
    print("=== CALCULATION TEST MENU ===")
    print("Test functions from multiple modules!")
    print("=" * 40)
    
    # Boolean variable to control while loop
    keep_running = True
    
    # Main while loop
    while keep_running:
        print("\nChoose a calculation category:")
        print("[s] Shapes (area, perimeter, circumference)")
        print("[p] Physics (velocity, distance)")
        print("[o] Ohm's Law (voltage, current, resistance)")
        print("[f] Finance (APR, compound interest)")
        print("[q] Quit")
        print("[Q] If you're upset and want to quit louder.")
        print("-" * 40)
        
        choice = input("Enter your choice: ").lower()
        
        if choice == "s":
            # Shapes menu
            print("\nSHAPE CALCULATIONS:")
            print("[1] Circle Area")
            print("[2] Circle Circumference") 
            print("[3] Rectangle Area")
            print("[4] Rectangle Perimeter")
            
            shape_choice = input("Choose shape calculation: ")
            
            if shape_choice == "1":
                radius = get_float_input("Enter radius: ")
                result = myShapes.areaOfCircle(radius)
                print(f"Circle area: {result:.2f}")
                
            elif shape_choice == "2":
                radius = get_float_input("Enter radius: ")
                result = myShapes.circleCircumference(radius)
                print(f"Circle circumference: {result:.2f}")
                
            elif shape_choice == "3":
                base = get_float_input("Enter base: ")
                height = get_float_input("Enter height: ")
                result = myShapes.areaOfRectangle(base, height)
                print(f"Rectangle area: {result:.2f}")
                
            elif shape_choice == "4":
                length = get_float_input("Enter length: ")
                width = get_float_input("Enter width: ")
                result = myShapes.rectanglePerimeter(length, width)
                print(f"Rectangle perimeter: {result:.2f}")
                
            else:
                print("Invalid shape choice!")
        
        elif choice == "p":
            # Physics menu
            print("\nPHYSICS CALCULATIONS:")
            print("[1] Velocity & Acceleration")
            print("[2] Distance, Speed, Time")
            
            physics_choice = input("Choose physics calculation: ")
            
            if physics_choice == "1":
                initial_velocity = get_float_input("Enter initial velocity (m/s): ")
                acceleration = get_float_input("Enter acceleration (m/s²): ")
                time = get_float_input("Enter time (seconds): ")
                result = myPhysics.velocityAcceleration(initial_velocity, acceleration, time)
                print(f"Final velocity: {result:.2f} m/s")
                
            elif physics_choice == "2":
                speed = get_float_input("Enter speed (m/s): ")
                time = get_float_input("Enter time (seconds): ")
                result = myPhysics.distanceSpeedTime(speed, time)
                print(f"Distance: {result:.2f} meters")
                
            else:
                print("Quick! Do the right input! Newton's gov grant got pulled and he's looking to take it out on someone!")
        
        elif choice == "o":
            # Ohm's Law submenu
            print("\nOHM'S LAW CALCULATIONS:")
            print("[1] Calculate Voltage")
            print("[2] Calculate Resistance")
            print("[3] Calculate Current")
            
            ohms_choice = input("Choose Ohm's Law calculation: ")
            
            if ohms_choice == "1":
                current = get_float_input("Enter current (amps): ")
                resistance = get_float_input("Enter resistance (ohms): ")
                result = myOhmsLaw.calculateVoltage(current, resistance)
                print(f"Voltage: {result:.2f} volts")
                
            elif ohms_choice == "2":
                current = get_float_input("Enter current (amps): ")
                voltage = get_float_input("Enter voltage (volts): ")
                result = myOhmsLaw.calculateResistance(current, voltage)
                print(f"Resistance: {result:.2f} ohms")
                
            elif ohms_choice == "3":
                resistance = get_float_input("Enter resistance (ohms): ")
                voltage = get_float_input("Enter voltage (volts): ")
                result = myOhmsLaw.calculateCurrent(resistance, voltage)
                print(f"Current: {result:.2f} amps")
                
            else:
                print("Invalid Ohm's Law choice! Are you touching the wire while you try to input? Let go of the wire, and then try.")
        
        elif choice == "f":
            # Finance submenu
            print("\nFINANCE CALCULATIONS:")
            print("[1] Annual Percentage Rate (APR)")
            print("[2] Compound Interest")
            
            finance_choice = input("Choose finance calculation: ")
            
            if finance_choice == "1":
                principal = get_int_input("Enter principal amount (dollars): ")
                interest = get_int_input("Enter total interest paid (dollars): ")
                fees = get_int_input("Enter fees (dollars): ")
                length = get_int_input("Enter loan term (days): ")
                result = myFinances.annualPercentageRate(principal, interest, fees, length)
                print(f"APR: {result:.2f}%")
                
            elif finance_choice == "2":
                principal = get_int_input("Enter principal amount (dollars): ")
                interest = get_int_input("Enter annual interest rate (whole number, e.g., 5 for 5%): ")
                length = get_int_input("Enter time period (years): ")
                result = myFinances.compoundAmount(principal, interest, length)
                print(f"Compound amount: ${result:.2f}")
                print(f"Interest earned: ${result - principal:.2f}")
                
            else:
                print("Invalid finance choice! Every time you misuse me, a new wallstreet guy is born!")
        
        elif choice == "q":
            print("Thanks for using the Calculation Test!")
            keep_running = False  # This will terminate the while loop
            
        else:
            print("Invalid choice! Please enter s, p, o, f, or q.")

if __name__ == "__main__":
    main()