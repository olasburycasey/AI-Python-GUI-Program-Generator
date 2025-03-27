import tkinter as tk
import random

# Constants
WIDTH = 600
HEIGHT = 400
SNAKE_SIZE = 20
SNAKE_COLOR = "green"
HEAD_COLOR = "lightblue"  # Added head color
FOOD_COLOR = "red"
BACKGROUND_COLOR = "black"
DEFAULT_SPEED = 100  # milliseconds (lower = faster)


class SnakeGame:
    def __init__(self, master):
        self.master = master
        master.title("Snake Game")

        self.canvas = tk.Canvas(master, width=WIDTH, height=HEIGHT, bg=BACKGROUND_COLOR, highlightthickness=0)
        self.canvas.pack()

        self.score_label = tk.Label(master, text="Score: 0", font=("Arial", 16), bg=BACKGROUND_COLOR, fg="white")
        self.score_label.pack()

        self.restart_button = None  # Initialize restart button

        # Speed Selection Buttons
        self.speed_frame = tk.Frame(master, bg=BACKGROUND_COLOR)
        self.speed_frame.pack()

        tk.Button(self.speed_frame, text="Slow", command=lambda: self.set_speed(150)).pack(side=tk.LEFT, padx=5)
        tk.Button(self.speed_frame, text="Medium", command=lambda: self.set_speed(100)).pack(side=tk.LEFT, padx=5)
        tk.Button(self.speed_frame, text="Fast", command=lambda: self.set_speed(50)).pack(side=tk.LEFT, padx=5)

        self.speed = DEFAULT_SPEED  # Initialize with a default speed
        self.start_new_game()  # Start a new game when the application starts

    def set_speed(self, speed):
        """Sets the game speed."""
        self.speed = speed

    def start_new_game(self):
        # Reset game state
        self.snake = [(100, 100), (80, 100), (60, 100)]  # Snake starts with 3 segments
        self.direction = "Right"
        self.food = self.create_food()
        self.score = 0
        self.score_label.config(text="Score: 0")
        self.running = True

        # Clear the canvas
        self.canvas.delete("all")

        # Create game elements
        self.create_snake()
        self.create_food_item()
        self.bind_keys()

        # Remove restart button if it exists
        if self.restart_button:
            self.restart_button.destroy()
            self.restart_button = None

        # Start the game loop
        self.game_loop()

    def create_snake(self):
        for i, (x, y) in enumerate(self.snake):
            if i == 0:  # Head of the snake
                color = HEAD_COLOR
            else:
                color = SNAKE_COLOR
            self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=color, tag="snake")

    def create_food(self):
        while True:
            x = random.randrange(0, WIDTH // SNAKE_SIZE) * SNAKE_SIZE
            y = random.randrange(0, HEIGHT // SNAKE_SIZE) * SNAKE_SIZE
            if (x, y) not in self.snake:  # Ensure food doesn't spawn inside the snake
                return (x, y)

    def create_food_item(self):
        x, y = self.food
        self.food_color = "#{:02x}{:02x}{:02x}".format(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))  # Generate a random hex color
        self.canvas.create_rectangle(x, y, x + SNAKE_SIZE, y + SNAKE_SIZE, fill=self.food_color, tag="food")

    def bind_keys(self):
        self.master.bind("<Up>", lambda event: self.change_direction("Up"))
        self.master.bind("<Down>", lambda event: self.change_direction("Down"))
        self.master.bind("<Left>", lambda event: self.change_direction("Left"))
        self.master.bind("<Right>", lambda event: self.change_direction("Right"))

    def change_direction(self, new_direction):
        if (new_direction == "Up" and self.direction != "Down") or \
           (new_direction == "Down" and self.direction != "Up") or \
           (new_direction == "Left" and self.direction != "Right") or \
           (new_direction == "Right" and self.direction != "Left"):
            self.direction = new_direction

    def move_snake(self):
        head_x, head_y = self.snake[0]
        if self.direction == "Up":
            new_head = (head_x, head_y - SNAKE_SIZE)
        elif self.direction == "Down":
            new_head = (head_x, head_y + SNAKE_SIZE)
        elif self.direction == "Left":
            new_head = (head_x - SNAKE_SIZE, head_y)
        elif self.direction == "Right":
            new_head = (head_x + SNAKE_SIZE, head_y)

        self.snake.insert(0, new_head)

        if self.snake[0] == self.food:
            self.score += 1  # Increment score by 1
            self.score_label.config(text="Score: {}".format(self.score))
            self.food = self.create_food()
            self.canvas.delete("food")  # Remove the old food
            self.create_food_item()  # Create the new food
        else:
            self.snake.pop()  # Remove the tail segment if no food was eaten

    def check_collision(self):
        head_x, head_y = self.snake[0]
        if head_x < 0 or head_x >= WIDTH or head_y < 0 or head_y >= HEIGHT:
            return True

        if self.snake[0] in self.snake[1:]:  # Check if head collides with body
            return True

        return False

    def game_over(self):
        self.running = False
        self.canvas.delete("snake", "food")
        self.canvas.create_text(WIDTH/2, HEIGHT/2, text="Game Over! Score: {}".format(self.score),
                                font=("Arial", 24), fill="white")

        # Create restart button
        self.restart_button = tk.Button(self.master, text="Restart", command=self.start_new_game)
        self.restart_button.pack()

    def update(self):
        self.move_snake()

        if self.check_collision():
            self.game_over()
            return # Stop updating after game over


        self.canvas.delete("snake")  # Remove the old snake
        self.create_snake()

    def game_loop(self):
        if self.running:
            self.update()
            self.master.after(self.speed, self.game_loop) # Call the function again after delay
        else:
            #Do nothing when not running
            pass

root = tk.Tk()
game = SnakeGame(root)
root.mainloop()
