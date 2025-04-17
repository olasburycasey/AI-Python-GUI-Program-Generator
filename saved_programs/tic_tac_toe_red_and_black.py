import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Tic Tac Toe")

        self.current_player = "X"  # Start with player X
        self.board = [""] * 9  # Represents the 3x3 board as a list
        self.buttons = [] # Keep track of buttons

        # Create buttons for the Tic Tac Toe grid
        for i in range(9):
            button = tk.Button(
                master,
                text="",
                width=10,
                height=3,
                command=lambda i=i: self.button_click(i), # Lambda captures the current 'i'
                font=("Arial", 24),
            )
            button.grid(row=i // 3, column=i % 3) # arrange the button in 3x3 grid
            self.buttons.append(button)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=3, column=1, columnspan=1)
        
        self.player_label = tk.Label(master, text=f"Player {self.current_player}'s Turn", font=("Arial", 16))
        self.player_label.grid(row=3, column=0, columnspan=1)


    def button_click(self, index):
        """Handles the event when a button is clicked."""
        if self.board[index] == "":
            self.board[index] = self.current_player
            if self.current_player == "X":
                color = "red"
            else:
                color = "black"
            self.buttons[index].config(text=self.current_player, fg=color)  # Update button text with color

            if self.check_winner():
                messagebox.showinfo("Tic Tac Toe", f"Player {self.current_player} wins!")
                self.reset_game()
                return

            if self.is_board_full():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.reset_game()
                return

            self.switch_player()
            self.player_label.config(text=f"Player {self.current_player}'s Turn")


    def switch_player(self):
        """Switches the current player from X to O or O to X."""
        self.current_player = "O" if self.current_player == "X" else "X"


    def check_winner(self):
        """Checks if there is a winner."""
        # Check rows
        for i in range(0, 9, 3):
            if self.board[i] == self.board[i + 1] == self.board[i + 2] != "":
                return True

        # Check columns
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return True

        # Check diagonals
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True

        return False


    def is_board_full(self):
        """Checks if the board is full (draw)."""
        return all(cell != "" for cell in self.board)


    def reset_game(self):
        """Resets the game board."""
        self.board = [""] * 9
        self.current_player = "X"
        self.player_label.config(text=f"Player {self.current_player}'s Turn")
        for button in self.buttons:
            button.config(text="", fg="black")  # Clear button text and reset color


if __name__ == "__main__":
    root = tk.Tk()
    tic_tac_toe = TicTacToe(root)
    root.mainloop()
