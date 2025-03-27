import tkinter as tk
from PIL import Image, ImageTk, ImageDraw

class BasketballDunkGUI:
    def __init__(self, master):
        self.master = master
        master.title("Basketball Dunk")

        self.canvas_width = 400
        self.canvas_height = 300
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "white")
        self.draw = ImageDraw.Draw(self.image)
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)

        self.draw_dunk()

    def draw_dunk(self):
        # Draw the background
        self.draw.rectangle([(0, self.canvas_height * 0.6), (self.canvas_width, self.canvas_height)], fill="lightgreen") # court
        self.draw.rectangle([(0, 0), (self.canvas_width, self.canvas_height * 0.6)], fill="lightblue") # sky

        # Draw the basketball player
        self.draw_player(150, 150)

        # Draw the hoop and backboard
        self.draw_hoop(300, 80)

        self.photo = ImageTk.PhotoImage(self.image) # Update photo image
        self.canvas.itemconfig(1, image=self.photo)

    def draw_player(self, x, y):
        # Head
        self.draw.ellipse([(x - 20, y - 40), (x + 20, y)], fill="peachpuff", outline="black")

        # Body
        self.draw.rectangle([(x - 15, y), (x + 15, y + 70)], fill="darkblue", outline="black")

        # Arms
        self.draw.rectangle([(x - 30, y + 10), (x - 15, y + 50)], fill="darkblue", outline="black")  # Left arm
        self.draw.rectangle([(x + 15, y + 10), (x + 30, y + 30)], fill="darkblue", outline="black")  # Right arm holding ball

        # Legs
        self.draw.rectangle([(x - 15, y + 70), (x - 5, y + 120)], fill="black", outline="black")  # Left leg
        self.draw.rectangle([(x + 5, y + 70), (x + 15, y + 120)], fill="black", outline="black")  # Right leg

        # Ball
        self.draw.ellipse([(x + 20, y + 10), (x + 50, y + 40)], fill="orange", outline="black")


    def draw_hoop(self, x, y):
        # Backboard
        self.draw.rectangle([(x - 20, y - 20), (x + 20, y + 20)], fill="red", outline="black")

        # Hoop
        self.draw.ellipse([(x - 30, y + 20), (x + 30, y + 50)], outline="red", width=3)


root = tk.Tk()
gui = BasketballDunkGUI(root)
root.mainloop()
