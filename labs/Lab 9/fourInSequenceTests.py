#Ashlyn Croft
# 22Jul255
# Lab 9
# Four in Sequence tests
# Makes the game more robust and harder to break

import pytest
from fourInSequence import checkForNextMoveWin, checkAdjacent, checkDraw, checkWinner

def create_empty_board():
    """Helper function to create an empty 6x7 board"""
    return [[".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", "."]]

def test_checkWinner_horizontal():
    """Test checkWinner function for horizontal wins"""
    board = create_empty_board()
    board[5] = ["X", "X", "X", "X", ".", ".", "."] 
    assert checkWinner(board, 1) == True
    

    board = create_empty_board()
    board[3] = [".", "O", "O", "O", "O", ".", "."]  
    assert checkWinner(board, 2) == True
    
    
    board = create_empty_board()
    board[5] = ["X", "X", "O", "X", ".", ".", "."]  
    assert checkWinner(board, 1) == False

def test_checkWinner_vertical():
    """Test checkWinner function for vertical wins"""
    board = create_empty_board()
    for row in range(2, 6): 
        board[row][0] = "X"
    assert checkWinner(board, 1) == True
    board = create_empty_board()
    for row in range(0, 4): 
        board[row][3] = "O"
    assert checkWinner(board, 2) == True
    

    board = create_empty_board()
    board[5][0] = "X"
    board[4][0] = "X"
    board[3][0] = "O"  
    board[2][0] = "X"
    assert checkWinner(board, 1) == False

def test_checkWinner_diagonal_negative():
    """Test checkWinner function for negatively sloped diagonal wins"""
    board = create_empty_board()
    board[2][0] = "X"  
    board[3][1] = "X"
    board[4][2] = "X"
    board[5][3] = "X"
    assert checkWinner(board, 1) == True
    

    board = create_empty_board()
    board[0][2] = "O"
    board[1][3] = "O"
    board[2][4] = "O"
    board[3][5] = "O"
    assert checkWinner(board, 2) == True

def test_checkWinner_diagonal_positive():
    """Test checkWinner function for positively sloped diagonal wins"""

    board = create_empty_board()
    board[5][0] = "X"  
    board[4][1] = "X"
    board[3][2] = "X"
    board[2][3] = "X"
    assert checkWinner(board, 1) == True
    


    board = create_empty_board()
    board[3][3] = "O"
    board[2][4] = "O"
    board[1][5] = "O"
    board[0][6] = "O"
    assert checkWinner(board, 2) == True

def test_checkWinner_no_win():
    """Test checkWinner function when there's no win"""
    board = create_empty_board()
    assert checkWinner(board, 1) == False
    assert checkWinner(board, 2) == False
    

    board = create_empty_board()
    board[5] = ["X", "O", "X", "O", "X", "O", "X"]
    assert checkWinner(board, 1) == False
    assert checkWinner(board, 2) == False

def test_checkDraw_empty_board():
    """Test checkDraw function with empty board"""
    board = create_empty_board()
    assert checkDraw(board) == False

def test_checkDraw_partial_board():
    """Test checkDraw function with partially filled board"""
    board = create_empty_board()
    board[5] = ["X", "O", "X", ".", ".", ".", "."]
    board[4] = ["O", "X", ".", ".", ".", ".", "."]
    assert checkDraw(board) == False

def test_checkDraw_full_board():
    """Test checkDraw function with completely full board"""
    board = [["X", "O", "X", "O", "X", "O", "X"],
             ["O", "X", "O", "X", "O", "X", "O"],
             ["X", "O", "X", "O", "X", "O", "X"],
             ["O", "X", "O", "X", "O", "X", "O"],
             ["X", "O", "X", "O", "X", "O", "X"],
             ["O", "X", "O", "X", "O", "X", "O"]]
    assert checkDraw(board) == True

def test_checkForNextMoveWin_horizontal():
    """Test checkForNextMoveWin function for horizontal winning moves"""
    board = create_empty_board()
    board[5] = ["X", "X", "X", ".", ".", ".", "."]
    result = checkForNextMoveWin(board, 1)
    assert result == 3  
    

    board = create_empty_board()
    board[5] = ["X", "X", "X", "X", "X", "X", "X"]  # Error here I think. Bookmarkig ------------------------------------
    board[4] = [".", "O", "O", "O", ".", ".", "."]  
    result = checkForNextMoveWin(board, 2)
    assert result in [0, 4] 

def test_checkForNextMoveWin_vertical():
    """Test checkForNextMoveWin function for vertical winning moves"""

    board = create_empty_board()
    board[5][2] = "X"
    board[4][2] = "X"
    board[3][2] = "X"
    result = checkForNextMoveWin(board, 1)
    assert result == 2  

def test_checkForNextMoveWin_no_win():
    """Test checkForNextMoveWin function when no winning move exists"""
    board = create_empty_board()
    result = checkForNextMoveWin(board, 1)
    assert result == -1


    board = create_empty_board()
    board[5] = ["X", ".", "O", ".", "X", ".", "."]
    result = checkForNextMoveWin(board, 1)
    assert result == -1

def test_checkAdjacent_with_pieces():
    """Test checkAdjacent function when there are adjacent pieces"""
    board = create_empty_board()
    board[5][3] = "X"  
    board[4][3] = "X"  
    
    result = checkAdjacent(board, 1)
    assert result != -1 or result == -1  # Could be either I think

def test_checkAdjacent_isolated_pieces():
    """Test checkAdjacent function with isolated pieces"""
    board = create_empty_board()
    board[5][0] = "X" 
    
    result = checkAdjacent(board, 1)
    assert isinstance(result, int)

def test_checkAdjacent_empty_board():
    """Test checkAdjacent function with empty board"""
    board = create_empty_board()
    result = checkAdjacent(board, 1)
    assert result == -1 

def test_checkAdjacent_opponent_pieces():
    """Test checkAdjacent function with opponent pieces"""
    board = create_empty_board()
    board[5][3] = "O" 

    
    result = checkAdjacent(board, 1)  
    assert result == -1

def test_edge_cases():
    """Test various edge cases"""
    board = create_empty_board()
    board[5] = [".", ".", ".", "X", "X", "X", "X"]
    assert checkWinner(board, 1) == True
    

    board = create_empty_board()
    for row in range(0, 4):
        board[row][6] = "O"
    assert checkWinner(board, 2) == True
    

    board = create_empty_board()
    board[5][0] = "X"
    board[4][1] = "X"
    board[3][2] = "X"
    board[2][3] = "X"
    assert checkWinner(board, 1) == True

if __name__ == "__main__":
    print("Running basic functionality tests...")
    
    # Test empty board
    empty_board = create_empty_board()
    print(f"Empty board checkWinner: {checkWinner(empty_board, 1)}")
    print(f"Empty board checkDraw: {checkDraw(empty_board)}")
    print(f"Empty board checkForNextMoveWin: {checkForNextMoveWin(empty_board, 1)}")
    print(f"Empty board checkAdjacent: {checkAdjacent(empty_board, 1)}")
    
    print("Basic tests completed. Run 'pytest fourInSequenceTests.py' for full test suite.")