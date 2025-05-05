import tkinter as tk
from tkinter import Canvas

class GraduationEmoji(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Graduation Emoji")
        self.geometry("300x300")  # Adjust size as needed
        self.resizable(False, False) # Disable resizing

        self.canvas = Canvas(self, width=300, height=300, bg="white")
        self.canvas.pack(pady=20)

        self.draw_graduation_emoji()


    def draw_graduation_emoji(self):
        """Draws a graduation cap and face on the canvas."""

        # --- Face ---
        face_x = 150
        face_y = 150
        face_radius = 70
        self.canvas.create_oval(face_x - face_radius, face_y - face_radius,
                                face_x + face_radius, face_y + face_radius,
                                fill="#FFDA63", outline="black") # Yellowish face

        # --- Eyes ---
        eye_offset_x = 25
        eye_offset_y = 20
        eye_radius = 8
        self.canvas.create_oval(face_x - eye_offset_x - eye_radius, face_y - eye_offset_y - eye_radius,
                                face_x - eye_offset_x + eye_radius, face_y - eye_offset_y + eye_radius,
                                fill="black")
        self.canvas.create_oval(face_x + eye_offset_x - eye_radius, face_y - eye_offset_y - eye_radius,
                                face_x + eye_offset_x + eye_radius, face_y - eye_offset_y + eye_radius,
                                fill="black")

        # --- Mouth ---
        mouth_start_x = face_x - 30
        mouth_start_y = face_y + 30
        mouth_end_x = face_x + 30
        mouth_end_y = face_y + 30
        self.canvas.create_arc(mouth_start_x, mouth_start_y - 20, mouth_end_x, mouth_end_y + 10,
                                start=180, extent=180, style=tk.ARC, width=2, outline="red") # Red mouth

        # --- Nose ---
        nose_x = face_x
        nose_y = face_y + 10
        nose_width = 10
        nose_height = 15
        self.canvas.create_oval(nose_x - nose_width / 2, nose_y - nose_height / 2,
                                nose_x + nose_width / 2, nose_y + nose_height / 2,
                                fill="black", outline="black")  # Black nose

        # --- Ears ---
        ear_offset_x = face_radius - 5
        ear_offset_y = 10
        ear_width = 10
        ear_height = 20
        self.canvas.create_oval(face_x - ear_offset_x - ear_width / 2, face_y - ear_offset_y - ear_height / 2,
                                face_x - ear_offset_x + ear_width / 2, face_y - ear_offset_y + ear_height / 2,
                                fill="#FFDA63", outline="black")  # Match face color

        self.canvas.create_oval(face_x + ear_offset_x - ear_width / 2, face_y - ear_offset_y - ear_height / 2,
                                face_x + ear_offset_x + ear_width / 2, face_y - ear_offset_y + ear_height / 2,
                                fill="#FFDA63", outline="black")  # Match face color


        # --- Graduation Cap ---
        cap_width = 120
        cap_height = 40
        cap_x = face_x - cap_width / 2
        cap_y = face_y - face_radius - cap_height
        self.canvas.create_rectangle(cap_x, cap_y, cap_x + cap_width, cap_y + cap_height,
                                     fill="blue", outline="black") # Blue cap

        # --- Cap Top (Square) ---
        top_size = cap_width * 0.8
        top_x = face_x - top_size / 2
        top_y = cap_y - top_size / 3  # Slightly overlap the rectangle below
        self.canvas.create_rectangle(top_x, top_y, top_x + top_size, top_y + top_size * (2/3),
                                     fill="blue", outline="black") #Blue cap


        # --- Tassel ---
        tassel_length = 40
        tassel_x = top_x + top_size * 0.75
        tassel_y = top_y + top_size * (2/3)
        self.canvas.create_line(tassel_x, tassel_y, tassel_x, tassel_y + tassel_length,
                                width=2, fill="red")  # Red tassel
        self.canvas.create_oval(tassel_x -3, tassel_y + tassel_length - 3, tassel_x+3, tassel_y + tassel_length +3, fill = "red", outline="red")


if __name__ == "__main__":
    app = GraduationEmoji()
    app.mainloop()