import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk  # Requires Pillow library


def draw_desk(draw, width, height, desk_color):
    """Draws the desk rectangle."""
    draw.rectangle([(0, height * 0.75), (width, height)], fill=desk_color)


def draw_paper(draw, width, height, paper_color="white", outline_color="black"):
    """Draws the paper with lines."""
    paper_width = width * 0.6
    paper_height = height * 0.5
    paper_x = width * 0.2
    paper_y = height * 0.2

    draw.rectangle([(paper_x, paper_y), (paper_x + paper_width, paper_y + paper_height)], fill=paper_color, outline=outline_color)

    # Draw lines on the paper
    line_spacing = paper_height / 6
    line_start_x = paper_x + 10
    for i in range(4):
        line_y = paper_y + line_spacing * (i + 1)
        draw.line([(line_start_x, line_y), (paper_x + paper_width - 10, line_y)], fill="black", width=2)

    # Add messy lines on top
    draw.line([(paper_x + 20, paper_y + 10), (paper_x + 50, paper_y + 10)], fill="black", width=2)
    draw.line([(paper_x + paper_width - 50, paper_y + 20), (paper_x + paper_width - 20, paper_y + 20)], fill="black", width=2)


def draw_pen(draw, width, height, pen_color="blue"):
    """Draws the pen on the desk."""
    paper_width = width * 0.6
    paper_height = height * 0.5
    paper_x = width * 0.2
    paper_y = height * 0.2
    pen_length = width * 0.15
    pen_start_x = paper_x + paper_width + 10
    pen_start_y = paper_y + paper_height / 2
    draw.line([(pen_start_x, pen_start_y), (pen_start_x + pen_length, pen_start_y)], fill=pen_color, width=5)


def draw_exam_study_guide(width=400, height=300, background_color="lightgray", desk_color=(139, 69, 19)):
    """Draws the exam study guide image using PIL."""

    try:
        with Image.new("RGB", (width, height), background_color) as image:
            draw = ImageDraw.Draw(image)

            draw_desk(draw, width, height, desk_color)
            draw_paper(draw, width, height)
            draw_pen(draw, width, height)  # Optional: Add pen

            return image

    except Exception as e:  # Catch a more generic error here if necessary, but specific errors handled above.
        print(f"Error drawing image: {e}")
        return None  # Or return a default image/error image


def main():
    """Creates the Tkinter GUI window and displays the image."""
    root = tk.Tk()
    root.title("Exam Study Guide")

    image = draw_exam_study_guide()

    if image:  # Only proceed if image creation was successful
        try:
            photo = ImageTk.PhotoImage(image)  # Convert PIL image to Tkinter PhotoImage

            label = tk.Label(root, image=photo)
            label.image = photo  # Keep a reference to the image to prevent garbage collection
            label.pack(padx=10, pady=10)

        except Exception as e:  # More general UI exception
            print(f"Error displaying image: {e}")
            error_label = tk.Label(root, text=f"Error displaying image: {e}")
            error_label.pack()

    else:
        error_label = tk.Label(root, text="Failed to generate the study guide image.")
        error_label.pack()

    root.mainloop()


if __name__ == "__main__":
    main()