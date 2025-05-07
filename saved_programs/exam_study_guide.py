import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageDraw, ImageTk  # Requires Pillow library


def draw_exam_study_guide():
    """Draws the exam study guide image using PIL."""

    width = 400
    height = 300

    try:
        image = Image.new("RGB", (width, height), "lightgray")  # Background color
        draw = ImageDraw.Draw(image)

        # Draw the desk
        desk_color = (139, 69, 19)  # Brown
        draw.rectangle([(0, height * 0.75), (width, height)], fill=desk_color)

        # Draw the paper
        paper_width = width * 0.6
        paper_height = height * 0.5
        paper_x = width * 0.2
        paper_y = height * 0.2

        draw.rectangle([(paper_x, paper_y), (paper_x + paper_width, paper_y + paper_height)], fill="white", outline="black")

        # Draw some lines on the paper to represent text
        line_spacing = paper_height / 6
        line_start_x = paper_x + 10
        for i in range(4):
            line_y = paper_y + line_spacing * (i + 1)
            draw.line([(line_start_x, line_y), (paper_x + paper_width - 10, line_y)], fill="black", width=2)
            # Add a few random short lines on the top to look messy
        draw.line([(paper_x + 20, paper_y + 10), (paper_x + 50, paper_y + 10)], fill="black", width=2)
        draw.line([(paper_x + paper_width - 50, paper_y + 20), (paper_x + paper_width - 20, paper_y + 20)], fill="black", width=2)


        # Draw a pen on the desk next to the paper (optional)
        pen_length = width * 0.15
        pen_start_x = paper_x + paper_width + 10
        pen_start_y = paper_y + paper_height / 2
        draw.line([(pen_start_x, pen_start_y), (pen_start_x + pen_length, pen_start_y)], fill="blue", width=5)

        return image
    except Exception as e:
        print(f"Error drawing image: {e}")
        return None  # Or return a default image/error image


def main():
    """Creates the Tkinter GUI window and displays the image."""
    root = tk.Tk()
    root.title("Exam Study Guide")

    image = draw_exam_study_guide()

    if image: # Only proceed if image creation was successful
        try:
            photo = ImageTk.PhotoImage(image)  # Convert PIL image to Tkinter PhotoImage

            label = tk.Label(root, image=photo)
            label.image = photo  # Keep a reference to the image to prevent garbage collection
            label.pack(padx=10, pady=10)

        except Exception as e:
            print(f"Error displaying image: {e}")
            error_label = tk.Label(root, text=f"Error displaying image: {e}")
            error_label.pack()

    else:
        error_label = tk.Label(root, text="Failed to generate the study guide image.")
        error_label.pack()



    root.mainloop()


if __name__ == "__main__":
    main()