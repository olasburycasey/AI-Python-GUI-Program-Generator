import tkinter as tk
from tkinter import ttk, Canvas
from PIL import Image, ImageTk  # Use Pillow instead of PIL
import random


class SchoolImageGenerator:
    def __init__(self, master):
        self.master = master
        master.title("School Image Generator")

        self.canvas_width = 600
        self.canvas_height = 400
        self.canvas = Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="skyblue")  # Sky background
        self.canvas.pack()

        self.draw_school()  # Initial drawing of the school

    def draw_school(self):
        """Draws the school image on the canvas."""

        # Clear the canvas (important for redrawing if needed)
        self.canvas.delete("all")

        # Sky
        self.canvas.create_rectangle(0, 0, self.canvas_width, self.canvas_height, fill="skyblue", outline="")

        # Draw Clouds
        self.draw_clouds(num_clouds=5)  # Added clouds

        # 1. Building (Main Structure)
        building_width = 400
        building_height = 200
        building_x = (self.canvas_width - building_width) // 2
        building_y = self.canvas_height - building_height - 20 # Leave space at bottom for grass

        self.canvas.create_rectangle(building_x, building_y, building_x + building_width, building_y + building_height,
                                     fill="lightgray", outline="black")

        # 2. Roof
        roof_width = building_width + 20
        roof_height = 50
        roof_x = building_x - 10
        roof_y = building_y - roof_height

        points = [roof_x, building_y,
                  roof_x + roof_width // 2, roof_y,
                  roof_x + roof_width, building_y]  # Triangle shape
        self.canvas.create_polygon(points, fill="darkred", outline="black")

        # 3. Windows (Multiple)
        window_width = 40
        window_height = 60
        window_spacing_x = 60
        window_y = building_y + 40
        num_windows = 5

        start_window_x = building_x + (building_width - (num_windows * window_width + (num_windows - 1) * window_spacing_x)) // 2

        for i in range(num_windows):
            window_x = start_window_x + i * (window_width + window_spacing_x)
            self.canvas.create_rectangle(window_x, window_y, window_x + window_width, window_y + window_height,
                                         fill="white", outline="black")
            # Add small grid lines inside each window
            self.canvas.create_line(window_x + window_width // 2, window_y, window_x + window_width // 2, window_y + window_height, fill="lightblue") # Vertical line
            self.canvas.create_line(window_x, window_y + window_height // 2, window_x + window_width, window_y + window_height // 2, fill="lightblue") # Horizontal line



        # 4. Door
        door_width = 50
        door_height = 80
        door_x = building_x + building_width // 2 - door_width // 2
        door_y = building_y + building_height - door_height
        self.canvas.create_rectangle(door_x, door_y, door_x + door_width, building_y + building_height,
                                     fill="brown", outline="black")
        # Door knob
        self.canvas.create_oval(door_x + door_width - 10, door_y + door_height // 2, door_x + door_width - 5, door_y + door_height // 2 + 5, fill="gold")

        # 5. Grass
        grass_height = 20
        grass_y = self.canvas_height - grass_height
        self.canvas.create_rectangle(0, grass_y, self.canvas_width, self.canvas_height, fill="lightgreen", outline="")

        # 6. Sun
        sun_size = 60
        sun_x = 50
        sun_y = 50
        self.canvas.create_oval(sun_x - sun_size // 2, sun_y - sun_size // 2, sun_x + sun_size // 2, sun_y + sun_size // 2, fill="yellow", outline="orange")

    def draw_clouds(self, num_clouds=3):
        """Draws clouds randomly in the sky."""
        for _ in range(num_clouds):
            cloud_x = random.randint(50, self.canvas_width - 50)
            cloud_y = random.randint(20, self.canvas_height // 3)  # Keep clouds in the upper portion
            cloud_size = random.randint(30, 60)
            cloud_color = "white"  # You can vary cloud colors slightly
            self.draw_cloud(cloud_x, cloud_y, cloud_size, cloud_color)


    def draw_cloud(self, x, y, size, color):
      """Draws a single cloud using overlapping circles."""
      for i in range(-1, 2):
          for j in range(-1, 2):
              if (i, j) != (0,0) :
                 self.canvas.create_oval(x + i*size//3 - size // 2, y + j*size//3 - size // 2, x + i*size//3 + size // 2, y + j*size//3 + size // 2, fill=color, outline=color)





root = tk.Tk()
school_generator = SchoolImageGenerator(root)
root.mainloop()