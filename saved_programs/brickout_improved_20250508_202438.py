import tkinter as tk
import random

class Breakout:
    def __init__(self, master):
        self.master = master
        master.title("Breakout (1976) - Enhanced")

        self.width = 600  # Increased width for better play
        self.height = 700  # Increased height
        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="black", highlightthickness=0)  # Added highlightthickness=0
        self.canvas.pack()

        # Paddle properties
        self.paddle_width = 80  # Increased paddle width
        self.paddle_height = 12
        self.paddle_x = self.width // 2 - self.paddle_width // 2
        self.paddle_y = self.height - 50  # Moved paddle lower
        self.paddle_speed = 10  # Increased paddle speed
        self.paddle = self.canvas.create_rectangle(self.paddle_x, self.paddle_y,
                                                    self.paddle_x + self.paddle_width,
                                                    self.paddle_y + self.paddle_height,
                                                    fill="white", tags="paddle")

        # Ball properties
        self.ball_size = 8  # Reduced ball size slightly
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.ball_x_speed = 4 # Increased ball speed
        self.ball_y_speed = -4 # Increased ball speed
        self.ball = self.canvas.create_oval(self.ball_x - self.ball_size, self.ball_y - self.ball_size,
                                             self.ball_x + self.ball_size, self.ball_y + self.ball_size,
                                             fill="red", tags="ball")

        # Brick properties
        self.bricks = []
        self.brick_width = 50  # Increased brick width
        self.brick_height = 20  # Increased brick height
        self.brick_rows = 6  # Increased rows
        self.brick_cols = 12  # Increased columns
        self.brick_colors = ["red", "orange", "yellow", "green", "blue", "purple"] # Added purple
        self.brick_spacing = 3 # Added spacing between bricks
        self.create_bricks()

        # Game state variables
        self.score = 0
        self.lives = 3
        self.level = 1  # Added level
        self.game_over = False
        self.paused = False
        self.message_label = None
        self.score_label = tk.Label(master, text="Score: 0", fg="white", bg="black")
        self.score_label.pack()
        self.lives_label = tk.Label(master, text="Lives: 3", fg="white", bg="black")
        self.lives_label.pack()
        self.level_label = tk.Label(master, text="Level: 1", fg="white", bg="black") # added level
        self.level_label.pack()


        # Input bindings
        master.bind("<Left>", self.move_paddle_left)
        master.bind("<Right>", self.move_paddle_right)
        master.bind("<space>", self.toggle_pause) # Changed pause key to space
        master.bind("<r>", self.restart_game) # Added restart key

        self.update()

    def create_bricks(self):
        for row in range(self.brick_rows):
            for col in range(self.brick_cols):
                x = col * (self.brick_width + self.brick_spacing) + 30 # added margin
                y = row * (self.brick_height + self.brick_spacing) + 80 # added margin
                color = self.brick_colors[row % len(self.brick_colors)]
                brick = self.canvas.create_rectangle(x, y, x + self.brick_width, y + self.brick_height,
                                                    fill=color, tags="brick")
                self.bricks.append(brick)

    def move_paddle_left(self, event):
        if not self.game_over and not self.paused:
            self.paddle_x -= self.paddle_speed
            if self.paddle_x < 0:
                self.paddle_x = 0
            self.canvas.coords(self.paddle, self.paddle_x, self.paddle_y,
                               self.paddle_x + self.paddle_width, self.paddle_y + self.paddle_height)

    def move_paddle_right(self, event):
        if not self.game_over and not self.paused:
            self.paddle_x += self.paddle_speed
            if self.paddle_x + self.paddle_width > self.width:
                self.paddle_x = self.width - self.paddle_width
            self.canvas.coords(self.paddle, self.paddle_x, self.paddle_y,
                               self.paddle_x + self.paddle_width, self.paddle_y + self.paddle_height)

    def toggle_pause(self, event):
        self.paused = not self.paused
        if self.paused:
            self.display_message("Paused")
        else:
            self.display_message("") # Clear pause message

    def update(self):
        if not self.game_over and not self.paused:
            self.move_ball()
            self.check_collision()
            if not self.bricks:
                self.level += 1 # Go to next level
                self.level_label.config(text = f"Level: {self.level}")
                self.display_message(f"Level {self.level} Complete! Starting Next Level")
                self.ball_x = self.width // 2 # Reset ball position
                self.ball_y = self.height // 2
                self.ball_x_speed *= 1.1  # Increase speed
                self.ball_y_speed *= 1.1
                self.canvas.coords(self.ball, self.ball_x - self.ball_size, self.ball_y - self.ball_size,
                                    self.ball_x + self.ball_size, self.ball_y + self.ball_size)
                self.create_bricks() # Create new bricks

            self.master.after(20, self.update)

    def move_ball(self):
        self.ball_x += self.ball_x_speed
        self.ball_y += self.ball_y_speed

        # Bounce off walls
        if self.ball_x - self.ball_size < 0 or self.ball_x + self.ball_size > self.width:
            self.ball_x_speed = -self.ball_x_speed
        if self.ball_y - self.ball_size < 0:
            self.ball_y_speed = -self.ball_y_speed

        # Ball hits bottom
        if self.ball_y + self.ball_size > self.height:
            self.lives -= 1
            self.lives_label.config(text=f"Lives: {self.lives}")
            if self.lives == 0:
                self.game_over = True
                self.display_message("Game Over!")
            else:
                # Reset ball position and direction
                self.ball_x = self.width // 2
                self.ball_y = self.height // 2
                self.ball_x_speed = random.choice([-4, 4]) # Increased speed
                self.ball_y_speed = -4 # Increased speed
                self.canvas.coords(self.ball, self.ball_x - self.ball_size, self.ball_y - self.ball_size,
                                    self.ball_x + self.ball_size, self.ball_y + self.ball_size)


        self.canvas.coords(self.ball, self.ball_x - self.ball_size, self.ball_y - self.ball_size,
                            self.ball_x + self.ball_size, self.ball_y + self.ball_size)

    def check_collision(self):
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle)

        # Collision with paddle
        if ball_coords[3] >= paddle_coords[1] and ball_coords[0] < paddle_coords[2] and ball_coords[2] > paddle_coords[0] and ball_coords[1] < paddle_coords[3]:
            self.ball_y_speed = -abs(self.ball_y_speed)  # Ensure it goes up
            # Adjust horizontal speed based on where it hits the paddle
            paddle_center = (paddle_coords[0] + paddle_coords[2]) / 2
            ball_center = (ball_coords[0] + ball_coords[2]) / 2
            difference = ball_center - paddle_center
            self.ball_x_speed += difference / 8  # Add a small horizontal speed


        # Collision with bricks
        bricks_to_remove = []
        for brick in self.bricks:
            brick_coords = self.canvas.coords(brick)
            if (ball_coords[0] < brick_coords[2] and ball_coords[2] > brick_coords[0] and
                ball_coords[1] < brick_coords[3] and ball_coords[3] > brick_coords[1]):
                bricks_to_remove.append(brick)

                self.score += 10 * self.level # Increased score
                self.score_label.config(text=f"Score: {self.score}")

                # Determine collision side (more accurate)
                overlap_left = brick_coords[2] - ball_coords[0]
                overlap_right = ball_coords[2] - brick_coords[0]
                overlap_top = brick_coords[3] - ball_coords[1]
                overlap_bottom = ball_coords[3] - brick_coords[1]

                if min(overlap_left, overlap_right, overlap_top, overlap_bottom) == overlap_left:
                    self.ball_x_speed = abs(self.ball_x_speed)  # Hit left side
                elif min(overlap_left, overlap_right, overlap_top, overlap_bottom) == overlap_right:
                    self.ball_x_speed = -abs(self.ball_x_speed) # Hit right side
                elif min(overlap_left, overlap_right, overlap_top, overlap_bottom) == overlap_top:
                    self.ball_y_speed = abs(self.ball_y_speed)  # Hit top side
                else:
                    self.ball_y_speed = -abs(self.ball_y_speed) # Hit bottom side

                break  # Only hit one brick per frame


        # Remove bricks after the loop to avoid modifying the list while iterating
        for brick in bricks_to_remove:
            self.bricks.remove(brick)
            self.canvas.delete(brick)

    def display_message(self, message):
        if self.message_label:
            self.message_label.destroy()

        self.message_label = tk.Label(self.master, text=message, fg="white", bg="black", font=("Arial", 24))
        self.message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the label

    def restart_game(self, event):
        # Reset game state
        self.game_over = False
        self.paused = False
        self.score = 0
        self.lives = 3
        self.level = 1
        self.ball_x_speed = 4
        self.ball_y_speed = -4

        # Update labels
        self.score_label.config(text="Score: 0")
        self.lives_label.config(text="Lives: 3")
        self.level_label.config(text="Level: 1")

        # Reset ball and paddle positions
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        self.paddle_x = self.width // 2 - self.paddle_width // 2

        self.canvas.coords(self.ball, self.ball_x - self.ball_size, self.ball_y - self.ball_size,
                            self.ball_x + self.ball_size, self.ball_y + self.ball_size)
        self.canvas.coords(self.paddle, self.paddle_x, self.paddle_y,
                            self.paddle_x + self.paddle_width, self.paddle_y + self.paddle_height)


        # Clear existing bricks and create new ones
        for brick in self.bricks:
            self.canvas.delete(brick)
        self.bricks = []
        self.create_bricks()

        # Remove game over message if it exists
        self.display_message("") # Clear message

        # Start the game loop
        self.update()

root = tk.Tk()
breakout = Breakout(root)
root.mainloop()