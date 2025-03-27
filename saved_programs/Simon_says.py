import tkinter as tk
import random
import time

class SimonSays:
    def __init__(self, master):
        self.master = master
        master.title("Simon Says")

        self.sequence = []
        self.user_sequence = []
        self.level = 1
        self.game_over = False
        self.score = 0
        self.high_score = 0

        self.button_colors = {
            "red": "red",
            "blue": "blue",
            "green": "green",
            "yellow": "yellow"
        }

        self.buttons = {}

        self.setup_ui()


    def setup_ui(self):
        """Sets up the graphical user interface."""

        # Score label
        self.score_label = tk.Label(self.master, text=f"Score: {self.score}", font=("Arial", 16))
        self.score_label.grid(row=0, column=0, columnspan=2, pady=10)

        # High score label
        self.high_score_label = tk.Label(self.master, text=f"High Score: {self.high_score}", font=("Arial", 12))
        self.high_score_label.grid(row=0, column=2, columnspan=2, pady=10)

        # Buttons
        button_names = ["red", "blue", "green", "yellow"]
        row = 1
        col = 0
        for name in button_names:
            button = tk.Button(self.master, text=name.capitalize(), bg=self.button_colors[name], width=10, height=5,
                               command=lambda color=name: self.user_input(color))  # use lambda to pass the color
            button.grid(row=row, column=col, padx=5, pady=5)
            self.buttons[name] = button
            col += 1
            if col > 1:
                col = 0
                row += 1

        # Start Button
        self.start_button = tk.Button(self.master, text="Start Game", command=self.start_game, font=("Arial", 14))
        self.start_button.grid(row=3, column=0, columnspan=4, pady=20)  # Adjusted row


        # Message Label
        self.message_label = tk.Label(self.master, text="Press Start to begin!", font=("Arial", 14))
        self.message_label.grid(row=4, column=0, columnspan=4, pady=10)  # Adjusted row


    def start_game(self):
        """Starts a new game."""
        self.sequence = []
        self.user_sequence = []
        self.level = 1
        self.game_over = False
        self.score = 0
        self.score_label.config(text=f"Score: {self.score}")
        self.message_label.config(text="Get ready!")
        self.master.after(1000, self.next_sequence)

    def next_sequence(self):
        """Adds a random color to the sequence and shows it to the player."""
        if self.game_over:
            return

        colors = list(self.button_colors.keys())
        random_color = random.choice(colors)
        self.sequence.append(random_color)

        self.message_label.config(text=f"Level: {self.level} - Watch closely!")
        self.master.after(500, self.play_sequence)  # Delay before showing sequence


    def play_sequence(self):
        """Highlights the sequence to the user."""
        for i, color in enumerate(self.sequence):
            self.master.after(i * 750, self.highlight_button, color)  # Show each button for 500ms, with 250ms delay
            self.master.after(i * 750 + 500, self.unhighlight_button, color)
        self.master.after(len(self.sequence) * 750, self.enable_buttons)  # Enable buttons after showing sequence
        self.user_sequence = []  # Reset user sequence


    def highlight_button(self, color):
        """Highlights a button."""
        self.buttons[color].config(relief=tk.SUNKEN)
        self.master.update()  # Force GUI update


    def unhighlight_button(self, color):
        """Unhighlights a button."""
        self.buttons[color].config(relief=tk.RAISED)
        self.master.update()  # Force GUI update

    def enable_buttons(self):
        """Enables the color buttons for user input."""
        for button in self.buttons.values():
            button['state'] = tk.NORMAL  # Set state to NORMAL to enable the button
        self.message_label.config(text="Your turn!")


    def disable_buttons(self):
        """Disables the color buttons to prevent user input."""
        for button in self.buttons.values():
            button['state'] = tk.DISABLED  # Set state to DISABLED to disable the button


    def user_input(self, color):
        """Handles user input when a color button is pressed."""

        if self.game_over:
            return

        self.user_sequence.append(color)
        self.check_sequence()



    def check_sequence(self):
        """Checks if the user's sequence matches the correct sequence."""
        index = len(self.user_sequence) - 1
        if self.user_sequence[index] != self.sequence[index]:
            self.game_over_func()
            return

        if len(self.user_sequence) == len(self.sequence):
            # Sequence completed successfully
            self.score += 1
            self.score_label.config(text=f"Score: {self.score}")
            self.level += 1
            self.message_label.config(text="Correct!")
            self.disable_buttons()  # Disable buttons while next sequence is prepared
            self.master.after(1000, self.next_sequence)


    def game_over_func(self):
        """Handles the game over state."""
        self.game_over = True
        self.message_label.config(text=f"Game Over! You reached level {self.level}. Score: {self.score}")

        # Update high score
        if self.score > self.high_score:
            self.high_score = self.score
            self.high_score_label.config(text=f"High Score: {self.high_score}")

        self.disable_buttons()
        self.start_button['state'] = tk.NORMAL # re-enable the start button.


root = tk.Tk()
game = SimonSays(root)
root.mainloop()
