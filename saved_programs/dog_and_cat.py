import tkinter as tk
from tkinter import ttk

class AnimalDrawer:
    def __init__(self, master):
        self.master = master
        master.title("Black Dog and Orange Cat")

        self.canvas_width = 400
        self.canvas_height = 300

        try:
            self.canvas = tk.Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
            self.canvas.pack()

            self.draw_dog()
            self.draw_cat()
        except Exception as e:
            print(f"Error initializing AnimalDrawer: {e}")
            # Optionally, display an error message in the GUI
            error_label = tk.Label(master, text=f"Error: {e}", fg="red")
            error_label.pack()


    def draw_dog(self):
        try:
            # Dog (Simplified representation)
            dog_x = 50
            dog_y = 150
            dog_size = 80

            # Body
            self.canvas.create_oval(dog_x, dog_y, dog_x + dog_size, dog_y + dog_size * 0.7, fill="black", outline="black")  # Body
            # Head
            self.canvas.create_oval(dog_x - dog_size*0.3, dog_y - dog_size*0.3, dog_x + dog_size*0.3, dog_y + dog_size*0.3, fill="black", outline="black") # Head
            # Tail
            self.canvas.create_line(dog_x+dog_size, dog_y + dog_size * 0.35, dog_x + dog_size + dog_size*0.2, dog_y + dog_size * 0.15, width=3, fill="black")

            # Ear
            self.canvas.create_polygon(dog_x - dog_size*0.3, dog_y-dog_size*0.3, dog_x-dog_size*0.1, dog_y-dog_size*0.6, dog_x+dog_size*0.1, dog_y-dog_size*0.3, fill="black", outline="black")

            # Eyes
            eye_size = dog_size * 0.08
            self.canvas.create_oval(dog_x - dog_size*0.1, dog_y - dog_size*0.1, dog_x - dog_size*0.1 + eye_size, dog_y - dog_size*0.1 + eye_size, fill="white")
            self.canvas.create_oval(dog_x + dog_size*0.05, dog_y - dog_size*0.1, dog_x + dog_size*0.05 + eye_size, dog_y - dog_size*0.1 + eye_size, fill="white")


        except Exception as e:
            print(f"Error drawing dog: {e}")
            # Optionally handle the error, e.g., display a message or log it


    def draw_cat(self):
        try:
            # Cat (Simplified representation)
            cat_x = 250
            cat_y = 150
            cat_size = 70

            # Body
            self.canvas.create_oval(cat_x, cat_y, cat_x + cat_size, cat_y + cat_size * 0.7, fill="orange", outline="orange") # Body
            # Head
            self.canvas.create_oval(cat_x - cat_size*0.3, cat_y - cat_size*0.3, cat_x + cat_size*0.3, cat_y + cat_size*0.3, fill="orange", outline="orange")# Head
            # Tail
            self.canvas.create_line(cat_x+cat_size, cat_y + cat_size * 0.35, cat_x + cat_size + cat_size*0.2, cat_y + cat_size * 0.65, width=3, fill="orange")

            # Ear
            self.canvas.create_polygon(cat_x - cat_size*0.3, cat_y-cat_size*0.3, cat_x-cat_size*0.1, cat_y-cat_size*0.6, cat_x+cat_size*0.1, cat_y-cat_size*0.3, fill="orange", outline="orange")

            # Whiskers
            whisker_length = cat_size * 0.4
            self.canvas.create_line(cat_x - cat_size*0.3, cat_y, cat_x - cat_size*0.3 - whisker_length, cat_y, width=2, fill="black")
            self.canvas.create_line(cat_x - cat_size*0.3, cat_y + cat_size*0.1, cat_x - cat_size*0.3 - whisker_length, cat_y + cat_size*0.1, width=2, fill="black")
            self.canvas.create_line(cat_x - cat_size*0.3, cat_y - cat_size*0.1, cat_x - cat_size*0.3 - whisker_length, cat_y - cat_size*0.1, width=2, fill="black")

            # Eyes
            eye_size = cat_size * 0.1
            self.canvas.create_oval(cat_x - cat_size*0.1, cat_y - cat_size*0.1, cat_x - cat_size*0.1 + eye_size, cat_y - cat_size*0.1 + eye_size, fill="white")
            self.canvas.create_oval(cat_x + cat_size*0.05, cat_y - cat_size*0.1, cat_x + cat_size*0.05 + eye_size, cat_y - cat_size*0.1 + eye_size, fill="white")


        except Exception as e:
            print(f"Error drawing cat: {e}")
            # Optionally handle the error.


root = tk.Tk()
try:
    my_gui = AnimalDrawer(root)
except Exception as e:
    print(f"Error creating AnimalDrawer instance: {e}")
    #Handle initialization error

try:
    root.mainloop()
except Exception as e:
    print(f"Error in mainloop: {e}")