import tkinter as tk
from tkinter import Canvas
import traceback

class OrangeCatGUI:
    def __init__(self, master):
        self.master = master
        master.title("Orange Cat")

        self.canvas = Canvas(master, width=300, height=300, bg="white")
        self.canvas.pack()

        try:
            self.draw_cat()
        except Exception as e:
            print(f"Error drawing cat: {e}")
            traceback.print_exc() # Print detailed error information

    def draw_cat(self):
        try:
            # Head
            self.canvas.create_oval(50, 50, 250, 200, fill="orange", outline="black")

            # Ears
            self.canvas.create_polygon(75, 50, 125, 0, 175, 50, fill="orange", outline="black")
            self.canvas.create_polygon(225, 50, 175, 0, 125, 50, fill="orange", outline="black")


            # Eyes
            self.canvas.create_oval(80, 90, 130, 140, fill="yellow", outline="black")
            self.canvas.create_oval(170, 90, 220, 140, fill="yellow", outline="black")

            # Pupils
            self.canvas.create_oval(95, 105, 115, 125, fill="black")
            self.canvas.create_oval(185, 105, 205, 125, fill="black")

            # Nose
            self.canvas.create_polygon(140, 140, 160, 140, 150, 160, fill="pink", outline="black")

            # Mouth
            self.canvas.create_arc(100, 150, 200, 180, start=0, extent=-180, style=tk.ARC, outline="black")

            # Whiskers
            self.canvas.create_line(50, 150, 70, 140, width=1)
            self.canvas.create_line(50, 160, 70, 160, width=1)
            self.canvas.create_line(50, 170, 70, 180, width=1)

            self.canvas.create_line(250, 150, 230, 140, width=1)
            self.canvas.create_line(250, 160, 230, 160, width=1)
            self.canvas.create_line(250, 170, 230, 180, width=1)

            # Body (Simplified)
            self.canvas.create_oval(75, 180, 225, 280, fill="orange", outline="black")

            # Tail
            self.canvas.create_line(225, 230, 275, 280, width=10, fill="orange")

        except tk.TclError as e:  # Catch Tkinter-specific errors
            print(f"Tkinter error during drawing: {e}")
            traceback.print_exc()
        except Exception as e: #Catch any other unexpected errors
            print(f"An unexpected error occurred: {e}")
            traceback.print_exc()



root = tk.Tk()
my_gui = OrangeCatGUI(root)
root.mainloop()