```python
import tkinter as tk
import random
from tkinter import messagebox

class RockPaperScissorsGUI:
    def __init__(self, master):
        self.master = master
        master.title("Rock Paper Scissors")

        # Keep the window the same size
        master.resizable(False, False)

        self.user_score = 0
        self.computer_score = 0

        self.label = tk.Label(master, text="Choose your move:", font=("Arial", 16))
        self.label.pack(pady=10)

        self.rock_button = tk.Button(master, text="Rock", command=lambda: self.play_round("Rock"), width=10, height=2, font=("Arial", 12))
        self.rock_button.pack(pady=5)

        self.paper_button = tk.Button(master, text="Paper", command=lambda: self.play_round("Paper"), width=10, height=2, font=("Arial", 12))
        self.paper_button.pack(pady=5)

        self.scissors_button = tk.Button(master, text="Scissors", command=lambda: self.play_round("Scissors"), width=10, height=2, font=("Arial", 12))
        self.scissors_button.pack(pady=5)

        self.result_label = tk.Label(master, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

        self.score_label = tk.Label(master, text="User: 0  Computer: 0", font=("Arial", 12))
        self.score_label.pack(pady=5)

    def play_round(self, user_choice):
        choices = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(choices)

        winner = self.determine_winner(user_choice, computer_choice)

        if winner == "user":
            self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}.\nYou win!")
            self.user_score += 1
        elif winner == "computer":
            self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}.\nYou lose!")
            self.computer_score += 1
        else:
            self.result_label.config(text=f"You chose {user_choice}. Computer chose {computer_choice}.\nIt's a tie!")

        self.score_label.config(text=f"User: {self.user_score}  Computer: {self.computer_score}")


    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "tie"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "user"
        else:
            return "computer"


root = tk.Tk()
gui = RockPaperScissorsGUI(root)
root.mainloop()
```

Key change:

* `master.resizable(False, False)`:  This line is added in the `__init__` method. It disables the window's ability to be resized horizontally and vertically, effectively locking the window size.  The first `False` argument controls horizontal resizing, and the second `False` argument controls vertical resizing.
