import tkinter as tk

def say_hello():
    print("Hello!")

root = tk.Tk()
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()
root.mainloop()
