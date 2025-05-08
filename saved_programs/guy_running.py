import tkinter as tk
from tkinter import ttk, Canvas

def draw_running_guy_crossing_finish_line(canvas, runner_x_offset, has_crossed_finish_line):
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
    runner_start_x = canvas.winfo_width() * 0.3  # Runner starts at 30% of canvas width
    runner_x = runner_start_x + runner_x_offset #runner moves left and right
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

    if has_crossed_finish_line:
        canvas.create_text(canvas.winfo_width() // 2, canvas.winfo_height() // 2,
                           text="Finished!", font=("Arial", 30), fill="green")



def resize_canvas(event):
    """Redraws the image when the canvas is resized."""
    draw_running_guy_crossing_finish_line(canvas, runner_x_offset, has_crossed_finish_line)

def move_runner():
    """Moves the runner back and forth, then crosses the finish line."""
    global runner_x_offset, direction, has_crossed_finish_line, runner_speed

    if not has_crossed_finish_line:
        runner_x_offset += runner_speed * direction

        # Reverse direction if the runner hits the edge *before* the finish line
        runner_x_position = canvas.winfo_width() * 0.3 + runner_x_offset
        finish_line_x = canvas.winfo_width() * 0.8

        if runner_x_position < finish_line_x:  #Only check for direction reversal *before* crossing
            if runner_x_offset > max_offset:
                direction = -1
            elif runner_x_offset < min_offset:
                direction = 1
        # Move towards the finish line after reaching a certain point, regardless of direction
        else:
            direction = 1 # Ensure the runner moves right toward the finish line
            runner_speed = 5 #make the runner run faster
            if runner_x_position > canvas.winfo_width():
                has_crossed_finish_line = True



        # Check if the runner has crossed the finish line
        if runner_x_position > finish_line_x and runner_x_position <= canvas.winfo_width():
            # Continue moving the runner until they are off the screen

            pass #keep moving until it is off the screen
        elif runner_x_position > canvas.winfo_width():
            has_crossed_finish_line = True

        canvas.delete("all")  # Clear the canvas
        draw_running_guy_crossing_finish_line(canvas, runner_x_offset, has_crossed_finish_line)
    else:
        canvas.delete("all") #clear the canvas
        draw_running_guy_crossing_finish_line(canvas, runner_x_offset, has_crossed_finish_line)


    root.after(20, move_runner)  # Repeat every 20 milliseconds (adjust for speed)


# --- Create the main window ---
root = tk.Tk()
root.title("Running Guy GUI")

# --- Canvas setup ---
canvas_width = 800
canvas_height = 600
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack(fill="both", expand=True)

# --- Runner movement variables ---
runner_x_offset = 0  # Initial offset from the starting position
runner_speed = 2     # Adjust for faster/slower movement
direction = 1        # 1 for right, -1 for left
max_offset = 150    # Maximum offset to the right (increased for crossing)
min_offset = -100   # Maximum offset to the left
has_crossed_finish_line = False  # Flag to indicate if the runner crossed the line

# --- Initial draw and animation start ---
draw_running_guy_crossing_finish_line(canvas, runner_x_offset, has_crossed_finish_line)
move_runner() # Start the animation loop

# --- Bind resize event ---
canvas.bind("<Configure>", resize_canvas)


root.mainloop()