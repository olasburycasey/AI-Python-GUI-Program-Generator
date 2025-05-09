import tkinter as tk
import random

class Breakout:
    def __init__(self, master):
        self.master = master
        master.title("Breakout (1976)")

        self.width = 400
        self.height = 500
        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.paddle_width = 60
        self.paddle_height = 10
        self.paddle_x = self.width // 2 - self.paddle_width // 2
        self.paddle_y = self.height - 30
        try:
            self.paddle = self.canvas.create_rectangle(self.paddle_x, self.paddle_y,
                                                       self.paddle_x + self.paddle_width,
                                                       self.paddle_y + self.paddle_height,
                                                       fill="white")
        except Exception as e:
            print(f"Error creating paddle: {e}")
            self.paddle = None  # Handle the error, e.g., set to None

        self.ball_size = 10
        self.ball_x = self.width // 2
        self.ball_y = self.height // 2
        try:
            self.ball = self.canvas.create_oval(self.ball_x - self.ball_size, self.ball_y - self.ball_size,
                                                self.ball_x + self.ball_size, self.ball_y + self.ball_size,
                                                fill="red")
        except Exception as e:
            print(f"Error creating ball: {e}")
            self.ball = None  # Handle error

        self.ball_x_speed = 3
        self.ball_y_speed = -3

        self.bricks = []
        self.brick_width = 40
        self.brick_height = 15
        self.brick_rows = 5
        self.brick_cols = 10
        self.brick_colors = ["red", "orange", "yellow", "green", "blue"]
        self.create_bricks()

        self.score = 0
        self.lives = 3
        self.score_label = tk.Label(master, text="Score: 0", fg="white", bg="black")
        self.score_label.pack()
        self.lives_label = tk.Label(master, text="Lives: 3", fg="white", bg="black")
        self.lives_label.pack()


        self.game_over = False
        self.paused = False
        self.message_label = None  # Initialize message label.


        master.bind("<Left>", self.move_paddle_left)
        master.bind("<Right>", self.move_paddle_right)
        master.bind("p", self.toggle_pause)  # Pause/Unpause the game


        self.update()

    def create_bricks(self):
        for row in range(self.brick_rows):
            for col in range(self.brick_cols):
                x = col * (self.brick_width + 5) + 25
                y = row * (self.brick_height + 5) + 50
                color = self.brick_colors[row % len(self.brick_colors)]
                try:
                    brick = self.canvas.create_rectangle(x, y, x + self.brick_width, y + self.brick_height,
                                                        fill=color, tags="brick")
                    self.bricks.append(brick)
                except Exception as e:
                    print(f"Error creating brick: {e}")
                    # Optionally, you could stop creating bricks if an error occurs.
                    return

    def move_paddle_left(self, event):
        if not self.game_over and not self.paused and self.paddle is not None: # Check if paddle exists
            self.paddle_x -= 20
            if self.paddle_x < 0:
                self.paddle_x = 0
            try:
                self.canvas.move(self.paddle, -20, 0)
            except Exception as e:
                print(f"Error moving paddle: {e}")


    def move_paddle_right(self, event):
        if not self.game_over and not self.paused and self.paddle is not None: #Check if paddle exists
            self.paddle_x += 20
            if self.paddle_x + self.paddle_width > self.width:
                self.paddle_x = self.width - self.paddle_width
            try:
                self.canvas.move(self.paddle, 20, 0)
            except Exception as e:
                print(f"Error moving paddle: {e}")

    def toggle_pause(self, event):
        self.paused = not self.paused

    def update(self):
        if not self.game_over and not self.paused and self.ball is not None and self.paddle is not None: #Check if ball and paddle exists
            self.move_ball()
            self.check_collision()
            if not self.bricks:
                self.game_over = True
                self.display_message("You Win!")
            else:
                try:
                    self.master.after(20, self.update) # Adjust delay for speed
                except Exception as e:
                    print(f"Error in update loop: {e}")

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
                self.ball_x_speed = random.choice([-3, 3])
                self.ball_y_speed = -3
                try:
                    self.canvas.move(self.ball, self.ball_x - self.canvas.coords(self.ball)[0] - self.ball_size , self.ball_y - self.canvas.coords(self.ball)[1]- self.ball_size) # Reset ball position.
                except Exception as e:
                    print(f"Error resetting ball position: {e}")


        try:
            self.canvas.move(self.ball, self.ball_x_speed, self.ball_y_speed)
        except Exception as e:
            print(f"Error moving ball: {e}")

    def check_collision(self):
        try:
            ball_coords = self.canvas.coords(self.ball)
            paddle_coords = self.canvas.coords(self.paddle)
        except Exception as e:
            print(f"Error getting coordinates: {e}")
            return  # Exit if we can't get coordinates.

        # Collision with paddle
        if ball_coords and paddle_coords:
            if ball_coords[3] >= paddle_coords[1] and ball_coords[0] < paddle_coords[2] and ball_coords[2] > paddle_coords[0] and ball_coords[1] < paddle_coords[3]:
                self.ball_y_speed = -abs(self.ball_y_speed)  # Ensure it goes up
                # Adjust horizontal speed based on where it hits the paddle
                paddle_center = (paddle_coords[0] + paddle_coords[2]) / 2
                ball_center = (ball_coords[0] + ball_coords[2]) / 2
                difference = ball_center - paddle_center
                self.ball_x_speed += difference / 10  # Add a small horizontal speed

        # Collision with bricks
        bricks_to_remove = []
        for brick in self.bricks:
            try:
                brick_coords = self.canvas.coords(brick)
                if (ball_coords[0] < brick_coords[2] and ball_coords[2] > brick_coords[0] and
                    ball_coords[1] < brick_coords[3] and ball_coords[3] > brick_coords[1]):
                    bricks_to_remove.append(brick)

                    self.score += 10
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

            except Exception as e:
                print(f"Error during brick collision check: {e}")

        # Remove bricks after the loop to avoid modifying the list while iterating
        for brick in bricks_to_remove:
            try:
                self.bricks.remove(brick)
                self.canvas.delete(brick)
            except Exception as e:
                print(f"Error deleting brick: {e}")

    def display_message(self, message):
        # Destroy the old message label if it exists
        if self.message_label:
            self.message_label.destroy()

        try:
            self.message_label = tk.Label(self.master, text=message, fg="white", bg="black", font=("Arial", 24))
            self.message_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the label
        except Exception as e:
            print(f"Error displaying message: {e}")


root = tk.Tk()
breakout = Breakout(root)
root.mainloop()