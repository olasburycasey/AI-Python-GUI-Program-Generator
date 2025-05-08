import tkinter as tk
import random

class SnakeGame3D:
    def __init__(self, master):
        self.master = master
        master.title("3D Snake")

        self.width = 600
        self.height = 600
        self.cell_size = 20
        self.grid_width = self.width // self.cell_size
        self.grid_height = self.height // self.cell_size

        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.snake = [(self.grid_width // 2, self.grid_height // 2), (self.grid_width // 2 - 1, self.grid_height // 2)]
        self.direction = (1, 0)  # (x, y) : right
        self.food = self.create_food()
        self.cube_size = self.cell_size * 0.7  # 3D illusion - smaller cubes
        self.snake_color = "green"
        self.food_color = "red"
        self.score = 0
        self.game_over_flag = False
        
        self.score_label = tk.Label(master, text="Score: 0", bg="white")
        self.score_label.pack()


        self.bind_keys()
        self.start_game()

    def create_food(self):
        try:
            while True:
                x = random.randint(0, self.grid_width - 1)
                y = random.randint(0, self.grid_height - 1)
                if (x, y) not in self.snake:
                    return (x, y)
        except Exception as e:
             print(f"Error creating food: {e}")
             return (random.randint(0, self.grid_width - 1), random.randint(0, self.grid_height - 1)) #Return default

    def move_snake(self):
        try:
            head = self.snake[0]
            new_head = (head[0] + self.direction[0], head[1] + self.direction[1])

            if (
                new_head[0] < 0
                or new_head[0] >= self.grid_width
                or new_head[1] < 0
                or new_head[1] >= self.grid_height
                or new_head in self.snake
            ):
                self.game_over()
                return

            self.snake.insert(0, new_head)

            if new_head == self.food:
                self.score += 10
                self.score_label.config(text=f"Score: {self.score}")
                self.food = self.create_food()
            else:
                self.snake.pop()
        except Exception as e:
            print(f"Error moving snake: {e}")
            self.game_over()


    def draw_cube(self, x, y, color):
        try:
            x1 = x * self.cell_size + self.cell_size * 0.15
            y1 = y * self.cell_size + self.cell_size * 0.15
            x2 = x1 + self.cube_size
            y2 = y1 + self.cube_size

            # Draw a 3D-ish cube by drawing rectangles with slight offsets
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="") # Front face
        except Exception as e:
            print(f"Error drawing cube: {e}")


    def draw(self):
        try:
            self.canvas.delete("all")  # Clear the canvas

            for x, y in self.snake:
                self.draw_cube(x, y, self.snake_color)
            
            x, y = self.food
            self.draw_cube(x, y, self.food_color)
        except Exception as e:
            print(f"Error in draw function: {e}")


    def update(self):
        try:
            if not self.game_over_flag:
                self.move_snake()
                self.draw()
                self.master.after(150, self.update)  # Adjust speed here (milliseconds)
        except Exception as e:
            print(f"Error in update function: {e}")
            self.game_over()

    def start_game(self):
        try:
            self.game_over_flag = False
            self.score = 0
            self.score_label.config(text="Score: 0")
            self.snake = [(self.grid_width // 2, self.grid_height // 2), (self.grid_width // 2 - 1, self.grid_height // 2)]
            self.direction = (1, 0)
            self.food = self.create_food()
            self.canvas.delete("all") # Clear game over message if any
            self.update()
        except Exception as e:
             print(f"Error starting game: {e}")

    def game_over(self):
        try:
            self.game_over_flag = True
            self.canvas.create_text(
                self.width / 2,
                self.height / 2,
                text=f"Game Over! Score: {self.score}\nPress 'R' to restart",
                fill="white",
                font=("Arial", 20),
            )
        except Exception as e:
             print(f"Error ending game: {e}")


    def bind_keys(self):
        try:
            self.master.bind("<Up>", lambda event: self.change_direction((0, -1)))
            self.master.bind("<Down>", lambda event: self.change_direction((0, 1)))
            self.master.bind("<Left>", lambda event: self.change_direction((-1, 0)))
            self.master.bind("<Right>", lambda event: self.change_direction((1, 0)))
            self.master.bind("r", lambda event: self.start_game())
        except Exception as e:
            print(f"Error binding keys: {e}")


    def change_direction(self, new_direction):
        try:
            # Prevent the snake from reversing direction immediately
            if (
                new_direction[0] * -1 != self.direction[0]
                or new_direction[1] * -1 != self.direction[1]
            ):
                self.direction = new_direction
        except Exception as e:
            print(f"Error changing direction: {e}")


root = tk.Tk()
game = SnakeGame3D(root)
root.mainloop()