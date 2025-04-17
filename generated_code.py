import tkinter as tk
from tkinter import messagebox
import random

class ConnectFour:
    def __init__(self, master):
        self.master = master
        master.title("Connect Four")

        self.rows = 6
        self.cols = 7
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.player = 'X'  # Human player
        self.computer = 'O'
        self.game_over = False

        self.buttons = []
        for col in range(self.cols):
            button = tk.Button(master, text=f"Drop in Column {col+1}", command=lambda c=col: self.drop_piece(c), width=15)
            button.grid(row=0, column=col, padx=5, pady=5)
            self.buttons.append(button)

        self.canvas = tk.Canvas(master, width=self.cols * 100, height=self.rows * 100, bg="blue")
        self.canvas.grid(row=1, columnspan=self.cols, padx=10, pady=10)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game, width=15)
        self.reset_button.grid(row=2, columnspan=self.cols, pady=10)

        self.draw_board()

    def draw_board(self):
        """Draws the Connect Four board on the canvas."""
        for row in range(self.rows):
            for col in range(self.cols):
                x1 = col * 100 + 10
                y1 = row * 100 + 10
                x2 = x1 + 80
                y2 = y1 + 80
                self.canvas.create_oval(x1, y1, x2, y2, fill="white", outline="black")
                piece = self.board[self.rows - 1 - row][col]  # Invert row for display
                if piece == 'X':
                    self.canvas.create_oval(x1, y1, x2, y2, fill="red", outline="black")
                elif piece == 'O':
                    self.canvas.create_oval(x1, y1, x2, y2, fill="yellow", outline="black")

    def drop_piece(self, col):
        """Drops a piece into the specified column."""
        if self.game_over:
            return

        for row in range(self.rows):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.player
                self.draw_board()
                if self.check_win(self.player):
                    messagebox.showinfo("Game Over", "You Win!")
                    self.game_over = True
                    return
                if self.check_draw():
                    messagebox.showinfo("Game Over", "It's a Draw!")
                    self.game_over = True
                    return

                self.player = self.computer
                self.master.after(500, self.computer_move) # Add a small delay for visual effect
                return  #  Make sure to return here to not execute the computer move directly after the player move

        messagebox.showinfo("Invalid Move", "Column is full!")

    def computer_move(self):
        """Makes a move for the computer."""
        if self.game_over:
            return

        # Enhanced Computer AI:
        best_move = self.get_best_move()

        if best_move is None: # No valid moves, should not happen with check_draw in place, but safeguard
            messagebox.showinfo("Game Over", "It's a Draw! (Computer couldn't find a move)")
            self.game_over = True
            return

        col = best_move
        for row in range(self.rows):
            if self.board[row][col] == ' ':
                self.board[row][col] = self.computer
                self.draw_board()
                if self.check_win(self.computer):
                    messagebox.showinfo("Game Over", "Computer Wins!")
                    self.game_over = True
                    return

                if self.check_draw():
                    messagebox.showinfo("Game Over", "It's a Draw!")
                    self.game_over = True
                    return


                self.player = 'X' # Switch back to player
                return

    def get_best_move(self):
        """Determines the best move for the computer using a simple heuristic."""

        # 1. Check for winning move
        for col in range(self.cols):
            if self.is_valid_move(col):
                temp_board = [row[:] for row in self.board] # Create a copy
                row = self.get_next_open_row(temp_board, col)
                temp_board[row][col] = self.computer
                if self.check_win(self.computer, temp_board): #check if the move wins
                    return col

        # 2. Block opponent's winning move
        for col in range(self.cols):
            if self.is_valid_move(col):
                temp_board = [row[:] for row in self.board]
                row = self.get_next_open_row(temp_board, col)
                temp_board[row][col] = self.player #simulate the player's move
                if self.check_win(self.player, temp_board): #check if the move wins for the player
                    return col

        # 3.  Center preference (Slightly improves gameplay)
        center_col = self.cols // 2
        if self.is_valid_move(center_col):
            return center_col

        # 4. Random valid move
        possible_moves = [col for col in range(self.cols) if self.is_valid_move(col)]
        if possible_moves:
            return random.choice(possible_moves)

        return None # No valid move found

    def is_valid_move(self, col):
        """Checks if a move is valid."""
        return self.board[self.rows - 1][col] == ' '

    def get_next_open_row(self, board, col):
        """Gets the next open row in a column."""
        for row in range(self.rows):
            if board[row][col] == ' ':
                return row
        return None #Should never happen if is_valid_move is used

    def check_win(self, player, board=None):
        """Checks if the given player has won on the given board (or self.board if None)."""
        if board is None:
            board = self.board  # Use the current board if none is provided

        # Check horizontal
        for row in range(self.rows):
            for col in range(self.cols - 3):
                if board[row][col] == player and \
                   board[row][col+1] == player and \
                   board[row][col+2] == player and \
                   board[row][col+3] == player:
                    return True

        # Check vertical
        for row in range(self.rows - 3):
            for col in range(self.cols):
                if board[row][col] == player and \
                   board[row+1][col] == player and \
                   board[row+2][col] == player and \
                   board[row+3][col] == player:
                    return True

        # Check positive diagonal
        for row in range(self.rows - 3):
            for col in range(self.cols - 3):
                if board[row][col] == player and \
                   board[row+1][col+1] == player and \
                   board[row+2][col+2] == player and \
                   board[row+3][col+3] == player:
                    return True

        # Check negative diagonal
        for row in range(3, self.rows):
            for col in range(self.cols - 3):
                if board[row][col] == player and \
                   board[row-1][col+1] == player and \
                   board[row-2][col+2] == player and \
                   board[row-3][col+3] == player:
                    return True

        return False

    def check_draw(self):
        """Checks if the game is a draw."""
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == ' ':
                    return False
        return True

    def reset_game(self):
        """Resets the game to its initial state."""
        self.board = [[' ' for _ in range(self.cols)] for _ in range(self.rows)]
        self.player = 'X'
        self.game_over = False
        self.draw_board()


root = tk.Tk()
game = ConnectFour(root)
root.mainloop()
