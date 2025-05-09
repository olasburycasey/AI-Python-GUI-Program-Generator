import tkinter as tk
import random

class FroggerGame:
    def __init__(self, master):
        self.master = master
        master.title("Frogger")

        self.width = 500
        self.height = 600
        self.canvas = tk.Canvas(master, width=self.width, height=self.height, bg="black")
        self.canvas.pack()

        self.frog_size = 20
        self.frog_x = self.width // 2 - self.frog_size // 2
        self.frog_y = self.height - self.frog_size - 10
        self.frog = self.canvas.create_rectangle(self.frog_x, self.frog_y, self.frog_x + self.frog_size, self.frog_y + self.frog_size, fill="green")

        self.score = 0
        self.lives = 3
        self.score_label = tk.Label(master, text="Score: 0", bg="white")
        self.score_label.pack()
        self.lives_label = tk.Label(master, text="Lives: 3", bg="white")
        self.lives_label.pack()

        self.game_over_label = None

        self.lane_height = 50
        self.lanes = [
            {"type": "water", "speed": 2, "direction": 1, "color": "blue"},  # Water
            {"type": "water", "speed": 3, "direction": -1, "color": "blue"}, # Water
            {"type": "water", "speed": 2.5, "direction": 1, "color": "blue"}, # Water
            {"type": "road", "speed": 4, "direction": -1, "color": "gray"},   # Road
            {"type": "road", "speed": 3.5, "direction": 1, "color": "gray"},  # Road
            {"type": "road", "speed": 5, "direction": -1, "color": "gray"}    # Road
        ]

        self.obstacles = []
        self.create_obstacles()

        self.canvas.bind("<KeyPress>", self.move_frog)
        self.canvas.focus_set()

        self.game_running = True
        self.update()

    def create_obstacles(self):
        try:
            for i, lane in enumerate(self.lanes):
                y = self.height - (i + 1) * self.lane_height
                obstacle_width = random.randint(50, 100)
                obstacle_x = 0 if lane["direction"] == 1 else self.width - obstacle_width
                obstacle_spacing = random.randint(150, 250)

                num_obstacles = self.width // (obstacle_width + obstacle_spacing) + 2  # Create extra obstacles to ensure continuous coverage

                for j in range(num_obstacles):
                    x = obstacle_x + j * (obstacle_width + obstacle_spacing) * lane["direction"]

                    if lane["type"] == "water":
                        color = "brown"  # Logs
                    else:
                        color = "red"    # Cars

                    obstacle = self.canvas.create_rectangle(x, y, x + obstacle_width, y + self.lane_height, fill=color)
                    self.obstacles.append({"object": obstacle, "x": x, "y": y, "width": obstacle_width, "height": self.lane_height, "speed": lane["speed"], "direction": lane["direction"], "type": lane["type"]})
        except Exception as e:
            print(f"Error creating obstacles: {e}")

    def move_frog(self, event):
        try:
            if not self.game_running:
                return
            move_distance = self.lane_height  # Move a whole lane at a time.

            if event.keysym == "Up":
                self.canvas.move(self.frog, 0, -move_distance)
                self.frog_y -= move_distance
                self.score += 10  # Increment score for each successful move forward
            elif event.keysym == "Down":
                self.canvas.move(self.frog, 0, move_distance)
                self.frog_y += move_distance
            elif event.keysym == "Left":
                self.canvas.move(self.frog, -move_distance, 0)
                self.frog_x -= move_distance
            elif event.keysym == "Right":
                self.canvas.move(self.frog, move_distance, 0)
                self.frog_x += move_distance

            # Keep frog within bounds
            self.frog_x = max(0, min(self.frog_x, self.width - self.frog_size))
            self.frog_y = max(0, min(self.frog_y, self.height - self.frog_size))
            self.canvas.coords(self.frog, self.frog_x, self.frog_y, self.frog_x + self.frog_size, self.frog_y + self.frog_size)

            self.update_score()
            self.check_win()
        except Exception as e:
            print(f"Error moving frog: {e}")

    def update_obstacles(self):
        try:
            for obstacle_data in self.obstacles:
                obstacle = obstacle_data["object"]
                speed = obstacle_data["speed"]
                direction = obstacle_data["direction"]

                self.canvas.move(obstacle, speed * direction, 0)
                obstacle_data["x"] += speed * direction

                # Wrap around obstacles at the edges of the screen
                if direction == 1 and obstacle_data["x"] > self.width:
                    self.canvas.move(obstacle, -self.width - obstacle_data["width"], 0)
                    obstacle_data["x"] -= self.width + obstacle_data["width"]
                elif direction == -1 and obstacle_data["x"] + obstacle_data["width"] < 0:
                    self.canvas.move(obstacle, self.width + obstacle_data["width"], 0)
                    obstacle_data["x"] += self.width + obstacle_data["width"]

                # Update obstacle coordinates within the data structure
                self.canvas.coords(obstacle, obstacle_data["x"], obstacle_data["y"], obstacle_data["x"] + obstacle_data["width"], obstacle_data["y"] + obstacle_data["height"])
        except Exception as e:
            print(f"Error updating obstacles: {e}")


    def check_collision(self):
        try:
            frog_x1, frog_y1, frog_x2, frog_y2 = self.canvas.coords(self.frog)

            for obstacle_data in self.obstacles:
                obstacle_x1, obstacle_y1, obstacle_x2, obstacle_y2 = self.canvas.coords(obstacle_data["object"])

                if frog_x1 < obstacle_x2 and frog_x2 > obstacle_x1 and frog_y1 < obstacle_y2 and frog_y2 > obstacle_y1:
                    if obstacle_data["type"] == "road":
                        self.lose_life()
                        return True
                    elif obstacle_data["type"] == "water":
                        # Frog is on a log - move it along with the log
                        self.frog_x += obstacle_data["speed"] * obstacle_data["direction"]
                        self.canvas.move(self.frog, obstacle_data["speed"] * obstacle_data["direction"], 0)
                        self.canvas.coords(self.frog, self.frog_x, self.frog_y, self.frog_x + self.frog_size, self.frog_y + self.frog_size)
                        return False # Don't lose life
            #Check if the frog is in the water without a log.
            frog_lane_index = int((self.height - self.frog_y) / self.lane_height) -1 #index 0 is the first lane near bottom
            if 0 <= frog_lane_index < len(self.lanes) and self.lanes[frog_lane_index]["type"] == "water":
                #See if the frog is colliding with any logs. If it is not touching a log in this water lane, then lose a life.
                is_on_log = False
                for obstacle_data in self.obstacles:
                    obstacle_x1, obstacle_y1, obstacle_x2, obstacle_y2 = self.canvas.coords(obstacle_data["object"])
                    if obstacle_data["type"] == "water" and frog_x1 < obstacle_x2 and frog_x2 > obstacle_x1 and frog_y1 < obstacle_y2 and frog_y2 > obstacle_y1:
                        is_on_log = True
                        break
                if not is_on_log:
                    self.lose_life()
                    return True

            return False
        except Exception as e:
            print(f"Error checking collision: {e}")
            return False  # Avoid crashing

    def lose_life(self):
        try:
            self.lives -= 1
            self.update_lives()

            if self.lives <= 0:
                self.game_over()
            else:
                self.reset_frog()
        except Exception as e:
            print(f"Error losing life: {e}")


    def reset_frog(self):
        try:
            self.frog_x = self.width // 2 - self.frog_size // 2
            self.frog_y = self.height - self.frog_size - 10
            self.canvas.coords(self.frog, self.frog_x, self.frog_y, self.frog_x + self.frog_size, self.frog_y + self.frog_size)
        except Exception as e:
            print(f"Error resetting frog: {e}")

    def update_score(self):
        try:
            self.score_label.config(text=f"Score: {self.score}")
        except Exception as e:
            print(f"Error updating score: {e}")

    def update_lives(self):
        try:
            self.lives_label.config(text=f"Lives: {self.lives}")
        except Exception as e:
            print(f"Error updating lives: {e}")

    def check_win(self):
        try:
            if self.frog_y < self.lane_height:  # Reached the top (winning condition)
                self.score += 500
                self.update_score()
                self.reset_frog() # Reset frog to start and continue the game
        except Exception as e:
            print(f"Error checking win: {e}")

    def game_over(self):
        try:
            self.game_running = False
            if self.game_over_label:
                self.game_over_label.destroy()

            self.game_over_label = tk.Label(self.master, text="Game Over!", bg="red", font=("Arial", 24))
            self.game_over_label.pack()
        except Exception as e:
            print(f"Error during game over: {e}")

    def update(self):
        try:
            if self.game_running:
                self.update_obstacles()
                self.check_collision() # Check for collisions *after* updating obstacle positions.
                self.master.after(20, self.update) # 20 milliseconds
            else:
                # Do nothing when game is over
                pass
        except Exception as e:
            print(f"Error during update: {e}")
            self.game_running = False #stop game if an error occurs in the update loop.


root = tk.Tk()
game = FroggerGame(root)
root.mainloop()