import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.current_player = "X"
        self.board = [""] * 9  # Represent the 3x3 board
        self.buttons = []

        for i in range(9):
            button = tk.Button(
                master,
                text="",
                width=10,
                height=3,
                font=("Arial", 24),
                command=lambda i=i: self.button_click(i),
            )
            self.buttons.append(button)
            button.grid(row=i // 3, column=i % 3)  # Arrange buttons in a grid

        self.reset_button = tk.Button(
            master, text="Reset", command=self.reset_game, font=("Arial", 16)
        )
        self.reset_button.grid(row=3, column=1, columnspan=1)

    def button_click(self, index):
        if self.board[index] == "":  # Check if the cell is empty
            self.board[index] = self.current_player
            self.buttons[index].config(text=self.current_player)
            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()  # Automatically reset after a win
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()  # Automatically reset after a draw
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

    def check_winner(self):
        # Define winning combinations
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6],             # Diagonals
        ]

        for combo in winning_combinations:
            if (
                self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]
                and self.board[combo[0]] != ""
            ):
                return True
        return False

    def check_draw(self):
        return all(cell != "" for cell in self.board)  # Check if all cells are filled

    def reset_game(self):
        self.board = [""] * 9
        self.current_player = "X"
        for button in self.buttons:
            button.config(text="") #Clear buttons texts



root = tk.Tk()
tictactoe = TicTacToe(root)
root.mainloop()
