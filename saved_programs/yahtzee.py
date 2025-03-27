import tkinter as tk
import tkinter.messagebox as messagebox
import random

class YahtzeeGUI:
    def __init__(self, master):
        self.master = master
        master.title("Yahtzee")

        # Game state variables
        self.dice = [0] * 5
        self.held = [False] * 5
        self.rolls_remaining = 3
        self.scorecard = {}
        self.game_over = False

        # GUI elements
        self.label_dice = [tk.Label(master, text="0", relief="solid", borderwidth=1, width=3) for _ in range(5)]
        self.button_roll = tk.Button(master, text="Roll Dice", command=self.roll_dice)
        self.button_hold = [tk.Button(master, text="Hold", command=lambda i=i: self.toggle_hold(i)) for i in range(5)]
        self.label_rolls_remaining = tk.Label(master, text="Rolls Remaining: 3")
        self.label_scorecard = tk.Label(master, text="Scorecard:")
        self.text_scorecard = tk.Text(master, height=15, width=30, state="disabled") # make read-only

        # Layout
        for i in range(5):
            self.label_dice[i].grid(row=0, column=i)
            self.button_hold[i].grid(row=1, column=i)

        self.button_roll.grid(row=2, column=0, columnspan=5)
        self.label_rolls_remaining.grid(row=3, column=0, columnspan=5)
        self.label_scorecard.grid(row=4, column=0, columnspan=5)
        self.text_scorecard.grid(row=5, column=0, columnspan=5)


        # Category buttons and score calculation
        self.category_buttons = {}
        self.categories = ["Aces", "Twos", "Threes", "Fours", "Fives", "Sixes",
                           "Three of a Kind", "Four of a Kind", "Full House",
                           "Small Straight", "Large Straight", "Yahtzee", "Chance"]

        for i, cat in enumerate(self.categories):
           self.category_buttons[cat] = tk.Button(master, text=cat, command=lambda c=cat: self.score_category(c), state="disabled")
           self.category_buttons[cat].grid(row=6 + i, column=0, columnspan=5)  # Place buttons below scorecard


        self.label_total_score = tk.Label(master, text="Total Score: 0")
        self.label_total_score.grid(row=6 + len(self.categories), column=0, columnspan=5)  # Place total score label

        self.total_score = 0 # Track total score


    def roll_dice(self):
        if self.rolls_remaining > 0:
            for i in range(5):
                if not self.held[i]:
                    self.dice[i] = random.randint(1, 6)
            self.update_dice_labels()
            self.rolls_remaining -= 1
            self.label_rolls_remaining.config(text=f"Rolls Remaining: {self.rolls_remaining}")
            self.update_hold_button_states()  # Reset hold button states
            self.update_category_button_states() # Enable the category buttons

            if self.rolls_remaining == 0:
                self.button_roll.config(state="disabled")  # Disable roll button after last roll
        else:
             messagebox.showinfo("Yahtzee", "No rolls remaining!")


    def toggle_hold(self, index):
        self.held[index] = not self.held[index]
        if self.held[index]:
            self.button_hold[index].config(text="Release")
        else:
            self.button_hold[index].config(text="Hold")

    def update_dice_labels(self):
        for i in range(5):
            self.label_dice[i].config(text=str(self.dice[i]))

    def update_hold_button_states(self):
      for i in range(5):
          self.held[i] = False  # Reset held state
          self.button_hold[i].config(text="Hold") #Reset button label


    def update_category_button_states(self):
        """Enables category buttons if the category hasn't been scored yet."""
        for cat in self.categories:
            if cat not in self.scorecard:
                self.category_buttons[cat].config(state="normal")

    def score_category(self, category):
        """Calculates and applies the score for a selected category."""

        score = self.calculate_score(category)
        self.scorecard[category] = score

        # Disable the button for the selected category
        self.category_buttons[category].config(state="disabled")

        # Update the scorecard text
        self.update_scorecard_text()

        # Reset for the next turn
        self.rolls_remaining = 3
        self.label_rolls_remaining.config(text=f"Rolls Remaining: {self.rolls_remaining}")
        self.button_roll.config(state="normal") # Enable roll button
        self.update_dice_labels() # Resets the dice to 0.
        self.dice = [0] * 5  # Resets the dice values

        self.update_hold_button_states()  # Reset hold buttons

        self.total_score += score
        self.label_total_score.config(text=f"Total Score: {self.total_score}")

        # Check for game over
        if len(self.scorecard) == len(self.categories):
            self.game_over = True
            messagebox.showinfo("Yahtzee", f"Game Over!  Your final score is: {self.total_score}")
            self.button_roll.config(state="disabled")
            for cat in self.categories:
              self.category_buttons[cat].config(state="disabled")



    def calculate_score(self, category):
        """Calculates the score based on the category and dice values."""
        counts = [self.dice.count(i) for i in range(1, 7)]
        self.dice.sort()

        if category == "Aces":
            return self.dice.count(1) * 1
        elif category == "Twos":
            return self.dice.count(2) * 2
        elif category == "Threes":
            return self.dice.count(3) * 3
        elif category == "Fours":
            return self.dice.count(4) * 4
        elif category == "Fives":
            return self.dice.count(5) * 5
        elif category == "Sixes":
            return self.dice.count(6) * 6
        elif category == "Three of a Kind":
            if max(counts) >= 3:
                return sum(self.dice)
            else:
                return 0
        elif category == "Four of a Kind":
            if max(counts) >= 4:
                return sum(self.dice)
            else:
                return 0
        elif category == "Full House":
            if 3 in counts and 2 in counts:
                return 25
            else:
                return 0
        elif category == "Small Straight":
            if self.is_straight(4):
                return 30
            else:
                return 0
        elif category == "Large Straight":
            if self.is_straight(5):
                return 40
            else:
                return 0
        elif category == "Yahtzee":
            if max(counts) == 5:
                return 50
            else:
                return 0
        elif category == "Chance":
            return sum(self.dice)
        else:
            return 0


    def is_straight(self, length):
      """Helper function to check for straights."""
      unique_dice = sorted(list(set(self.dice)))
      if len(unique_dice) < length:
          return False

      for i in range(len(unique_dice) - length + 1):
          if unique_dice[i + length - 1] - unique_dice[i] == length - 1:
              return True
      return False


    def update_scorecard_text(self):
        """Updates the scorecard display in the text box."""
        self.text_scorecard.config(state="normal")  # Enable editing temporarily
        self.text_scorecard.delete("1.0", tk.END)  # Clear the text box
        for category, score in self.scorecard.items():
            self.text_scorecard.insert(tk.END, f"{category}: {score}\n")
        self.text_scorecard.config(state="disabled")  # Disable editing


root = tk.Tk()
gui = YahtzeeGUI(root)
root.mainloop()
