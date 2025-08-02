# Ashlyn Croft
# 1 Jul 25
# Lab 4
# Adventure Story - Interactive zombie survival story using if statements and user input

# I'd like to explore how I can create a character inventory, which probaby would be a similar process to a HUD.
# But, 1,000 things to do. Time to do 10.

def main():
    """
    Interactive adventure story about zombie survival.
    """
    
    # Story introduction
    print("=== THE SPOOKIN ===")
    print("By: Ashlyn Croft")
    print()
    print("Disclaimer: this is just proof of concept, and doesn't have all the routes mapped out. It's not a full game, it's a homework assignment when I'm pulling 9am-2am days most days on school work.")
    print()
    print("The news stories didn't seem quite real at first... zombies, really?")
    print("It started to feel real, but distant, when the national guard was mobilized and curfew enacted.")
    print("Then came the first night with screams, drowned out by gunfire the next.")
    print("You missed the evacuation. Good thing, because the noise of the 'safe zone' drew the horde.")
    print("Stuck in middle American suburbia as keeping up with the Joneses")
    print("becomes outrunning what WERE the Joneses.")
    print()
    print("This is how you died...")
    print()
    
    # First choice - Starting location
    print("You're standing in your single story home's kitchen - every window covered in heavy curtains.")
    print("There's an incredibly soft wet thump coming from your bathroom.")
    print()
    first_choice = input("Do you: Check for [s]upplies in the kitchen, look in the [b]athroom, or head to the [m]aster bedroom? ").lower()
    
    # IF STATEMENT 1: First major path choice
    if first_choice == "s":
        # Kitchen supplies path
        print()
        print("You search through the kitchen drawers and cabinets.")
        print("You find several useful items scattered around.")
        print()
        supply_choice = input("Do you take the [k]itchen knife, your [c]ar keys, or investigate the dog [t]oy (wait, you don't have a dog...)? ").lower()
        
        # IF STATEMENT 2: Kitchen supplies choice
        if supply_choice == "k":
            print()
            print("You grab the kitchen knife. It feels reassuring in your hand. Like you can stab someone in the face, or cut the crust off a sandwhich.")
            
        elif supply_choice == "c":
            print()
            print("Smart choice! You grab your car keys.")
            print("The soft thump from the bathroom suddenly gets MUCH louder.")
            print("You hear the sound of breaking glass!")
            print("Without hesitation, you bolt for the garage and your car.")
            
        elif supply_choice == "t":
            print()
            print("Why the hell is there a dog toy in my kitchen?")
            print("*SQUEAK*")
            print("You turn around to see a'rot'weiler staring at you with hungry eyes.")
            print("His idea of what constitutes fetch might be incompatible with yours.")
            
        else:
            print("Invalid choice! How do you think you'd survive if you can't follow instruction?")
            print("Game Over!")
    
    elif first_choice == "b":
        # Bathroom investigation path
        print()
        print("As you creak open the door to the bathroom, you can see through the heavy curtain")
        print("a shadow that grows, fades, and grows along with the wet thump.")
        print()
        bathroom_choice = input("Do you [l]eave immediately or [p]ull back the curtain? ").lower()
        
        # IF STATEMENT 3: Bathroom investigation choice
        if bathroom_choice == "l":
            print()
            print("Wise choice! You slowly back away from the bathroom.")
            print("As you retreat, you hear the wet thumping get more frantic.")
            
        elif bathroom_choice == "p":
            print()
            print("You pull back the curtain, heart freezing as you jump at the sight of")
            print("a human face inches from your own. That jogger lady... what was her name?")
            print("She always waved with that big 'everything's okay' smile.")
            print("There's a small, bloody spot on her forehead from hitting the window.")
            print("Then her pretty sky-blue eyes meet yours.")
            print()
            face_choice = input("Do you [a]sk what her name is, [s]cream, [r]un, or [p]olitely say goodbye? ").lower()
            
            # IF STATEMENT 4: Face-to-face encounter choice
            if face_choice == "p":
                print()
                print("'Excuse me, I'm terribly sorry to bother you, but I really must be going.'")
                print("You politely back away from the window.")
                print("The last thing you see before you close and latch the door is her wave.")
                
            else:
                print()
                print("Your reaction triggers the predator-prey response!")
                print("The window explodes inward as the zombie crashes through!")
                print("In the struggle that follows, you realize this is how your story ends.")
                print("Game Over! Sometimes fight or flight just isn't enough.")
        
        else:
            print("Invalid choice! While you stood there confused, the window broke!")
            print("Game Over!")
    
    elif first_choice == "m":
        # Master bedroom path
        print()
        print("You head toward the master bedroom, staying low and quiet.")
        print("As you enter, you notice the bedroom window is slightly open.")
        print("There's a low moaning sound coming from outside.")
        print()
        bedroom_choice = input("Do you [c]lose the window, [h]ide under the bed, or [l]ook outside? ").lower()
        
        # IF STATEMENT 5: Master bedroom choice
        if bedroom_choice == "c":
            print()
            print("You quietly close and lock the window.")
            print("The moaning outside continues for a while, then gradually fades away.")
            print("You wait in silence for what feels like hours.")
            print("Zombies are bad enough, now you're not a target for burglers.")
            
        elif bedroom_choice == "h":
            print()
            print("You dive under the bed just as shadows pass by the window.")
            print("You hold your breath as footsteps shuffle around outside.")
            print("After what feels like an eternity, the sounds fade away.")
            print("Chalk one up for cowardice!")

        elif bedroom_choice == "l":
            print()
            print("You peek through the curtains and immediately wish you hadn't.")
            print("There's a small crowd of zombies wandering through your neighbor's yard.")
            print("One of them notices movement at your window and shifts it's shambling gate towards you")
            print("He's wearing a Neighborhood Watch shirt, so you sigh in relief at good fortune.")
            
        else:
            print("Invalid choice! While you hesitated, they noticed you!")
            print("Game Over!")
    
    else:
        print("Invalid choice! While you stood there confused, something found you!")
        print("Possibly a realtor checking which houses have the least corpses for an easy flip.")
        print("Game Over!")

if __name__ == "__main__":
    main()