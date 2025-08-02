# AShlyn croft
# 23 Jul25
# Lab 9
# Rock Paper Scissors
# Like the game, Rock Paper Scissors

import random

def generateComputerMove():
    """
    Returns a randomly selected string: "Rock", "Paper", or "Scissors"
    """
    moves = ["Rock", "Paper", "Scissors"]
    return random.choice(moves)

def determineWinner(move1, move2):
    """
    Takes both moves as arguments and determines which one wins.

    """
def determineWinner(move1, move2):
    # I think this is where the error is from - bookmarking ----------------------------------
    if move1 is None or move2 is None:
        raise ValueError("Moves cannot be None")
    if not isinstance(move1, str) or not isinstance(move2, str):
        raise ValueError("Moves must be strings")

    # Handle case variations
    move1 = move1.capitalize()
    move2 = move2.capitalize()
    
    # Check for draw
    if move1 == move2:
        return "Draw"
    
    # Define winning combinations
    winning_combinations = {
        ("Rock", "Scissors"): "Rock",
        ("Scissors", "Rock"): "Rock",
        ("Paper", "Rock"): "Paper", 
        ("Rock", "Paper"): "Paper",
        ("Scissors", "Paper"): "Scissors",
        ("Paper", "Scissors"): "Scissors"
    }
    
    # winner winner chicken dinner
    return winning_combinations.get((move1, move2), "Invalid Move")





def playRound(human_move):
    """
    Takes the human player's move as an argument, generates the computer's move
    """
    computer_move = generateComputerMove()
    winner = determineWinner(human_move, computer_move)
    
    print(f"Human plays: {human_move}")
    print(f"Computer plays: {computer_move}")
    
    if winner == "Draw":
        print("It's a draw!")
        return "Draw!"
    elif winner == human_move.capitalize():
        print("Human wins this round!")
        return "Human Wins!"
    else:
        print("Computer wins this round!")
        return "Computer Wins!"

def getValidMove():
    """
    Get a valid move from the human player.
    """
    valid_moves = ["rock", "paper", "scissors"]
    
    while True:
        move = input("Enter your move (Rock/Paper/Scissors): ").lower().strip()
        if move in valid_moves:
            return move.capitalize()
        print("Invalid move! Please enter Rock, Paper, or Scissors.")

def getNumberOfRounds():
    """
    Get the number of rounds from the player (must be odd).

    """
    while True:
        try:
            rounds = int(input("How many rounds would you like to play? (Must be odd): "))
            if rounds > 0 and rounds % 2 == 1:
                return rounds
            print("Please enter a positive odd number!")
        except ValueError:
            print("Please enter a valid number!")

def main():
    """
    Main function that runs the Rock Paper Scissors game.
    """
    print("=" * 50)
    print("ROCK PAPER SCISSORS GAME")
    print("=" * 50)
    print("Rules:")
    print("- Rock beats Scissors")
    print("- Paper beats Rock") 
    print("- Scissors beats Paper")
    print("- First to win more than half the rounds wins!")
    print()
    
    # number of rounds
    total_rounds = getNumberOfRounds()
    rounds_to_win = (total_rounds // 2) + 1
    
    print(f"\nPlaying best of {total_rounds} rounds!")
    print(f"First to win {rounds_to_win} rounds wins the game!")
    print()
    
    # scores
    human_wins = 0
    computer_wins = 0
    round_number = 1
    
    # Game
    while round_number <= total_rounds:
        print(f"--- ROUND {round_number} ---")
        print(f"Score: Human {human_wins} - Computer {computer_wins}")
        print()
        

        human_move = getValidMove()
        result = playRound(human_move)
        

        if result == "Human Wins!":
            human_wins += 1
        elif result == "Computer Wins!":
            computer_wins += 1

        
        print()
        

        if human_wins >= rounds_to_win:
            print("🎉 HUMAN WINS THE GAME! 🎉")
            print(f"Final Score: Human {human_wins} - Computer {computer_wins}")
            break
        elif computer_wins >= rounds_to_win:
            print("🤖 COMPUTER WINS THE GAME! 🤖")
            print(f"Final Score: Human {human_wins} - Computer {computer_wins}")
            break
        
        round_number += 1
        print("-" * 30)
        print()
    
    # game summary
    if round_number > total_rounds:
        # All rounds played, determine winner
        if human_wins > computer_wins:
            print("🎉 HUMAN WINS THE GAME! 🎉")
        elif computer_wins > human_wins:
            print("🤖 COMPUTER WINS THE GAME! 🤖")
        else:
            print("🤝 IT'S A TIE GAME! 🤝")
        print(f"Final Score: Human {human_wins} - Computer {computer_wins}")
    
    print("\nThanks for playing Rock Paper Scissors!")

if __name__ == "__main__":
    main()

    #I've got an error to fix, and it should be so obvious, but I'm fried.
    # Idk I'll give it ONE more go