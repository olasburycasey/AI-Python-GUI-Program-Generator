import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk, ImageDraw

class CatAndMouseGUI:
    def __init__(self, master):
        self.master = master
        master.title("Cat and Mouse Image")

        self.canvas_width = 400
        self.canvas_height = 300
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")  # Start with a white background
        self.draw = ImageDraw.Draw(self.image)
        self.photo = ImageTk.PhotoImage(self.image)  # Initially blank canvas

        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.cat_x = 50  # Initial position of the cat
        self.cat_y = 150
        self.mouse_x = 300  # Initial position of the mouse
        self.mouse_y = 150

        self.draw_static_image()


    def draw_cat(self, x, y):
        # Simple cat drawing
        self.draw.ellipse((x - 15, y - 15, x + 15, y + 15), fill="orange")  # Body
        self.draw.polygon([(x - 15, y - 15), (x - 20, y - 25), (x - 10, y - 25)], fill="orange") #Left ear
        self.draw.polygon([(x + 15, y - 15), (x + 20, y - 25), (x + 10, y - 25)], fill="orange") #Right ear
        self.draw.ellipse((x - 5, y - 5, x + 5, y + 5), fill="black") #Nose


    def draw_mouse(self, x, y):
        # Simple mouse drawing
        self.draw.ellipse((x - 10, y - 10, x + 10, y + 10), fill="gray")  # Body
        self.draw.ellipse((x - 10, y - 20, x - 2, y - 12), fill="pink") # Left Ear
        self.draw.ellipse((x + 2, y - 20, x + 10, y - 12), fill="pink") # Right Ear

    def draw_static_image(self):
        # Clear the canvas
        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)

        # Draw the cat and mouse at their initial positions
        self.draw_cat(self.cat_x, self.cat_y)
        self.draw_mouse(self.mouse_x, self.mouse_y)

        # Update the canvas
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfig(self.canvas.find_all()[0], image=self.photo)

root = tk.Tk()
gui = CatAndMouseGUI(root)
root.mainloop()
