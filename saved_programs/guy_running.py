import tkinter as tk
from tkinter import ttk, Canvas

def draw_running_guy_crossing_finish_line(canvas):
    """Draws a running guy crossing the finish line on the canvas."""

    # --- Define Colors and Sizes ---
    bg_color = "lightgray"  # Background color
    track_color = "gray"    # Track color
    line_color = "white"    # Finish line color
    guy_color = "blue"      # Runner color
    head_size = 20          # Size of the runner's head
    body_length = 60        # Length of the runner's body
    arm_length = 40         # Length of runner's arms
    leg_length = 50         # Length of runner's legs
    finish_line_width = 5   # Width of the finish line
    checker_size = 10       # Size of each checker square

    # --- Track and Background ---
    canvas.create_rectangle(0, 0, canvas.winfo_width(), canvas.winfo_height(), fill=bg_color, outline="")
    track_height = canvas.winfo_height() // 4  # Occupy the lower quarter of the canvas
    track_y_start = canvas.winfo_height() - track_height
    canvas.create_rectangle(0, track_y_start, canvas.winfo_width(), canvas.winfo_height(), fill=track_color, outline="")

    # --- Finish Line (Checker Pattern) ---
    finish_line_x = canvas.winfo_width() * 0.8  # Finish line at 80% of canvas width
    num_checkers_vertical = track_height // checker_size  # How many checkers fit vertically
    
    for i in range(num_checkers_vertical):
        y1 = track_y_start + i * checker_size
        y2 = y1 + checker_size
        
        # Alternate black and white squares
        if i % 2 == 0:
            color1 = "black"
            color2 = "white"
        else:
            color1 = "white"
            color2 = "black"
        
        canvas.create_rectangle(finish_line_x - finish_line_width // 2, y1, 
                                finish_line_x + finish_line_width // 2, y2, 
                                fill=color1, outline="")
        
    # --- Runner ---
    runner_x = canvas.winfo_width() * 0.3  # Runner starts at 30% of canvas width
    runner_y = track_y_start - head_size - body_length - leg_length // 2  # Calculated y-position based on body parts

    # Head
    canvas.create_oval(runner_x - head_size // 2, runner_y - head_size // 2,
                       runner_x + head_size // 2, runner_y + head_size // 2, fill=guy_color, outline="black")

    # Body
    body_y_start = runner_y + head_size // 2
    canvas.create_line(runner_x, body_y_start, runner_x, body_y_start + body_length, width=3, fill=guy_color)

    # Arms (running posture)
    arm_y = body_y_start + body_length // 4  # Arms start slightly down the body
    canvas.create_line(runner_x, arm_y, runner_x - arm_length // 2, arm_y - arm_length // 2, width=3, fill=guy_color) # Back arm
    canvas.create_line(runner_x, arm_y, runner_x + arm_length // 2, arm_y + arm_length // 2, width=3, fill=guy_color) # Front arm

    # Legs (running posture, with bend)
    leg_y_start = body_y_start + body_length

    # Back leg (bent)
    back_leg_x_start = runner_x
    back_leg_y_start = leg_y_start
    back_leg_x_mid = runner_x - leg_length // 4  # Slightly bent back
    back_leg_y_mid = leg_y_start + leg_length // 4
    back_leg_x_end = runner_x - leg_length // 2
    back_leg_y_end = leg_y_start + leg_length // 2
    canvas.create_line(back_leg_x_start, back_leg_y_start, back_leg_x_mid, back_leg_y_mid, width=3, fill=guy_color)
    canvas.create_line(back_leg_x_mid, back_leg_y_mid, back_leg_x_end, back_leg_y_end, width=3, fill=guy_color)


    # Front leg (bent)
    front_leg_x_start = runner_x
    front_leg_y_start = leg_y_start
    front_leg_x_mid = runner_x + leg_length // 4  # Slightly bent forward
    front_leg_y_mid = leg_y_start - leg_length // 4
    front_leg_x_end = runner_x + leg_length // 2
    front_leg_y_end = leg_y_start - leg_length // 2
    canvas.create_line(front_leg_x_start, front_leg_y_start, front_leg_x_mid, front_leg_y_mid, width=3, fill=guy_color)
    canvas.create_line(front_leg_x_mid, front_leg_y_mid, front_leg_x_end, front_leg_y_end, width=3, fill=guy_color)




def resize_canvas(event):
    """Redraws the image when the canvas is resized."""
    draw_running_guy_crossing_finish_line(canvas)

# --- Create the main window ---
root = tk.Tk()
root.title("Running Guy GUI")

# --- Create the Canvas widget ---
canvas_width = 800
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(fill="both", expand=True)  # Allow canvas to expand to fill the window

# --- Draw initial image ---
draw_running_guy_crossing_finish_line(canvas)

# --- Bind resize event to redraw the image ---
canvas.bind("<Configure>", resize_canvas)


root.mainloop()
