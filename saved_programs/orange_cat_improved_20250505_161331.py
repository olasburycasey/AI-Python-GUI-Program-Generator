import tkinter as tk
from tkinter import Canvas
import traceback
import random

class OrangeCatGUI:
    """
    A GUI for drawing an orange cat using Tkinter's Canvas widget.
    Includes error handling and customizable features.
    """

    def __init__(self, master, cat_color="orange", eye_color="yellow", whisker_color="black", nose_color="pink", rug_color="lightgreen"):
        """
        Initializes the OrangeCatGUI.

        Args:
            master: The Tkinter root window.
            cat_color (str): The color of the cat's fur (default: "orange").
            eye_color (str): The color of the cat's eyes (default: "yellow").
            whisker_color (str): The color of the cat's whiskers (default: "black").
            nose_color (str): The color of the cat's nose (default: "pink").
            rug_color (str): The color of the rug (default: "lightgreen").
        """
        self.master = master
        master.title("Orange Cat")

        self.cat_color = cat_color
        self.eye_color = eye_color
        self.whisker_color = whisker_color
        self.nose_color = nose_color
        self.rug_color = rug_color

        self.canvas_width = 400  # Increased canvas size
        self.canvas_height = 400
        self.canvas = Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        try:
            self.draw_cat()
        except Exception as e:
            print(f"Error drawing cat: {e}")
            traceback.print_exc()  # Print detailed error information

    def draw_cat(self):
        """Draws the orange cat on the canvas. Uses relative coordinates for better scaling."""
        try:
            # --- Helper function for relative coordinates ---
            def scale_x(x):
                return x * self.canvas_width

            def scale_y(y):
                return y * self.canvas_height

            # --- Rug ---
            rug_x1 = scale_x(0)
            rug_y1 = scale_y(0.7)
            rug_x2 = scale_x(1)
            rug_y2 = scale_y(1)
            self.canvas.create_rectangle(rug_x1, rug_y1, rug_x2, rug_y2, fill=self.rug_color, outline="") #Removed outline

            # --- Head ---
            head_x1 = scale_x(0.125)  # 50 / 400
            head_y1 = scale_y(0.125)  # 50 / 400
            head_x2 = scale_x(0.625)  # 250 / 400
            head_y2 = scale_y(0.5)    # 200 / 400

            self.canvas.create_oval(head_x1, head_y1, head_x2, head_y2, fill=self.cat_color, outline="black")


            # --- Ears ---
            ear_points_left = [scale_x(0.1875), scale_y(0.175),  #75/400, 70/400 Moved down
                               scale_x(0.3125), scale_y(0.05),    #125/400, 20/400 Moved down
                               scale_x(0.4375), scale_y(0.175)]   #175/400, 70/400 Moved down

            ear_points_right = [scale_x(0.5625), scale_y(0.175), #225/400, 70/400 Moved down
                                scale_x(0.4375), scale_y(0.05),   #175/400, 20/400 Moved down
                                scale_x(0.6875), scale_y(0.175)]  #275/400, 70/400  CHANGED THIS LINE

            self.canvas.create_polygon(ear_points_left, fill=self.cat_color, outline="black")
            self.canvas.create_polygon(ear_points_right, fill=self.cat_color, outline="black") # Added the right ear


            # --- Eyes ---
            eye_x1 = scale_x(0.2)   #80/400
            eye_y1 = scale_y(0.225) #90/400
            eye_x2 = scale_x(0.325) #130/400
            eye_y2 = scale_y(0.35)  #140/400

            self.canvas.create_oval(eye_x1, eye_y1, eye_x2, eye_y2, fill=self.eye_color, outline="black")

            eye_x3 = scale_x(0.425) #170/400
            eye_y3 = scale_y(0.225) #90/400
            eye_x4 = scale_x(0.55)  #220/400
            eye_y4 = scale_y(0.35)  #140/400
            self.canvas.create_oval(eye_x3, eye_y3, eye_x4, eye_y4, fill=self.eye_color, outline="black")

            # --- Pupils ---
            pupil_x1 = scale_x(0.2375) #95/400
            pupil_y1 = scale_y(0.2625) #105/400
            pupil_x2 = scale_x(0.2875) #115/400
            pupil_y2 = scale_y(0.3125) #125/400
            self.canvas.create_oval(pupil_x1, pupil_y1, pupil_x2, pupil_y2, fill="black")

            pupil_x3 = scale_x(0.4625) #185/400
            pupil_y3 = scale_y(0.2625) #105/400
            pupil_x4 = scale_x(0.5125) #205/400
            pupil_y4 = scale_y(0.3125) #125/400

            self.canvas.create_oval(pupil_x3, pupil_y3, pupil_x4, pupil_y4, fill="black")


            # --- Nose ---
            nose_points = [scale_x(0.35),  scale_y(0.35),  #140/400, 140/400
                           scale_x(0.4),    scale_y(0.35),  #160/400, 140/400
                           scale_x(0.375),  scale_y(0.4)]    #150/400, 160/400

            self.canvas.create_polygon(nose_points, fill=self.nose_color, outline="black")


            # --- Mouth ---
            mouth_x1 = scale_x(0.25)  #100/400
            mouth_y1 = scale_y(0.375) #150/400
            mouth_x2 = scale_x(0.5)   #200/400
            mouth_y2 = scale_y(0.45)  #180/400

            self.canvas.create_arc(mouth_x1, mouth_y1, mouth_x2, mouth_y2, start=0, extent=-180, style=tk.ARC, outline="black")

            # --- Whiskers ---
            whisker_x_start = scale_x(0.2) # Moved to be closer to the nose
            whisker_x_end   = scale_x(0.05) # Moved to be closer to the nose
            whisker_y1 = scale_y(0.35)
            whisker_y2 = scale_y(0.4)
            whisker_y3 = scale_y(0.45)

            self.canvas.create_line(whisker_x_start, scale_y(0.375), whisker_x_end, whisker_y1, width=2, fill=self.whisker_color)
            self.canvas.create_line(whisker_x_start, whisker_y2, whisker_x_end, whisker_y2, width=2, fill=self.whisker_color)
            self.canvas.create_line(whisker_x_start, scale_y(0.425), whisker_x_end, whisker_y3, width=2, fill=self.whisker_color)


            whisker_x_start = scale_x(0.55) # Moved to be closer to the nose
            whisker_x_end   = scale_x(0.7) # Moved to be closer to the nose

            self.canvas.create_line(whisker_x_start, scale_y(0.375), whisker_x_end, whisker_y1, width=2, fill=self.whisker_color)
            self.canvas.create_line(whisker_x_start, whisker_y2, whisker_x_end, whisker_y2, width=2, fill=self.whisker_color)
            self.canvas.create_line(whisker_x_start, scale_y(0.425), whisker_x_end, whisker_y3, width=2, fill=self.whisker_color)


            # --- Body (Simplified) ---
            body_x1 = scale_x(0.1875) #75/400
            body_y1 = scale_y(0.45)   #180/400
            body_x2 = scale_x(0.5625) #225/400
            body_y2 = scale_y(0.7)    #280/400

            self.canvas.create_oval(body_x1, body_y1, body_x2, body_y2, fill=self.cat_color, outline="black")

            # --- Legs ---
            leg_width = scale_x(0.05)  # Width of the legs
            leg_height = scale_y(0.1)  # Height of the legs
            # Front left leg
            leg1_x1 = scale_x(0.2)  # Starting x position of the leg
            leg1_y1 = scale_y(0.6)  # Starting y position of the leg
            self.canvas.create_rectangle(leg1_x1, leg1_y1, leg1_x1 + leg_width, leg1_y1 + leg_height, fill=self.cat_color, outline="black")

            # Front right leg
            leg2_x1 = scale_x(0.3)  # Starting x position of the leg
            leg2_y1 = scale_y(0.6)  # Starting y position of the leg
            self.canvas.create_rectangle(leg2_x1, leg2_y1, leg2_x1 + leg_width, leg2_y1 + leg_height, fill=self.cat_color, outline="black")

            # Back left leg
            leg3_x1 = scale_x(0.4)  # Starting x position of the leg
            leg3_y1 = scale_y(0.6)  # Starting y position of the leg
            self.canvas.create_rectangle(leg3_x1, leg3_y1, leg3_x1 + leg_width, leg3_y1 + leg_height, fill=self.cat_color, outline="black")

            # Back right leg
            leg4_x1 = scale_x(0.5)  # Starting x position of the leg
            leg4_y1 = scale_y(0.6)  # Starting y position of the leg
            self.canvas.create_rectangle(leg4_x1, leg4_y1, leg4_x1 + leg_width, leg4_y1 + leg_height, fill=self.cat_color, outline="black")

            # --- Tail ---
            tail_x1 = scale_x(0.5625) #225/400
            tail_y1 = scale_y(0.575)   #230/400
            tail_x2 = scale_x(0.6875) #275/400
            tail_y2 = scale_y(0.7)   #280/400

            self.canvas.create_line(tail_x1, tail_y1, tail_x2, tail_y2, width=10, fill=self.cat_color)

        except tk.TclError as e:  # Catch Tkinter-specific errors
            print(f"Tkinter error during drawing: {e}")
            traceback.print_exc()
        except Exception as e:  # Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            traceback.print_exc()


if __name__ == "__main__":
    root = tk.Tk()
    my_gui = OrangeCatGUI(root)  # Default orange cat
    # my_gui = OrangeCatGUI(root, cat_color="gray", eye_color="green") # A gray cat with green eyes
    root.mainloop()