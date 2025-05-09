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
        self.initial_frog_x = self.width // 2 - self.frog_size // 2
        self.initial_frog_y = self.height - self.frog_size - 10
        self.frog_x = self.initial_frog_x
        self.frog_y = self.initial_frog_y
        self.frog = self.canvas.create_rectangle(self.frog_x, self.frog_y, self.frog_x + self.frog_size, self.frog_y + self.frog_size, fill="green", tags="frog")

        self.score = 0
        self.lives = 3
        self.score_label = tk.Label(master, text="Score: 0", bg="white")
        self.score_label.pack()
        self.lives_label = tk.Label(master, text="Lives: 3", bg="white")
        self.lives_label.pack()

        self.game_over_label = None
        self.restart_button = None

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
        self.obstacles = [] # Clear any existing obstacles.
        for i, lane in enumerate(self.lanes):
            y = self.height - (i + 1) * self.lane_height
            obstacle_width = random.randint(50, 100)
            obstacle_spacing = random.randint(150, 250)

            num_obstacles = self.width // (obstacle_width + obstacle_spacing) + 2
            x = -obstacle_width if lane["direction"] == 1 else self.width

            for _ in range(num_obstacles):
                x += (obstacle_width + obstacle_spacing) * lane["direction"]
                if lane["type"] == "water":
                    color = "brown"
                else:
                    color = "red"

                obstacle = self.canvas.create_rectangle(x, y, x + obstacle_width, y + self.lane_height, fill=color, tags="obstacle")
                self.obstacles.append({
                    "object": obstacle,
                    "x": x,
                    "y": y,
                    "width": obstacle_width,
                    "height": self.lane_height,
                    "speed": lane["speed"],
                    "direction": lane["direction"],
                    "type": lane["type"]
                })

    def move_frog(self, event):
        if not self.game_running:
            return

        move_distance = self.lane_height

        if event.keysym == "Up":
            new_x, new_y = self.frog_x, self.frog_y - move_distance
        elif event.keysym == "Down":
            new_x, new_y = self.frog_x, self.frog_y + move_distance
        elif event.keysym == "Left":
            new_x, new_y = self.frog_x - move_distance, self.frog_y
        elif event.keysym == "Right":
            new_x, new_y = self.frog_x + move_distance, self.frog_y
        else:
            return # Ignore other keys

        # Keep frog within bounds (before moving)
        new_x = max(0, min(new_x, self.width - self.frog_size))
        new_y = max(0, min(new_y, self.height - self.frog_size))

        self.frog_x, self.frog_y = new_x, new_y
        self.canvas.move(self.frog, new_x - self.frog_x, new_y - self.frog_y) #Move in smaller increments to prevent leaving the water lane.
        self.canvas.coords(self.frog, self.frog_x, self.frog_y, self.frog_x + self.frog_size, self.frog_y + self.frog_size) # Ensure frog stays inside bounds.

        if event.keysym == "Up":
            self.score += 10  # Increment score for each successful move forward
            self.update_score()
            self.check_win()

    def update_obstacles(self):
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
            self.canvas.coords(obstacle, obstacle_data["x"], obstacle_data["y"], obstacle_data["x"] + obstacle_data["width"], obstacle_data["y"] + obstacle_data["height"])

    def check_collision(self):
        frog_x1, frog_y1, frog_x2, frog_y2 = self.canvas.coords(self.frog)
        frog_bbox = (frog_x1, frog_y1, frog_x2, frog_y2) #Create a bounding box for the frog.

        #Check if the frog is in the water
        frog_lane_index = int((self.height - self.frog_y) / self.lane_height) -1
        if 0 <= frog_lane_index < len(self.lanes) and self.lanes[frog_lane_index]["type"] == "water":
            #Check for collision with logs.
            is_on_log = False
            for obstacle_data in self.obstacles:
                if obstacle_data["type"] == "water":
                    obstacle_x1, obstacle_y1, obstacle_x2, obstacle_y2 = self.canvas.coords(obstacle_data["object"])
                    obstacle_bbox = (obstacle_x1, obstacle_y1, obstacle_x2, obstacle_y2)
                    if self.bbox_overlap(frog_bbox, obstacle_bbox):
                        is_on_log = True
                        self.frog_x += obstacle_data["speed"] * obstacle_data["direction"] #Carry the frog.
                        self.canvas.move(self.frog, obstacle_data["speed"] * obstacle_data["direction"], 0)
                        self.frog_x = max(0, min(self.frog_x, self.width - self.frog_size)) # Keep frog within bounds.
                        self.canvas.coords(self.frog, self.frog_x, self.frog_y, self.frog_x + self.frog_size, self.frog_y + self.frog_size) #Update frog coordinates.
                        break #Don't check the rest of logs.
            if not is_on_log:
                self.lose_life()
                return True #exit the function.

        #Check for collisions with road vehicles.
        for obstacle_data in self.obstacles:
            if obstacle_data["type"] == "road":
                obstacle_x1, obstacle_y1, obstacle_x2, obstacle_y2 = self.canvas.coords(obstacle_data["object"])
                obstacle_bbox = (obstacle_x1, obstacle_y1, obstacle_x2, obstacle_y2)
                if self.bbox_overlap(frog_bbox, obstacle_bbox):
                    self.lose_life()
                    return True
        return False

    def bbox_overlap(self, bbox1, bbox2):
        #Check if two bounding boxes overlap.
        x1_1, y1_1, x1_2, y1_2 = bbox1
        x2_1, y2_1, x2_2, y2_2 = bbox2
        return not (x1_2 < x2_1 or x1_1 > x2_2 or y1_2 < y2_1 or y1_1 > y2_2)

    def lose_life(self):
        self.lives -= 1
        self.update_lives()
        if self.lives <= 0:
            self.game_over()
        else:
            self.reset_frog()

    def reset_frog(self):
        self.frog_x = self.initial_frog_x
        self.frog_y = self.initial_frog_y
        self.canvas.coords(self.frog, self.frog_x, self.frog_y, self.frog_x + self.frog_size, self.frog_y + self.frog_size)

    def update_score(self):
        self.score_label.config(text=f"Score: {self.score}")

    def update_lives(self):
        self.lives_label.config(text=f"Lives: {self.lives}")

    def check_win(self):
        if self.frog_y < self.lane_height:
            self.score += 500
            self.update_score()
            self.reset_frog()

    def game_over(self):
        self.game_running = False
        if self.game_over_label:
            self.game_over_label.destroy()
        if self.restart_button:
            self.restart_button.destroy()

        self.game_over_label = tk.Label(self.master, text="Game Over!", bg="red", font=("Arial", 24))
        self.game_over_label.pack()

        self.restart_button = tk.Button(self.master, text="Restart", command=self.restart_game)
        self.restart_button.pack()

    def restart_game(self):
        if self.game_over_label:
            self.game_over_label.destroy()
            self.game_over_label = None
        if self.restart_button:
            self.restart_button.destroy()
            self.restart_button = None

        self.score = 0
        self.lives = 3
        self.update_score()
        self.update_lives()
        self.reset_frog()
        self.create_obstacles()  # Reset obstacles
        self.game_running = True
        self.update()

    def update(self):
        if self.game_running:
            self.update_obstacles()
            self.check_collision()
            self.master.after(20, self.update)

root = tk.Tk()
game = FroggerGame(root)
root.mainloop()