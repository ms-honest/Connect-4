import numpy as np


def create_board():
    return np.zeros((5, 5))


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, row, col):
    return board[row][col] == 0


def print_board(board):
    print(board)


def check_winner(board, piece):
    # Check rows
    for r in range(5):
        for c in range(2):
            if all(board[r][c + i] == piece for i in range(4)):
                return True

    # Check columns
    for c in range(5):
        for r in range(2):
            if all(board[r + i][c] == piece for i in range(4)):
                return True

    # Check diagonals
    for r in range(2):
        for c in range(2):
            if all(board[r + i][c + i] == piece for i in range(4)):
                return True
            if all(board[r + 3 - i][c + i] == piece for i in range(4)):
                return True

    return False


board = create_board()
turn = 0
game_over = False
while not game_over:
    print_board(board)
    player = turn % 2 + 1
    print(f"Player {player}'s turn")

    row = int(input("Enter row (0-4): "))
    col = int(input("Enter column (0-4): "))

    if is_valid_location(board, row, col):
        drop_piece(board, row, col, player)

        if check_winner(board, player):
            print_board(board)
            print(f"Player {player} wins!")
            game_over = True

        turn += 1
    else:
        print("Invalid move. Try again.")