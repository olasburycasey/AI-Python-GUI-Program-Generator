import tkinter as tk
import random
from tkinter import messagebox

class MinesweeperBattleRoyale:
    def __init__(self, master, rows=10, cols=10, mines=10):
        self.master = master
        master.title("Minesweeper Battle Royale")

        if not (isinstance(rows, int) and rows > 0 and isinstance(cols, int) and cols > 0 and isinstance(mines, int) and mines >= 0):
            raise ValueError("Rows, cols, and mines must be positive integers.")

        if mines >= rows * cols:
            raise ValueError("Too many mines for the grid size.")

        self.rows = rows
        self.cols = cols
        self.mines = mines
        self.grid = []
        self.buttons = []
        self.flags_placed = 0
        self.game_over = False

        self.remaining_cells = rows * cols - mines  # Track revealed non-mine cells

        self.flag_count_label = tk.Label(master, text=f"Flags: {self.mines - self.flags_placed}")
        self.flag_count_label.grid(row=0, column=0, columnspan=cols)

        self.initialize_grid()
        self.create_widgets()


    def initialize_grid(self):
        # Create empty grid
        self.grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        # Place mines
        mine_positions = random.sample(range(self.rows * self.cols), self.mines)
        for pos in mine_positions:
            row = pos // self.cols
            col = pos % self.cols
            self.grid[row][col] = -1  # -1 represents a mine


        # Calculate adjacent mine counts
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] != -1:
                    count = 0
                    for i in range(max(0, row - 1), min(self.rows, row + 2)):
                        for j in range(max(0, col - 1), min(self.cols, col + 2)):
                            if self.grid[i][j] == -1:
                                count += 1
                    self.grid[row][col] = count


    def create_widgets(self):
        self.buttons = []
        for row in range(self.rows):
            button_row = []
            for col in range(self.cols):
                try:
                    button = tk.Button(
                        self.master,
                        width=2,
                        height=1,
                        command=lambda r=row, c=col: self.on_click(r, c),
                        relief=tk.RAISED,
                        font=("Arial", 12)
                    )
                    button.bind("<Button-3>", lambda event, r=row, c=col: self.on_right_click(event, r, c))
                    button.grid(row=row + 1, column=col) # Add 1 to row due to flag count label
                    button_row.append(button)
                except Exception as e:
                    print(f"Error creating button at row={row}, col={col}: {e}")

            self.buttons.append(button_row)


    def on_click(self, row, col):
        if self.game_over:
            return

        try:
            if self.buttons[row][col]["relief"] == tk.SUNKEN: #If already revealed
                return

            if self.buttons[row][col]["text"] == "🚩":
                return #prevent clicking on a flagged cell

            if self.grid[row][col] == -1:
                self.reveal_mines()
                self.buttons[row][col].config(bg="red")  # Highlight clicked mine
                messagebox.showinfo("Game Over", "You hit a mine!")
                self.game_over = True
            else:
                self.reveal_cell(row, col)
                if self.remaining_cells == 0:
                    messagebox.showinfo("Congratulations!", "You won!")
                    self.game_over = True
        except IndexError:
            print(f"IndexError: row={row}, col={col} is out of bounds.")
        except Exception as e:
            print(f"An error occurred during on_click: {e}")



    def on_right_click(self, event, row, col):
        if self.game_over:
            return
        try:
            if self.buttons[row][col]["relief"] == tk.SUNKEN:
                return

            if self.buttons[row][col]["text"] == "":
                if self.flags_placed < self.mines:
                    self.buttons[row][col].config(text="🚩", fg="red")
                    self.flags_placed += 1
                else:
                    messagebox.showinfo("No more flags!", "You have used all your flags.")

            elif self.buttons[row][col]["text"] == "🚩":
                self.buttons[row][col].config(text="")
                self.flags_placed -= 1

            self.update_flag_count()
        except IndexError:
            print(f"IndexError: row={row}, col={col} is out of bounds.")
        except Exception as e:
            print(f"An error occurred during on_right_click: {e}")



    def reveal_cell(self, row, col):
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return

        try:
            if self.buttons[row][col]["relief"] == tk.SUNKEN:
                return

            if self.buttons[row][col]["text"] == "🚩":
                return

            self.buttons[row][col].config(relief=tk.SUNKEN)
            self.remaining_cells -=1


            value = self.grid[row][col]

            if value > 0:
                self.buttons[row][col].config(text=str(value))
            elif value == 0:
                self.buttons[row][col].config(text="")
                # Recursively reveal adjacent cells
                for i in range(max(0, row - 1), min(self.rows, row + 2)):
                    for j in range(max(0, col - 1), min(self.cols, col + 2)):
                        self.reveal_cell(i, j)
        except IndexError:
            print(f"IndexError: row={row}, col={col} during reveal_cell.")
        except Exception as e:
             print(f"An error occurred during reveal_cell: {e}")


    def reveal_mines(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col] == -1:
                    try:
                        self.buttons[row][col].config(text="💣", relief=tk.SUNKEN)
                    except IndexError:
                        print(f"IndexError in reveal_mines: row={row}, col={col}")
                    except Exception as e:
                        print(f"Error in reveal_mines: {e}")


    def update_flag_count(self):
       self.flag_count_label.config(text=f"Flags: {self.mines - self.flags_placed}")



root = tk.Tk()
try:
    minesweeper = MinesweeperBattleRoyale(root)
    root.mainloop()
except ValueError as e:
    messagebox.showerror("Initialization Error", str(e))
except Exception as e:
    messagebox.showerror("Unexpected Error", f"An unexpected error occurred: {e}")