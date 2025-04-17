import tkinter as tk
from tkinter import ttk, Canvas

class BearOwlImage:
    def __init__(self, master):
        self.master = master
        master.title("BEARS EAT OWLS")  # Changed title here

        self.canvas_width = 400
        self.canvas_height = 300
        self.canvas = Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack(pady=20)

        self.draw_bear()
        self.draw_owl()
        self.add_text()


    def draw_bear(self):
        bear_color = "maroon"  # Changed bear color to maroon

        # Draw the bear's body
        self.canvas.create_oval(100, 150, 300, 250, fill=bear_color, outline="black")  # Body

        # Draw the bear's head
        self.canvas.create_oval(70, 80, 170, 170, fill=bear_color, outline="black")  # Head

        # Draw the bear's ears
        self.canvas.create_oval(60, 70, 90, 100, fill=bear_color, outline="black")  # Left ear
        self.canvas.create_oval(150, 70, 180, 100, fill=bear_color, outline="black") # Right ear

        # Draw the bear's snout
        self.canvas.create_oval(60, 130, 100, 160, fill="darkgray", outline="black") #Snout

        #Draw the bear's nose
        self.canvas.create_oval(60,145, 80, 160, fill = "black", outline = "black")

        # Draw bear's eyes
        self.canvas.create_oval(90, 100, 110, 120, fill="white", outline="black")  # Left eye
        self.canvas.create_oval(120, 100, 140, 120, fill="white", outline="black")  # Right eye

        # Draw bear's pupils
        self.canvas.create_oval(95, 105, 105, 115, fill="black")  # Left pupil
        self.canvas.create_oval(125, 105, 135, 115, fill="black")  # Right pupil


        # Draw bear's arms/paws
        self.canvas.create_oval(120, 220, 150, 250, fill=bear_color, outline="black") #left paw
        self.canvas.create_oval(250, 220, 280, 250, fill=bear_color, outline="black") #right paw

        # Draw bear's teeth
        self.draw_bear_teeth(70, 150)  # Position teeth near the snout


    def draw_bear_teeth(self, x, y):
        # Draw some simple teeth
        self.canvas.create_line(x, y, x + 5, y - 10, fill="white", width=2)
        self.canvas.create_line(x + 10, y, x + 15, y - 10, fill="white", width=2)
        self.canvas.create_line(x + 20, y, x + 25, y - 10, fill="white", width=2)


    def draw_owl(self):
        owl_color = "blue" # changed owl color to blue

        # Owl body
        self.owl_body = self.canvas.create_oval(50, 30, 90, 70, fill=owl_color, outline="black")

        # Owl head
        self.owl_head = self.canvas.create_oval(40, 10, 100, 50, fill=owl_color, outline="black")

        # Owl eyes
        self.owl_eye1 = self.canvas.create_oval(50, 20, 65, 35, fill="yellow", outline="black")
        self.owl_eye2 = self.canvas.create_oval(75, 20, 90, 35, fill="yellow", outline="black")

        #Owl pupils
        self.owl_pupil1 = self.canvas.create_oval(55, 25, 60, 30, fill = "black")
        self.owl_pupil2 = self.canvas.create_oval(80, 25, 85, 30, fill = "black")

        # Owl beak
        points = [70, 35, 60, 45, 80, 45]
        self.owl_beak = self.canvas.create_polygon(points, fill="orange", outline="black")

        # Owl feet
        self.owl_foot1 = self.canvas.create_line(60, 70, 55, 80, fill="orange", width=2)
        self.owl_foot2 = self.canvas.create_line(80, 70, 85, 80, fill="orange", width=2)


        self.owl_parts = [self.owl_body, self.owl_head, self.owl_eye1, self.owl_eye2, self.owl_pupil1, self.owl_pupil2, self.owl_beak, self.owl_foot1, self.owl_foot2]

        # Position the owl near the bear's mouth (adjust coordinates as needed)
        self.move_owl(30, 140)
        self.add_owl_blood(30, 140)


    def move_owl(self, x, y):
        for part in self.owl_parts:
            self.canvas.move(part, x, y)  # Move all owl parts together

    def add_owl_blood(self, x, y):
        # Add some blood droplets near the owl
        self.blood_droplet1 = self.canvas.create_oval(x + 10, y + 20, x + 15, y + 25, fill="red", outline="red")
        self.blood_droplet2 = self.canvas.create_oval(x + 20, y + 10, x + 25, y + 15, fill="red", outline="red")
        self.blood_droplet3 = self.canvas.create_oval(x + 30, y + 30, x + 35, y + 35, fill="red", outline="red")
        self.owl_parts.extend([self.blood_droplet1, self.blood_droplet2, self.blood_droplet3])


    def add_text(self):
        # Spread the words further apart by adjusting the x-coordinates

        bears_x = self.canvas_width / 2 - 100 # Adjusted
        owls_x = self.canvas_width / 2 + 100  # Adjusted
        eat_x = self.canvas_width / 2 #Keep Eat centered

        #Create the word bears red
        self.canvas.create_text(bears_x, 20, text="BEARS", font=("Arial", 16, "bold"), fill="red")
        #Create the word owls blue
        self.canvas.create_text(owls_x, 20, text="OWLS", font=("Arial", 16, "bold"), fill="blue")

        #Keep Eat centered
        self.canvas.create_text(eat_x, 20, text="EAT", font=("Arial", 16, "bold"), fill="black")



root = tk.Tk()
my_gui = BearOwlImage(root)
root.mainloop()
