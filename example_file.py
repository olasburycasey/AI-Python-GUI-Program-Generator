import tkinter as tk
from tkinter import messagebox

def generate_code_and_file():
    print("Generating code and file...")  # Replace with your logic
    save_file()

def save_file():
    print("Saving file...")  # Replace with your logic

def run_existing_path():
    print("Running existing program...")  # Replace with your logic

def give_feedback():
    print("Giving feedback...")  # Replace with your logic

def initiate_program(choice: str):
    if choice == "1":
        generate_code_and_file()
    elif choice == "2":
        run_existing_path()
    elif choice == "3":
        give_feedback()
    elif choice == "4":
        root.destroy()

def on_button_click(choice):
    initiate_program(choice)

# GUI Setup
root = tk.Tk()
root.title("LLM Program Launcher")
root.geometry("700x300")  # Wider window

label = tk.Label(root, text="Hello user. What would you like to do?", font=("Arial", 16))
label.pack(pady=20)

# Frame for the first three buttons side-by-side
button_frame = tk.Frame(root)
button_frame.pack(pady=10)

btn1 = tk.Button(button_frame, text="Create New Program", font=("Arial", 14), width=20, height=3, command=lambda: on_button_click("1"))
btn1.grid(row=0, column=0, padx=10, pady=10)

btn2 = tk.Button(button_frame, text="Run Existing Program", font=("Arial", 14), width=20, height=3, command=lambda: on_button_click("2"))
btn2.grid(row=0, column=1, padx=10, pady=10)

btn3 = tk.Button(button_frame, text="Give Feedback", font=("Arial", 14), width=20, height=3, command=lambda: on_button_click("3"))
btn3.grid(row=0, column=2, padx=10, pady=10)

# Quit button below
quit_button = tk.Button(root, text="Quit", font=("Arial", 14), width=15, height=2, command=lambda: on_button_click("4"))
quit_button.pack(pady=20)

root.mainloop()
