import tkinter as tk
from tkinter import Canvas

def draw_pencil_face(canvas, x, y, size=50):
    """Draws a pencil with a face on the given canvas."""

    # Pencil Body (Rectangular part)
    body_width = size * 0.2
    body_height = size * 0.8
    canvas.create_rectangle(x - body_width / 2, y - body_height / 2,
                             x + body_width / 2, y + body_height / 2,
                             fill="yellow", outline="black")

    # Pencil Tip (Triangle)
    tip_height = size * 0.2
    canvas.create_polygon(x - body_width / 2, y - body_height / 2 - tip_height,
                             x + body_width / 2, y - body_height / 2 - tip_height,
                             x, y - body_height / 2 - tip_height * 2,
                             fill="black", outline="black")

    # Eraser (Circle/Oval)
    eraser_radius_x = body_width / 2
    eraser_radius_y = tip_height / 2  # Slightly oval for effect
    canvas.create_oval(x - eraser_radius_x, y + body_height / 2 - eraser_radius_y,
                       x + eraser_radius_x, y + body_height / 2 + eraser_radius_y,
                       fill="pink", outline="black")

    # Face (Oval)  - Centered on the pencil body
    face_size = body_width * 0.8  # Smaller than the body width
    canvas.create_oval(x - face_size / 2, y - face_size / 2,
                       x + face_size / 2, y + face_size / 2,
                       fill="white", outline="black")

    # Eyes (Small circles)
    eye_offset_x = face_size * 0.2
    eye_offset_y = face_size * 0.2
    eye_size = face_size * 0.15
    canvas.create_oval(x - eye_offset_x - eye_size / 2, y - eye_offset_y - eye_size / 2,
                       x - eye_offset_x + eye_size / 2, y - eye_offset_y + eye_size / 2,
                       fill="black")
    canvas.create_oval(x + eye_offset_x - eye_size / 2, y - eye_offset_y - eye_size / 2,
                       x + eye_offset_x + eye_size / 2, y - eye_offset_y + eye_size / 2,
                       fill="black")

    # Mouth (Simple arc)
    mouth_width = face_size * 0.6
    mouth_height = face_size * 0.3
    canvas.create_arc(x - mouth_width / 2, y,
                      x + mouth_width / 2, y + mouth_height,
                      start=180, extent=180, style=tk.ARC, outline="black")


# Create the main window
root = tk.Tk()
root.title("Pencil Face GUI")

# Create a canvas to draw on
canvas_width = 300
canvas_height = 300
canvas = Canvas(root, width=canvas_width, height=canvas_height, bg="white")
canvas.pack()

# Draw the pencil face (centered)
pencil_x = canvas_width / 2
pencil_y = canvas_height / 2
pencil_size = 100 # Adjust size as needed
draw_pencil_face(canvas, pencil_x, pencil_y, pencil_size)

# Start the Tkinter event loop
root.mainloop()