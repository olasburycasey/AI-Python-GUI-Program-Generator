import tkinter as tk
import math

class FidgetSpinnerGUI:
    def __init__(self, master):
        self.master = master
        master.title("Fidget Spinner")

        self.canvas_width = 300
        self.canvas_height = 300
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.spinner_radius = 100
        self.bearing_radius = 20  # Center bearing
        self.blade_radius = 40   # Size of the blades
        self.blade_hole_radius = 10 # Size of the hole in each blade
        self.blade_distance = 60   # Distance of the blade centers from the spinner center
        self.blade_colors = ["red", "green", "blue"]  # List of blade colors
        self.bearing_color = "black"

        self.rotation_angle = 0
        self.rotation_speed = 2

        self.draw_spinner()
        self.animate_spinner()

    def draw_spinner(self):
        self.canvas.delete("all") # Clear the canvas

        # Draw the central bearing
        center_x = self.canvas_width // 2
        center_y = self.canvas_height // 2
        self.canvas.create_oval(center_x - self.bearing_radius, center_y - self.bearing_radius,
                                 center_x + self.bearing_radius, center_y + self.bearing_radius,
                                 fill=self.bearing_color, outline="black")

        # Draw the blades
        for i in range(3):  # Fidget spinners typically have 3 blades
            angle = math.radians(i * 120 + self.rotation_angle)  # 120 degrees between each blade
            blade_center_x = center_x + self.blade_distance * math.cos(angle)
            blade_center_y = center_y + self.blade_distance * math.sin(angle)

            # Draw the blade itself, using the corresponding color
            self.canvas.create_oval(blade_center_x - self.blade_radius, blade_center_y - self.blade_radius,
                                     blade_center_x + self.blade_radius, blade_center_y + self.blade_radius,
                                     fill=self.blade_colors[i], outline="black")

            # Draw the hole in the blade
            self.canvas.create_oval(blade_center_x - self.blade_hole_radius, blade_center_y - self.blade_hole_radius,
                                     blade_center_x + self.blade_hole_radius, blade_center_y + self.blade_hole_radius,
                                     fill="white", outline="black")


    def animate_spinner(self):
        self.rotation_angle += self.rotation_speed
        if self.rotation_angle > 360:
            self.rotation_angle -= 360

        self.draw_spinner()
        self.master.after(20, self.animate_spinner)  # Redraw every 20 milliseconds


root = tk.Tk()
my_gui = FidgetSpinnerGUI(root)
root.mainloop()