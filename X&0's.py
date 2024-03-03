import tkinter as tk
from tkinter import messagebox
import random

def check_win(board, player):

    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True

    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

def check_draw(board):
    for row in board:
        for cell in row:
            if cell == "":
                return False
    return True

def evaluate_move(board, row, col, player):

    temp_board = [row[:] for row in board]

    temp_board[row][col] = player

    if check_win(temp_board, player):
        return 1

    if check_draw(temp_board):
        return 0

    return -1

def find_best_move(board, player):
    best_score = -float('inf')
    best_move = None
    opponent = "O" if player == "X" else "X"
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                score = evaluate_move(board, i, j, player)
                if score > best_score:
                    best_score = score
                    best_move = (i, j)
                elif score == -1:
                    # Check if blocking is needed
                    board[i][j] = opponent
                    if check_win(board, opponent):
                        best_move = (i, j)
                    board[i][j] = ""
    return best_move

def button_click(row, col):
    global current_player

    if buttons[row][col]["text"] == "":
        buttons[row][col]["text"] = current_player
        board[row][col] = current_player

        if check_win(board, current_player):
            messagebox.showinfo("Tic-Tac-Toe", f"Player {current_player} wins!")
            reset_board()
        elif check_draw(board):
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
            reset_board()
        else:
            current_player = "X" if current_player == "O" else "O"
            if current_player == "O":
                row, col = find_best_move(board, "O")
                buttons[row][col].invoke()

def reset_board():
    global current_player, board
    current_player = "X"
    board = [["" for _ in range(3)] for _ in range(3)]
    for row in buttons:
        for button in row:
            button["text"] = ""


root = tk.Tk()
root.title("Tic-Tac-Toe")


buttons = [[None, None, None] for _ in range(3)]
for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text="", font=("Arial", 20), width=5, height=2,
                                   command=lambda row=i, col=j: button_click(row, col))
        buttons[i][j].grid(row=i, column=j, padx=5, pady=5)


current_player = "X"
board = [["" for _ in range(3)] for _ in range(3)]

root.mainloop()
