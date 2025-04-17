import tkinter as tk
from tkinter import messagebox
import random

class TicTacToe:
    def __init__(self, master):
        self.master = master
        master.title("Impossible Tic Tac Toe")

        self.player_symbol = "X"  # Player is X
        self.computer_symbol = "O"  # Computer is O
        self.current_player = self.player_symbol
        self.board = [""] * 9  # Represent the 3x3 board
        self.buttons = []
        self.game_over = False

        # Score tracking
        self.player_score = 0
        self.computer_score = 0

        # Difficulty level (1: Easy, 2: Medium, 3: Hard)
        self.difficulty = 2  # Default to Medium

        # UI elements for difficulty selection
        self.difficulty_label = tk.Label(master, text="Difficulty:", font=("Arial", 12))
        self.difficulty_label.grid(row=5, column=0, columnspan=1)

        self.difficulty_var = tk.IntVar()
        self.difficulty_var.set(self.difficulty)  # Initialize with the default difficulty

        self.easy_radio = tk.Radiobutton(master, text="Easy", variable=self.difficulty_var, value=1, command=self.set_difficulty, font=("Arial", 12))
        self.medium_radio = tk.Radiobutton(master, text="Medium", variable=self.difficulty_var, value=2, command=self.set_difficulty, font=("Arial", 12))
        self.hard_radio = tk.Radiobutton(master, text="Hard", variable=self.difficulty_var, value=3, command=self.set_difficulty, font=("Arial", 12))

        self.easy_radio.grid(row=5, column=1)
        self.medium_radio.grid(row=5, column=2)
        self.hard_radio.grid(row=5, column=3)


        # UI elements for score
        self.player_score_label = tk.Label(master, text="Player (X): 0", font=("Arial", 16))
        self.player_score_label.grid(row=4, column=0, columnspan=1)

        self.computer_score_label = tk.Label(master, text="Computer (O): 0", font=("Arial", 16))
        self.computer_score_label.grid(row=4, column=2, columnspan=1)

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

    def set_difficulty(self):
        self.difficulty = self.difficulty_var.get()
        self.reset_game() # Reset the game after changing difficulty.

    def button_click(self, index):
        if self.game_over:
            return  # Prevent moves after game is over

        if self.board[index] == "":  # Check if the cell is empty
            self.board[index] = self.player_symbol
            self.buttons[index].config(text=self.player_symbol)

            if self.check_winner():
                self.update_score(self.player_symbol)
                messagebox.showinfo("Tic Tac Toe", f"Player {self.player_symbol} wins!")
                self.game_over = True
                return
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.game_over = True
                return

            self.current_player = self.computer_symbol
            self.master.after(500, self.computer_move)  # Computer's turn after a delay

    def computer_move(self):
        if self.game_over:
            return

        if self.difficulty == 1: #Easy
            move = self.find_random_move()
        elif self.difficulty == 2: #Medium
            if random.random() < 0.7: # 70% chance of playing optimally
                move = self.find_best_move()
            else:
                move = self.find_random_move()
        else: #Hard
             move = self.find_best_move()


        if move is not None:  # Ensure a valid move was found
            self.board[move] = self.computer_symbol
            self.buttons[move].config(text=self.computer_symbol)

            if self.check_winner():
                self.update_score(self.computer_symbol)
                messagebox.showinfo("Tic Tac Toe", f"Computer wins!")
                self.game_over = True
                return
            elif self.check_draw():
                messagebox.showinfo("Tic Tac Toe", "It's a draw!")
                self.game_over = True
                return

            self.current_player = self.player_symbol

    def find_random_move(self):
        available_moves = [i for i, cell in enumerate(self.board) if cell == ""]
        if available_moves:
            return random.choice(available_moves)
        return None

    def find_best_move(self):  #Implements the minimax algorithm to find the best move for the computer.
        best_score = -float('inf')
        best_move = None

        for i in range(9):
            if self.board[i] == "":
                self.board[i] = self.computer_symbol
                score = self.minimax(self.board, 0, False)
                self.board[i] = ""  # Undo the move
                if score > best_score:
                    best_score = score
                    best_move = i

        return best_move

    def minimax(self, board, depth, is_maximizing): #Minimax with alpha-beta pruning to find optimal moves.
        scores = {
            self.computer_symbol: 1,
            self.player_symbol: -1,
            "draw": 0
        }

        winner = self.check_winner_minimax(board) #Pass the board to check winner
        if winner:
            return scores[winner]
        if self.check_draw_minimax(board):
            return 0

        if is_maximizing:
            best_score = -float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = self.computer_symbol
                    score = self.minimax(board, depth + 1, False)
                    board[i] = ""
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = float('inf')
            for i in range(9):
                if board[i] == "":
                    board[i] = self.player_symbol
                    score = self.minimax(board, depth + 1, True)
                    board[i] = ""
                    best_score = min(score, best_score)
            return best_score


    def check_winner(self):
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
        return all(cell != "" for cell in self.board)

    def check_winner_minimax(self, board): #Check winner using the board passed from minimax algorithm
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],
            [0, 3, 6], [1, 4, 7], [2, 5, 8],
            [0, 4, 8], [2, 4, 6],
        ]

        for combo in winning_combinations:
            if (
                board[combo[0]] == board[combo[1]] == board[combo[2]]
                and board[combo[0]] != ""
            ):
                return board[combo[0]]
        return None

    def check_draw_minimax(self, board): #Check draw using the board passed from minimax algorithm
        return all(cell != "" for cell in board)


    def reset_game(self):
        self.board = [""] * 9
        self.current_player = self.player_symbol
        self.game_over = False
        for button in self.buttons:
            button.config(text="")

    def update_score(self, winner):
        if winner == self.player_symbol:
            self.player_score += 1
            self.player_score_label.config(text=f"Player (X): {self.player_score}")
        elif winner == self.computer_symbol:
            self.computer_score += 1
            self.computer_score_label.config(text=f"Computer (O): {self.computer_score}")


root = tk.Tk()
tictactoe = TicTacToe(root)
root.mainloop()
