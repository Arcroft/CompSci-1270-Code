# Ashlyn Croft
# 7JUL25
# Assignment 3
# Nimbrab - trying to not take the last "one"

import random

def displayRules():
    """
    Display the rules of NIMGRAB! to the player.
    """
    print("\n" + "="*50)
    print("NIMGRAB! RULES")
    print("="*50)
    print("OBJECTIVE:")
    print("  Avoid being the player who takes the very last item!")
    print()
    print("HOW TO PLAY:")
    print("  • The game starts with a row of items (usually 20-25)")
    print("  • Players take turns removing items from the row")
    print("  • On each turn, you must take between 1 and 3 items")
    print("  • You cannot take more items than are currently available")
    print("  • The player who is forced to take the last item LOSES!")
    print()
    print("STRATEGY TIP:")
    print("  Think ahead! Try to leave your opponent in a position")
    print("  where they'll be forced to take the last item.")
    print("="*50)
    print("Interestingly, this a common conman bar trick")

# Apparently I can use bullet points?!

def getPlayerMove(itemsRemaining, playerName):
    """
    Get a valid move from a human player.
    
    itemsRemaining - number of items currently in the row (int)
    playerName - name of the current player (string)
    
    Returns the number of items the player wants to take (int)
    """
    minTake = 1
    maxTake = min(3, itemsRemaining)  # Can't take more than available
    
    while True:
        try:
            print(f"\n{playerName}, there are {itemsRemaining} items remaining.")
            print("Items: " + "* " * itemsRemaining)
            
            if maxTake == 1:
                print("You must take the last item. You lose!")
                return 1
            
            choice = int(input(f"How many items do you want to take? ({minTake}-{maxTake}): "))
            
            if choice < minTake or choice > maxTake:
                print(f"Error: You must take between {minTake} and {maxTake} items!")
                continue
            
            return choice
            
        except ValueError:
            print("Error: Please enter a valid number!")

def getComputerMove(itemsRemaining):
    """
    Calculate the computer's move using basic strategy.
    
    itemsRemaining - number of items currently in the row (int)
    
    Returns the number of items the computer will take (int)
    """
    minTake = 1
    maxTake = min(3, itemsRemaining)
    
    # If only one item left, computer must take it (and lose)
    if itemsRemaining == 1:
        return 1
    
    # Avoid losing moves - don't leave exactly 1 item if possible
    # If taking maxTake would leave exactly 1 item, take one less
    if itemsRemaining - maxTake == 1 and maxTake > 1:
        choice = maxTake - 1
    else:
        # Otherwise, take a random valid amount
        choice = random.randint(minTake, maxTake)

# There's a strat for this, and if the 4th didn't prevent me from sleeping at all and I can feel entropy actively behind my eyes
# The computer can pretty easily be unbeatable.
# Iirc, it's related to keeping the number odd or even depending on if you're 1st or 2nd player

    
    print(f"\nComputer takes {choice} item{'s' if choice != 1 else ''}.")
    return choice

def playGame(gameMode):
    """
    Main game logic for NIMGRAB!
    
    gameMode - either "1" for single player or "2" for two player (string)
    """
    print("\n" + "="*40)
    print("STARTING NEW GAME")
    print("="*40)
    


    # Setup game
    itemsRemaining = random.randint(20, 25)
    print(f"Starting with {itemsRemaining} items in the row!")
    
    if gameMode == "1":
        players = ["You", "Computer"]
        currentPlayer = 0  # Human goes first
    else:
        player1 = input("Enter name for Player 1: ").strip() or "Player 1"
        player2 = input("Enter name for Player 2: ").strip() or "Player 2" 
        players = [player1, player2]
        currentPlayer = 0  # Player 1 goes first
    

    # Game loop
    while itemsRemaining > 0:
        if gameMode == "1" and currentPlayer == 1:  # Computer's turn
            itemsTaken = getComputerMove(itemsRemaining)
        else:  # Human player's turn
            itemsTaken = getPlayerMove(itemsRemaining, players[currentPlayer])
        
        itemsRemaining -= itemsTaken
        
        # Check for game over
        if itemsRemaining == 0:
            print(f"\n{players[currentPlayer]} took the last item and LOSES!")
            if gameMode == "1":
                if currentPlayer == 0:
                    print("Computer wins! Better luck next time!")
                else:
                    print("Congratulations! You beat the computer!")
            else:
                winner = players[1 - currentPlayer]  # The other player wins
                print(f"Congratulations {winner}! You win!")
            break
        
        # Switch to next player
        currentPlayer = 1 - currentPlayer
    
    print("\nGame Over!")



def displayMenu():
    """
    Display the main menu and get user's choice.
    
    Returns the user's menu choice (string)
    """
    print("\n" + "="*40)
    print("NIMGRAB! - MAIN MENU")
    print("="*40)
    print("1. Play Game (1 Player vs Computer)")
    print("2. Play Game (2 Players)")
    print("3. View Rules")
    print("4. Quit")
    print("-"*40)

    
    while True:
        choice = input("Please select an option (1-4): ").strip()
        if choice in ["1", "2", "3", "4"]:
            return choice
        print("Error: Please enter 1, 2, 3, or 4!")

def main():
    """
    Main program function that handles menu navigation.
    """
    print("="*50)
    print("NIMGRAB!")
    print("Ashlyn Croft - Adventures in overfull plates and underfilled sanity.")
    print("="*50)
    print("Welcome to NIMGRAB! - The ultimate strategy game!")
    print("Can you avoid taking the last item?")
    
    while True:
        choice = displayMenu()
        
        if choice == "1":
            playGame("1")
        elif choice == "2":
            playGame("2")
        elif choice == "3":
            displayRules()
        elif choice == "4":
            print("\nThanks for playing NIMGRAB!")
            break

if __name__ == "__main__":
    main()