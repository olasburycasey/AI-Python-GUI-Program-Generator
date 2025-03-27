import tkinter as tk
from tkinter import Canvas

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator")

        self.expression = ""  # Store the current expression
        self.result = None  # Store the result after calculation

        # Create a canvas
        self.canvas_width = 400
        self.canvas_height = 500
        self.canvas = Canvas(master, width=self.canvas_width, height=self.canvas_height, bg="white")
        self.canvas.pack()

        self.draw_calculator(50, 50, 300, 400)  # Adjust position and size as needed

    def draw_calculator(self, x, y, width, height):
        """Draws a calculator on the canvas."""

        # Calculator body
        self.canvas.create_rectangle(x, y, x + width, y + height, fill="#E0E0E0", outline="black")

        # Screen area
        screen_x = x + width * 0.1
        screen_y = y + height * 0.1
        screen_width = width * 0.8
        screen_height = height * 0.2
        self.screen_x = screen_x
        self.screen_y = screen_y
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.canvas.create_rectangle(screen_x, screen_y, screen_x + screen_width, screen_y + screen_height, fill="white", outline="black")

        # Display text (initially empty)
        self.display_text = self.canvas.create_text(screen_x + screen_width * 0.95, screen_y + screen_height * 0.5,
                                           text="", anchor="e", font=("Arial", int(screen_height * 0.4)))

        # Buttons
        button_width = width * 0.2
        button_height = height * 0.15
        button_x_start = x + width * 0.1
        button_y_start = screen_y + screen_height + height * 0.1

        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+",
            "C" # Add clear button
        ]

        self.button_rects = []  # Store rectangle IDs for click detection
        button_index = 0
        for row in range(4):
            for col in range(4):
                button_x = button_x_start + col * button_width
                button_y = button_y_start + row * button_height
                button_text = buttons[button_index]

                rect_id = self.canvas.create_rectangle(button_x, button_y, button_x + button_width, button_y + button_height,
                                       fill="#D0D0D0", outline="black", tags=button_text)
                self.button_rects.append(rect_id)
                self.canvas.create_text(button_x + button_width * 0.5, button_y + button_height * 0.5,
                                   text=button_text, anchor="center", font=("Arial", int(button_height * 0.5)))
                button_index += 1

        #Add the clear button separately because of the layout changes
        button_x = button_x_start
        button_y = button_y_start + 4 * button_height
        button_text = buttons[16]

        rect_id = self.canvas.create_rectangle(button_x, button_y, button_x + button_width, button_y + button_height,
                                    fill="#D0D0D0", outline="black", tags=button_text)
        self.button_rects.append(rect_id)
        self.canvas.create_text(button_x + button_width * 0.5, button_y + button_height * 0.5,
                           text=button_text, anchor="center", font=("Arial", int(button_height * 0.5)))



        # Bind mouse click to canvas
        self.canvas.bind("<Button-1>", self.on_click)


    def on_click(self, event):
        """Handles mouse clicks on the canvas."""
        x = event.x
        y = event.y

        # Find the clicked button
        for rect_id in self.button_rects:
            bbox = self.canvas.bbox(rect_id)  # (x1, y1, x2, y2)
            if bbox[0] <= x <= bbox[2] and bbox[1] <= y <= bbox[3]:
                tags = self.canvas.gettags(rect_id)
                button_text = tags[0]  # The text is the tag

                self.button_pressed(button_text)
                break

    def button_pressed(self, button_text):
        """Handles the action when a button is pressed."""
        if button_text == "=":
            try:
                self.result = eval(self.expression)
                self.update_display(str(self.result))  # Update display with result
                self.expression = str(self.result)  # Store result as the current expression
            except Exception as e:
                self.update_display("Error")
                self.expression = ""
                self.result = None


        elif button_text == "C": #Clear
            self.expression = ""
            self.result = None
            self.update_display("")  # Clear the display

        else:
            self.expression += button_text
            self.update_display(self.expression) #Update the expression

    def update_display(self, text):
        """Updates the text displayed on the calculator screen."""
        self.canvas.itemconfig(self.display_text, text=text)




# Create the main window
root = tk.Tk()
calculator = Calculator(root)

# Run the main loop
root.mainloop()
