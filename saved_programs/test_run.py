from gui_features import write_code_to_file

code_string = '''
import tkinter as tk

def say_hello():
    print("Hello!")

root = tk.Tk()
button = tk.Button(root, text="Click Me", command=say_hello)
button.pack()
root.mainloop()
'''.lstrip()

write_code_to_file("example_gui.py", code_string)
