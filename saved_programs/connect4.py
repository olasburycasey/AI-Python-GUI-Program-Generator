import tkinter as tk
from tkinter import messagebox

class ConnectFour:
    def __init__(self, master):
        self.master = master
        master.title("Connect Four")

        self.rows = 6
        self.cols = 7
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        self.player = "X"  # 'X' for Player 1, 'O' for Player 2
        self.game_over = False

        self.buttons = []
        for col in range(self.cols):
            button = tk.Button(
                master,
                text=f"Column {col + 1}",
                command=lambda col=col: self.drop_piece(col),
                width=10,
                height=2,
            )
            button.grid(row=self.rows, column=col, padx=5, pady=5)
            self.buttons.append(button)

        self.canvas_width = 500
        self.canvas_height = 400  # Reduced height for visual balance
        self.canvas = tk.Canvas(
            master, width=self.canvas_width, height=self.canvas_height, bg="blue"
        )
        self.canvas.grid(row=0, column=0, columnspan=self.cols)
        self.draw_board()

        self.status_label = tk.Label(master, text=f"Player {1 if self.player == 'X' else 2}'s Turn", font=("Arial", 12))
        self.status_label.grid(row=self.rows + 1, column=0, columnspan=self.cols)

        self.reset_button = tk.Button(master, text="Reset Game", command=self.reset_game)
        self.reset_button.grid(row=self.rows + 2, column=0, columnspan=self.cols, pady=5)


    def draw_board(self):
        """Draws the Connect Four board on the canvas."""
        circle_radius = min(
            self.canvas_width // (self.cols * 2 + 1),
            self.canvas_height // (self.rows * 2 + 1),
        )  # Adjust radius for spacing
        padding_x = (self.canvas_width - (self.cols * 2 * circle_radius)) // (self.cols + 1)
        padding_y = (self.canvas_height - (self.rows * 2 * circle_radius)) // (self.rows + 1)


        for row in range(self.rows):
            for col in range(self.cols):
                x = padding_x + col * (2 * circle_radius + padding_x) + circle_radius
                y = padding_y + row * (2 * circle_radius + padding_y) + circle_radius

                if self.board[row][col] == "X":
                    color = "red"
                elif self.board[row][col] == "O":
                    color = "yellow"
                else:
                    color = "white"
                self.canvas.create_oval(
                    x - circle_radius,
                    y - circle_radius,
                    x + circle_radius,
                    y + circle_radius,
                    fill=color,
                    outline="black",
                )



    def drop_piece(self, col):
        """Drops a piece into the specified column."""
        if self.game_over:
            return

        for row in range(self.rows - 1, -1, -1):
            if self.board[row][col] == " ":
                self.board[row][col] = self.player
                self.draw_board()
                if self.check_win(row, col):
                    self.game_over = True
                    winner = 1 if self.player == "X" else 2
                    messagebox.showinfo("Game Over", f"Player {winner} wins!")
                    self.status_label.config(text=f"Player {winner} wins!")
                    return  # Early return to prevent further turns

                if self.check_draw():
                    self.game_over = True
                    messagebox.showinfo("Game Over", "It's a draw!")
                    self.status_label.config(text="It's a draw!")
                    return

                self.player = "O" if self.player == "X" else "X"
                self.status_label.config(text=f"Player {1 if self.player == 'X' else 2}'s Turn")
                return

        messagebox.showinfo("Invalid Move", "Column is full.  Choose another column.")


    def check_win(self, row, col):
        """Checks for a win starting from the given row and column."""
        # Check horizontal
        count = 0
        for c in range(self.cols):
            if self.board[row][c] == self.player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check vertical
        count = 0
        for r in range(self.rows):
            if self.board[r][col] == self.player:
                count += 1
                if count == 4:
                    return True
            else:
                count = 0

        # Check positive diagonal (top-left to bottom-right)
        count = 0
        for i in range(-3, 4):
            r, c = row + i, col + i
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.board[r][c] == self.player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        # Check negative diagonal (top-right to bottom-left)
        count = 0
        for i in range(-3, 4):
            r, c = row + i, col - i
            if 0 <= r < self.rows and 0 <= c < self.cols:
                if self.board[r][c] == self.player:
                    count += 1
                    if count == 4:
                        return True
                else:
                    count = 0

        return False


    def check_draw(self):
        """Checks if the board is full (a draw)."""
        for row in self.board:
            if " " in row:
                return False
        return True


    def reset_game(self):
        """Resets the game to the initial state."""
        self.board = [[" " for _ in range(self.cols)] for _ in range(self.rows)]
        self.player = "X"
        self.game_over = False
        self.draw_board()
        self.status_label.config(text=f"Player {1 if self.player == 'X' else 2}'s Turn")


root = tk.Tk()
game = ConnectFour(root)
root.mainloop()
