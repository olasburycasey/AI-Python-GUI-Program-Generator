import tkinter as tk
from tkinter import Canvas
import random

def draw_usa_map(canvas, width, height):
    """Draws a simplified map of the USA on the canvas."""

    # Simplified coordinates for state shapes (replace with more accurate data if needed)
    # These are extremely basic and illustrative. You'd need a shapefile or similar for accurate boundaries.
    states = {
        "WA": {"coords": [(0.1, 0.1), (0.2, 0.15), (0.2, 0.25), (0.1, 0.2)], "color": "lightgreen"},
        "OR": {"coords": [(0.1, 0.2), (0.2, 0.25), (0.2, 0.35), (0.1, 0.3)], "color": "lightgreen"},
        "CA": {"coords": [(0.1, 0.3), (0.2, 0.35), (0.2, 0.6), (0.1, 0.5)], "color": "lightyellow"},
        "ID": {"coords": [(0.2, 0.15), (0.3, 0.2), (0.3, 0.3), (0.2, 0.25)], "color": "lightblue"},
        "NV": {"coords": [(0.2, 0.35), (0.3, 0.4), (0.3, 0.5), (0.2, 0.6)], "color": "lightyellow"},
        "UT": {"coords": [(0.3, 0.3), (0.4, 0.35), (0.4, 0.5), (0.3, 0.4)], "color": "lightblue"},
        "AZ": {"coords": [(0.3, 0.4), (0.4, 0.5), (0.4, 0.6), (0.3, 0.5)], "color": "lightyellow"},
        "MT": {"coords": [(0.2, 0.1), (0.3, 0.15), (0.3, 0.2), (0.2, 0.15)], "color": "lightgreen"},
        "WY": {"coords": [(0.3, 0.2), (0.4, 0.25), (0.4, 0.35), (0.3, 0.3)], "color": "lightblue"},
        "CO": {"coords": [(0.4, 0.35), (0.5, 0.4), (0.5, 0.5), (0.4, 0.5)], "color": "lightblue"},
        "NM": {"coords": [(0.4, 0.5), (0.5, 0.55), (0.5, 0.6), (0.4, 0.6)], "color": "lightyellow"},
        "ND": {"coords": [(0.3, 0.1), (0.4, 0.15), (0.4, 0.2), (0.3, 0.15)], "color": "lightgreen"},
        "SD": {"coords": [(0.4, 0.15), (0.5, 0.2), (0.5, 0.3), (0.4, 0.25)], "color": "lightgreen"},
        "NE": {"coords": [(0.5, 0.2), (0.6, 0.25), (0.6, 0.35), (0.5, 0.3)], "color": "lightyellow"},
        "KS": {"coords": [(0.5, 0.3), (0.6, 0.35), (0.6, 0.5), (0.5, 0.4)], "color": "lightyellow"},
        "OK": {"coords": [(0.5, 0.4), (0.6, 0.45), (0.6, 0.6), (0.5, 0.5)], "color": "lightyellow"},
        "TX": {"coords": [(0.5, 0.5), (0.7, 0.6), (0.7, 0.7), (0.5, 0.6)], "color": "lightyellow"},
        "MN": {"coords": [(0.4, 0.05), (0.5, 0.1), (0.5, 0.2), (0.4, 0.1)], "color": "lightgreen"},
        "IA": {"coords": [(0.5, 0.2), (0.6, 0.2), (0.6, 0.3), (0.5, 0.25)], "color": "lightyellow"},
        "MO": {"coords": [(0.6, 0.3), (0.7, 0.35), (0.7, 0.5), (0.6, 0.4)], "color": "lightyellow"},
        "AR": {"coords": [(0.6, 0.45), (0.7, 0.5), (0.7, 0.6), (0.6, 0.55)], "color": "lightyellow"},
        "LA": {"coords": [(0.6, 0.6), (0.7, 0.65), (0.7, 0.7), (0.6, 0.65)], "color": "lightyellow"},
        "WI": {"coords": [(0.5, 0.05), (0.6, 0.1), (0.6, 0.2), (0.5, 0.1)], "color": "lightgreen"},
        "IL": {"coords": [(0.6, 0.25), (0.7, 0.3), (0.7, 0.4), (0.6, 0.3)], "color": "lightyellow"},
        "TN": {"coords": [(0.7, 0.4), (0.8, 0.45), (0.8, 0.55), (0.7, 0.5)], "color": "lightyellow"},
        "MS": {"coords": [(0.7, 0.55), (0.8, 0.6), (0.8, 0.7), (0.7, 0.6)], "color": "lightyellow"},
        "MI": {"coords": [(0.6, 0.05), (0.7, 0.1), (0.7, 0.2), (0.6, 0.15)], "color": "lightgreen"},
        "IN": {"coords": [(0.7, 0.3), (0.8, 0.35), (0.8, 0.45), (0.7, 0.4)], "color": "lightyellow"},
        "KY": {"coords": [(0.7, 0.4), (0.8, 0.4), (0.8, 0.5), (0.7, 0.45)], "color": "lightyellow"},
        "AL": {"coords": [(0.8, 0.6), (0.9, 0.65), (0.9, 0.7), (0.8, 0.65)], "color": "lightyellow"},
        "OH": {"coords": [(0.7, 0.2), (0.8, 0.3), (0.8, 0.4), (0.7, 0.3)], "color": "lightyellow"},
        "WV": {"coords": [(0.8, 0.3), (0.9, 0.35), (0.9, 0.45), (0.8, 0.4)], "color": "lightyellow"},
        "GA": {"coords": [(0.9, 0.6), (1.0, 0.65), (1.0, 0.7), (0.9, 0.65)], "color": "lightyellow"},
        "PA": {"coords": [(0.8, 0.1), (0.9, 0.3), (0.9, 0.4), (0.8, 0.3)], "color": "lightyellow"},
        "VA": {"coords": [(0.9, 0.4), (1.0, 0.45), (1.0, 0.55), (0.9, 0.5)], "color": "lightyellow"},
        "NC": {"coords": [(0.9, 0.5), (1.0, 0.55), (1.0, 0.65), (0.9, 0.6)], "color": "lightyellow"},
        "SC": {"coords": [(0.9, 0.6), (1.0, 0.6), (1.0, 0.7), (0.9, 0.65)], "color": "lightyellow"},
        "NY": {"coords": [(0.8, 0.1), (0.9, 0.2), (0.9, 0.4), (0.8, 0.2)], "color": "lightyellow"},
        "VT": {"coords": [(0.9, 0.1), (1.0, 0.2), (0.9, 0.25)], "color": "lightyellow"},
        "NH": {"coords": [(0.9, 0.15), (1.0, 0.25), (0.9, 0.3)], "color": "lightyellow"},
        "ME": {"coords": [(0.9, 0.05), (1.0, 0.1), (1.0, 0.2), (0.9, 0.1)], "color": "lightyellow"},
        "MA": {"coords": [(0.9, 0.2), (1.0, 0.3), (0.9, 0.3)], "color": "lightyellow"},
        "CT": {"coords": [(0.9, 0.3), (1.0, 0.35), (0.9, 0.35)], "color": "lightyellow"},
        "RI": {"coords": [(0.9, 0.35), (1.0, 0.4), (0.9, 0.4)], "color": "lightyellow"},
        "NJ": {"coords": [(0.8, 0.3), (0.9, 0.35), (0.8, 0.4)], "color": "lightyellow"},
        "DE": {"coords": [(0.8, 0.35), (0.9, 0.4), (0.8, 0.45)], "color": "lightyellow"},
        "MD": {"coords": [(0.9, 0.4), (1.0, 0.45), (0.9, 0.5)], "color": "lightyellow"},
        "FL": {"coords": [(0.9, 0.7), (1.0, 0.75), (1.0, 0.9), (0.9, 0.8)], "color": "lightyellow"},
        # Add Alaska and Hawaii
        "AK": {"coords": [(0.1, 0.7), (0.3, 0.7), (0.3, 0.9), (0.1, 0.9)], "color": "lightblue"}, # Positioned to the left, scaled down
        "HI": {"coords": [(0.8, 0.8), (0.9, 8.5), (0.9, 0.9), (0.8, 0.9)], "color": "lightyellow"}  # Positioned to the right, scaled down
    }


    # Draw the states
    for state, data in states.items():
        coords = data["coords"]
        color = data["color"]
        scaled_coords = [(x * width, y * height) for x, y in coords] # Scale coordinates to canvas size
        canvas.create_polygon(scaled_coords, fill=color, outline="black")

        # Add state abbreviation (optional)
        center_x = sum(x for x, y in scaled_coords) / len(scaled_coords)
        center_y = sum(y for x, y in scaled_coords) / len(scaled_coords)
        canvas.create_text(center_x, center_y, text=state, fill="black")  # Add state labels


    # Optional: Add a title
    canvas.create_text(width/2, 20, text="A VERY Simplified Map of the USA", font=("Arial", 16, "bold"))



def main():
    """Creates the Tkinter window and draws the map."""

    window = tk.Tk()
    window.title("USA Map")

    width = 800
    height = 600
    canvas = Canvas(window, width=width, height=height, bg="white") # Set background color
    canvas.pack()

    draw_usa_map(canvas, width, height)

    window.mainloop()

if __name__ == "__main__":
    main()
