# wap to play tic tac toe
import random

def print_board(board):
    # Print the Tic-Tac-Toe board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check if the specified player has won by completing a row, column, or diagonal
    for i in range(3):
        # Check rows and columns
        if all(board[i][j] == player for j in range(3)) or all(board[j][i] == player for j in range(3)):
            return True
    # Check diagonals
    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_board_full(board):
    # Check if the board is full (no empty spaces left)
    return all(cell != ' ' for row in board for cell in row)

def user_move(board):
    while True:
        try:
            # Get the user's move input
            position = int(input("Your move (1-9): "))
            # Convert the move input to row and column indices
            if 1 <= position <= 9:
                row, col = divmod(position - 1, 3)
            else:
                # Handle invalid input (not between 1 and 9)
                print("Invalid input. Enter a number between 1 and 9.")
                continue
        except ValueError:
            # Handle invalid input (not an integer)
            print("Invalid input. Enter a number between 1 and 9.")
            continue

        # Check if the chosen cell is empty
        if board[row][col] == ' ':
            # Place the user's symbol in the chosen cell
            board[row][col] = 'X'
            break
        else:
            # Handle invalid move (cell already occupied)
            print("Invalid move. Please try again.")

def computer_move(board):
    while True:
        # Generate a random move for the computer
        row, col = random.randint(0, 2), random.randint(0, 2)

        # Check if the chosen cell is empty
        if board[row][col] == ' ':
            # Place the computer's symbol in the chosen cell
            board[row][col] = 'O'
            break

def play_tic_tac_toe():
    # Initialize an empty Tic-Tac-Toe board
    board = [[' ' for _ in range(3)] for _ in range(3)]

    while True:
        # Display the current state of the board
        print_board(board)

        # User's move
        user_move(board)

        # Check if the user has won
        if check_winner(board, 'X'):
            print_board(board)
            print("You win!")
            break
        # Check if the board is full (tie)
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

        # Computer's move
        computer_move(board)

        # Check if the computer has won
        if check_winner(board, 'O'):
            print_board(board)
            print("Computer wins!")
            break
        # Check if the board is full (tie)
        elif is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break

if __name__ == "__main__":
    # Start the Tic-Tac-Toe game
    play_tic_tac_toe()
