import random

print("Welcome to Tic Tac Toe Game!")

def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end="")
        for j in range(3):
            print(" " + board[i][j] + " |", end="")
        print()
        print("-------------")

def check_win(board, player):
    for i in range(3):
        if (board[i][0] == player and board[i][1] == player and board[i][2] == player):
            return True
        if (board[0][i] == player and board[1][i] == player and board[2][i] == player):
            return True
    if (board[0][0] == player and board[1][1] == player and board[2][2] == player):
        return True
    if (board[0][2] == player and board[1][1] == player and board[2][0] == player):
        return True
    return False


def tic_tac_toe():
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    players = ["X", "O"]
    current_player = players[0]
    print_board(board)
    while True:
        if current_player == "X":
            row = int(input("Enter row number (1-3) for " + current_player + ": "))
            col = int(input("Enter column number (1-3) for " + current_player + ": "))
            if (board[row-1][col-1] == " "):
                board[row-1][col-1] = current_player
                print_board(board)
            else:
                print("The cell is not empty. Try again!")
        else:
            row = random.randint(1, 3)
            col = random.randint(1, 3)
            if (board[row-1][col-1] == " "):
                board[row-1][col-1] = current_player
                print_board(board)
            else:
                continue
        if (check_win(board, current_player)):
            print("Congratulations! " + current_player + " wins!")
            break
        elif all(" " not in row for row in board):
            print("The game ended in a tie!")
            break
        if (current_player == players[0]):
            current_player = players[1]
        else:
            current_player = players[0]

tic_tac_toe()