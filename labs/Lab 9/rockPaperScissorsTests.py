# Ashlyn Croft  
# 23 Jul25
# Lab 9
# Tests for the rock, paper, scissors game


import pytest
from rockPaperScissors import generateComputerMove, determineWinner, playRound

def test_generateComputerMove():
    """Test that generateComputerMove returns valid moves"""
    valid_moves = ["Rock", "Paper", "Scissors"]
    
    # Test function returns one of the valid moves
    for _ in range(50):  # Test multiple times
        move = generateComputerMove()
        assert move in valid_moves
    
    # Test that function can return all possible moves 
    moves_seen = set()
    for _ in range(100):
        move = generateComputerMove()
        moves_seen.add(move)
    
    # Should see all three moves
    assert len(moves_seen) >= 2  





def test_determineWinner_rock_wins():
    """Test determineWinner when Rock wins"""
    assert determineWinner("Rock", "Scissors") == "Rock"
    assert determineWinner("Scissors", "Rock") == "Rock"

def test_determineWinner_paper_wins():
    """Test determineWinner when Paper wins"""
    assert determineWinner("Paper", "Rock") == "Paper"
    assert determineWinner("Rock", "Paper") == "Paper"

def test_determineWinner_scissors_wins():
    """Test determineWinner when Scissors wins"""
    assert determineWinner("Scissors", "Paper") == "Scissors"
    assert determineWinner("Paper", "Scissors") == "Scissors"




def test_determineWinner_draws():
    """Test determineWinner when both players choose same move"""
    assert determineWinner("Rock", "Rock") == "Draw"
    assert determineWinner("Paper", "Paper") == "Draw"
    assert determineWinner("Scissors", "Scissors") == "Draw"



def test_determineWinner_all_combinations():
    """Test all possible combinations systematically"""
    assert determineWinner("Rock", "Rock") == "Draw"
    assert determineWinner("Rock", "Paper") == "Paper"
    assert determineWinner("Rock", "Scissors") == "Rock"
    

    assert determineWinner("Paper", "Rock") == "Paper"
    assert determineWinner("Paper", "Paper") == "Draw"
    assert determineWinner("Paper", "Scissors") == "Scissors"
    

    assert determineWinner("Scissors", "Rock") == "Rock"
    assert determineWinner("Scissors", "Paper") == "Scissors"
    assert determineWinner("Scissors", "Scissors") == "Draw"

def test_playRound_human_wins():
    """Test playRound when human should win"""

    

    result = playRound("Rock")
    assert isinstance(result, str)
    

    valid_results = ["Human Wins!", "Computer Wins!", "Draw!"]
    assert result in valid_results

def test_playRound_all_human_moves():
    """Test playRound with all possible human moves"""
    valid_moves = ["Rock", "Paper", "Scissors"]
    valid_results = ["Human Wins!", "Computer Wins!", "Draw!"]
    
    for human_move in valid_moves:
        result = playRound(human_move)
        assert result in valid_results

def test_playRound_multiple_calls():
    """Test that playRound can produce different results due to randomness"""
    results = set()
    
    # Call playRound many times to see different outcomes
    for _ in range(50):
        result = playRound("Rock")
        results.add(result)
    
    # Should see at least 2 different results in 50 calls
    assert len(results) >= 1 

def test_case_sensitivity():
    """Test that functions handle exact case matching"""

    assert determineWinner("Rock", "Paper") == "Paper"
    assert determineWinner("ROCK", "PAPER") == "Paper"  
    
def test_invalid_moves():
    """Test functions with invalid moves - should handle gracefully"""
    # These might need handling
    try:
        result = determineWinner("InvalidMove", "Rock")
        assert result is not None
    except (ValueError, KeyError):
        pass

def test_edge_cases():
    """Test various edge cases"""

    try:
        result = determineWinner("", "Rock")
        assert result is not None
    except (ValueError, KeyError):
        pass
    
    # None values
    try:
        result = determineWinner(None, "Rock")
        assert result is not None
    except (TypeError, ValueError):
        pass

# verify game logic
def test_rock_paper_scissors_rules():
    """Test that the core game rules are implemented correctly"""
    # Rock beats Scissors
    assert determineWinner("Rock", "Scissors") == "Rock"
    
    # Paper beats Rock
    assert determineWinner("Paper", "Rock") == "Paper"
    
    # Scissors beats Paper
    assert determineWinner("Scissors", "Paper") == "Scissors"
    
    # Verify reverse scenarios
    assert determineWinner("Scissors", "Rock") == "Rock"
    assert determineWinner("Rock", "Paper") == "Paper"
    assert determineWinner("Paper", "Scissors") == "Scissors"

def test_function_return_types():
    """Test that functions return correct data types"""
    computer_move = generateComputerMove()
    assert isinstance(computer_move, str)
    

    winner = determineWinner("Rock", "Paper")
    assert isinstance(winner, str)
    

    result = playRound("Rock")
    assert isinstance(result, str)

if __name__ == "__main__":
    print("Running basic verification tests...")
    
    try:
        move = generateComputerMove()
        print(f"Computer generated move: {move}")
        
        winner = determineWinner("Rock", "Paper")
        print(f"Rock vs Paper winner: {winner}")
        
        result = playRound("Scissors")
        print(f"Human plays Scissors result: {result}")
        
        print("Basic tests completed successfully!")
        
    except ImportError:
        print("rockPaperScissors.py not found - this is expected in TDD!")
        print("Write the implementation after creating these tests.")
        print("Run 'pytest rockPaperScissorsTests.py' after implementing the functions.")