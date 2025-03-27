import tkinter as tk
from PIL import Image, ImageTk, ImageDraw
import random

class GrayTV:
    def __init__(self, master):
        self.master = master
        master.title("Gray TV")

        self.canvas_width = 400
        self.canvas_height = 300
        self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="light blue")  # Set background to a light blue color
        self.canvas.pack()

        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), "black")
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.draw = ImageDraw.Draw(self.image)  # create ImageDraw object

        self.draw_desk()
        self.draw_tv()


    def draw_tv(self):
        """Draws a simple gray TV with static on the screen."""

        # TV outline
        tv_color = (80, 80, 80)  # Gray
        screen_color = (50, 50, 50)  # Darker gray

        tv_x1 = 50
        tv_y1 = 50
        tv_x2 = self.canvas_width - 50
        tv_y2 = self.canvas_height - 50

        # Draw the TV outer frame
        self.draw.rectangle([(tv_x1, tv_y1), (tv_x2, tv_y2)], fill=tv_color, outline="black", width=3)

        # Draw the screen
        screen_x1 = tv_x1 + 10
        screen_y1 = tv_y1 + 10
        screen_x2 = tv_x2 - 10
        screen_y2 = tv_y2 - 10
        self.draw.rectangle([(screen_x1, screen_y1), (screen_x2, screen_y2)], fill=screen_color)

        # Draw the static
        self.draw_static(screen_x1, screen_y1, screen_x2, screen_y2)

        # Update the image on the canvas
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfig(1, image=self.photo)


    def draw_static(self, x1, y1, x2, y2):
        """Draws static on the TV screen."""
        for x in range(x1, x2):
            for y in range(y1, y2):
                gray_value = random.randint(0, 150)  #Lighter static
                self.draw.point((x, y), fill=(gray_value, gray_value, gray_value))

    def draw_desk(self):
        """Draws a simple desk."""
        desk_color = (139, 69, 19)  # Brown
        desk_x1 = 0
        desk_y1 = self.canvas_height - 70
        desk_x2 = self.canvas_width
        desk_y2 = self.canvas_height
        self.draw.rectangle([(desk_x1, desk_y1), (desk_x2, desk_y2)], fill=desk_color)

        # Desk legs (optional)
        leg_width = 20
        leg_height = 40
        leg_color = (101, 67, 33) # Darker brown

        # Left leg
        leg1_x1 = 30
        leg1_y1 = self.canvas_height - 70 # Matches desk top
        leg1_x2 = leg1_x1 + leg_width
        leg1_y2 = self.canvas_height - 30
        self.draw.rectangle([(leg1_x1, leg1_y1), (leg1_x2, leg1_y2)], fill=leg_color)

        #Right leg
        leg2_x1 = self.canvas_width - 30 - leg_width
        leg2_y1 = self.canvas_height - 70
        leg2_x2 = leg2_x1 + leg_width
        leg2_y2 = self.canvas_height - 30
        self.draw.rectangle([(leg2_x1, leg2_y1), (leg2_x2, leg2_y2)], fill=leg_color)

        # Update the image on the canvas
        self.photo = ImageTk.PhotoImage(self.image)
        self.canvas.itemconfig(1, image=self.photo)



root = tk.Tk()
gray_tv = GrayTV(root)
root.mainloop()
