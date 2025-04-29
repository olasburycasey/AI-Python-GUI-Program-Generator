import tkinter as tk
from tkinter import ttk

class EmpireStateGUI:
    def __init__(self, master):
        self.master = master
        master.title("Floating Empire State Building")

        self.canvas_width = 600
        self.canvas_height = 400
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="skyblue") # Sky background
        self.canvas.pack()

        self.draw_island()
        self.draw_empire_state_building()

    def draw_island(self):
        """Draws a floating island."""
        island_color = "forestgreen"
        dirt_color = "saddlebrown"

        # Rounded rectangle for the island
        island_x1 = self.canvas_width * 0.2
        island_y1 = self.canvas_height * 0.6
        island_x2 = self.canvas_width * 0.8
        island_y2 = self.canvas_height * 0.9

        self.canvas.create_oval(island_x1, island_y1, island_x2, island_y2,
                                fill=island_color, outline=island_color)

        # Add a bit of dirt/rock below
        dirt_x1 = island_x1 + 20
        dirt_y1 = island_y2 - 20
        dirt_x2 = island_x2 - 20
        dirt_y2 = island_y2 + 40
        self.canvas.create_oval(dirt_x1, dirt_y1, dirt_x2, dirt_y2,
                                fill=dirt_color, outline=dirt_color)

    def draw_empire_state_building(self):
        """Draws a simplified Empire State Building."""
        base_color = "lightgray"
        middle_color = "silver"
        top_color = "gainsboro"  # A slightly lighter gray

        # Building proportions (adjust as desired)
        building_width = 50
        building_height = 150

        # Coordinates for the building
        building_x = self.canvas_width // 2 - building_width // 2  # Center horizontally
        building_y = self.canvas_height * 0.6 - building_height    # Place on the island

        # Base (rectangle)
        base_height = building_height * 0.4
        base_x1 = building_x
        base_y1 = building_y + building_height - base_height
        base_x2 = building_x + building_width
        base_y2 = building_y + building_height
        self.canvas.create_rectangle(base_x1, base_y1, base_x2, base_y2,
                                      fill=base_color, outline="black")

        # Middle section (smaller rectangle)
        middle_height = building_height * 0.3
        middle_width = building_width * 0.8
        middle_x1 = building_x + building_width * 0.1
        middle_y1 = building_y + building_height - base_height - middle_height
        middle_x2 = building_x + building_width * 0.9
        middle_y2 = building_y + building_height - base_height
        self.canvas.create_rectangle(middle_x1, middle_y1, middle_x2, middle_y2,
                                      fill=middle_color, outline="black")


        # Top section (smallest rectangle)
        top_height = building_height * 0.3
        top_width = building_width * 0.6
        top_x1 = building_x + building_width * 0.2
        top_y1 = building_y
        top_x2 = building_x + building_width * 0.8
        top_y2 = building_y + top_height
        self.canvas.create_rectangle(top_x1, top_y1, top_x2, top_y2,
                                      fill=top_color, outline="black")

        # Antenna (line)
        antenna_x = self.canvas_width // 2
        antenna_y1 = building_y
        antenna_y2 = building_y - 20  # Extend the antenna up
        self.canvas.create_line(antenna_x, antenna_y1, antenna_x, antenna_y2, width=2)




root = tk.Tk()
gui = EmpireStateGUI(root)
root.mainloop()