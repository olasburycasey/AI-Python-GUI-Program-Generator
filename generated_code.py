import tkinter as tk
import random
import time

class SimonSaysGame:
    def __init__(self, master):
        self.master = master
        master.title("Simon Says")

        self.colors = ["red", "green", "blue", "yellow", "orange", "purple", "pink", "cyan",
                       "brown", "gray", "lime", "magenta", "teal", "olive", "maroon", "navy"]
        self.sequence = []
        self.user_sequence = []
        self.level = 0 #start at 0 and increment at start_game so level will be 1 at the first round
        self.game_over = False
        self.delay = 0.7  # Initial delay in seconds
        self.buttons = {}
        button_width = 8  # Adjust button width for more buttons
        button_height = 2  # Adjust button height if needed
        num_cols = 4  # Number of columns for buttons
        for i, color in enumerate(self.colors):
            self.buttons[color] = tk.Button(master, bg=color, width=button_width, height=button_height,
                                             command=lambda c=color: self.button_press(c))
            self.buttons[color].grid(row=i // num_cols, column=i % num_cols, padx=5, pady=5)

        self.start_button = tk.Button(master, text="Start", command=self.start_game)
        self.start_button.grid(row=4, column=2, columnspan=2, pady=10)

        self.level_label = tk.Label(master, text="Level: 0")
        self.level_label.grid(row=4, column=0, columnspan=2, pady=10)

        self.message_label = tk.Label(master, text="")
        self.message_label.grid(row=5, column=0, columnspan=4, pady=10)


    def start_game(self):
        self.sequence = []
        self.user_sequence = []
        self.level = 1
        self.game_over = False
        self.delay = 0.7 #reset delay
        self.level_label.config(text="Level: 1")
        self.message_label.config(text="")
        self.add_to_sequence()


    def add_to_sequence(self):
        try:
            self.sequence.append(random.choice(self.colors))
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
                self.master.after(int(self.delay * 1000), self.play_next_color, index + 1)  # Use updated delay

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
            self.master.update()
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
                self.message_label.config(text="Game Over!  Level reached: " + str(self.level))
                self.disable_buttons()
                return

            if len(self.user_sequence) == len(self.sequence):
                self.level += 1
                self.level_label.config(text="Level: " + str(self.level))
                self.user_sequence = []
                if self.delay > 0.2:  # Decrease delay but don't go below 0.2 seconds
                    self.delay *= 0.9  # Reduce delay by 10%
                self.master.after(500, self.add_to_sequence)
        except IndexError:
            self.game_over = True
            self.message_label.config(text="Game Over!  Level reached: " + str(self.level))
            self.disable_buttons()
            return #ensure game terminates after index error

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