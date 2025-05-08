import tkinter as tk
import random
import time
import tkinter.font as tkFont  # For font styling
import pickle #to save and load high score

class SimonSaysGame:
    def __init__(self, master):
        self.master = master
        master.title("Simon Says")

        # Constants for better readability and maintainability
        self.COLORS = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan",
                       "brown", "gray", "lime", "magenta", "teal", "olive", "maroon", "navy"]
        self.INITIAL_DELAY = 0.7  # Initial delay in seconds
        self.MIN_DELAY = 0.2  # Minimum delay allowed
        self.DELAY_DECREASE_FACTOR = 0.9  # Reduction factor for delay
        self.BUTTON_WIDTH = 8
        self.BUTTON_HEIGHT = 2
        self.NUM_COLS = 4

        self.sequence = []
        self.user_sequence = []
        self.level = 0
        self.game_over = False
        self.delay = self.INITIAL_DELAY
        self.buttons = {}
        self.score = 0 # Initialize score

        # Load High Score
        self.high_score = self.load_high_score()

        # Font Styling
        font_style = tkFont.Font(family="Helvetica", size=12)

        # Create Buttons
        for i, color in enumerate(self.COLORS):
            self.buttons[color] = tk.Button(
                master,
                bg=color,
                width=self.BUTTON_WIDTH,
                height=self.BUTTON_HEIGHT,
                command=lambda c=color: self.button_press(c),
                state=tk.DISABLED,  # Disable buttons initially
                font=font_style
            )
            self.buttons[color].grid(row=i // self.NUM_COLS, column=i % self.NUM_COLS, padx=5, pady=5)

        # Start Button
        self.start_button = tk.Button(master, text="Start", command=self.start_game, font=font_style)
        self.start_button.grid(row=len(self.COLORS) // self.NUM_COLS, column=self.NUM_COLS // 2 - 1, columnspan=2, pady=10)

        # Level Label
        self.level_label = tk.Label(master, text="Level: 0", font=font_style)
        self.level_label.grid(row=len(self.COLORS) // self.NUM_COLS, column=0, columnspan=self.NUM_COLS // 2, pady=10)

        # Score Label
        self.score_label = tk.Label(master, text=f"Score: {self.score}", font=font_style)
        self.score_label.grid(row=len(self.COLORS) // self.NUM_COLS + 1, column=0, columnspan=self.NUM_COLS // 2, pady=10)

        # High Score Label
        self.high_score_label = tk.Label(master, text=f"High Score: {self.high_score}", font=font_style)
        self.high_score_label.grid(row=len(self.COLORS) // self.NUM_COLS + 1, column=self.NUM_COLS // 2, columnspan=self.NUM_COLS // 2, pady=10)


        # Message Label
        self.message_label = tk.Label(master, text="", font=font_style)
        self.message_label.grid(row=len(self.COLORS) // self.NUM_COLS + 2, column=0, columnspan=self.NUM_COLS, pady=10)

    def load_high_score(self):
        try:
            with open("high_score.pkl", "rb") as f:
                return pickle.load(f)
        except FileNotFoundError:
            return 0
        except Exception as e:
            print(f"Error loading high score: {e}") #print error to console
            return 0



    def save_high_score(self):
        try:
            with open("high_score.pkl", "wb") as f:
                pickle.dump(self.high_score, f)
        except Exception as e:
            print(f"Error saving high score: {e}") #print error to console


    def start_game(self):
        self.sequence = []
        self.user_sequence = []
        self.level = 1
        self.score = 0 # Reset score on new game
        self.game_over = False
        self.delay = self.INITIAL_DELAY
        self.level_label.config(text="Level: 1")
        self.score_label.config(text=f"Score: {self.score}")
        self.message_label.config(text="")
        self.enable_buttons()  # Enable buttons at start
        self.add_to_sequence()


    def add_to_sequence(self):
        try:
            self.sequence.append(random.choice(self.COLORS))
            self.play_sequence()
        except Exception as e:
            self.message_label.config(text=f"Error adding to sequence: {e}")
            self.disable_buttons()
            self.game_over = True

    def play_sequence(self):
        self.disable_buttons()
        self.master.after(500, self.play_next_color, 0)

    def play_next_color(self, index):
        try:
            if index < len(self.sequence):
                color = self.sequence[index]
                self.flash_button(color)
                self.master.after(int(self.delay * 1000), self.play_next_color, index + 1)

            else:
                self.enable_buttons()

        except Exception as e:
            self.message_label.config(text=f"Error playing sequence: {e}")
            self.disable_buttons()
            self.game_over = True


    def flash_button(self, color):
        try:
            original_color = self.buttons[color].cget("bg")
            self.buttons[color].config(bg="white")
            self.master.after(int(self.delay * 1000 / 2), lambda c=color, oc=original_color: self.buttons[c].config(bg=oc))
        except KeyError:
            self.message_label.config(text=f"Color {color} not found in buttons.")
            self.disable_buttons()
            self.game_over = True
        except Exception as e:
            self.message_label.config(text=f"Error flashing button: {e}")
            self.disable_buttons()
            self.game_over = True


    def button_press(self, color):
        if self.game_over:
            return

        self.user_sequence.append(color)
        self.check_sequence()


    def check_sequence(self):
        try:
            index = len(self.user_sequence) - 1
            if self.user_sequence[index] != self.sequence[index]:
                self.game_over = True
                self.message_label.config(text=f"Game Over! Level reached: {self.level}, Score: {self.score}")
                self.disable_buttons()
                if self.score > self.high_score:
                    self.high_score = self.score
                    self.high_score_label.config(text=f"High Score: {self.high_score}")
                    self.save_high_score()  # Save the new high score

                return

            if len(self.user_sequence) == len(self.sequence):
                self.score += self.level * 10  # Award points based on level
                self.score_label.config(text=f"Score: {self.score}")
                self.level += 1
                self.level_label.config(text="Level: " + str(self.level))
                self.user_sequence = []
                if self.delay > self.MIN_DELAY:
                    self.delay *= self.DELAY_DECREASE_FACTOR
                self.master.after(500, self.add_to_sequence)

        except IndexError:
            self.game_over = True
            self.message_label.config(text=f"Game Over! Level reached: {self.level}, Score: {self.score}")
            self.disable_buttons()
            if self.score > self.high_score:
                self.high_score = self.score
                self.high_score_label.config(text=f"High Score: {self.high_score}")
                self.save_high_score()
            return  # ensure game terminates after index error

        except Exception as e:
            self.message_label.config(text=f"Error checking sequence: {e}")
            self.disable_buttons()
            self.game_over = True


    def disable_buttons(self):
        for button in self.buttons.values():
            button.config(state=tk.DISABLED)


    def enable_buttons(self):
        for button in self.buttons.values():
            button.config(state=tk.NORMAL)


root = tk.Tk()
game = SimonSaysGame(root)
root.mainloop()