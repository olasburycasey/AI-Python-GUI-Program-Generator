import tkinter as tk
import math

class ScientificCalculator:
    def __init__(self, master):
        self.master = master
        master.title("Scientific Calculator")

        self.expression = ""
        self.entry_value = tk.StringVar()

        # Entry field
        self.entry = tk.Entry(master, textvariable=self.entry_value, font=('Arial', 20), bd=5, insertwidth=4, bg="white", justify='right')
        self.entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10, sticky="nsew") # Use sticky for resizing

        # Buttons
        button_config = {'padx': 10, 'pady': 10, 'font': ('Arial', 14)}

        # Row 1
        self.button_clear = tk.Button(master, text="C", width=5, command=self.clear, **button_config, bg="#FFCCCC")
        self.button_clear.grid(row=1, column=0)

        self.button_backspace = tk.Button(master, text="←", width=5, command=self.backspace, **button_config, bg="#FFCCCC")
        self.button_backspace.grid(row=1, column=1)

        self.button_percent = tk.Button(master, text="%", width=5, command=lambda: self.append_to_expression("%"), **button_config)
        self.button_percent.grid(row=1, column=2)

        self.button_divide = tk.Button(master, text="/", width=5, command=lambda: self.append_to_expression("/"), **button_config)
        self.button_divide.grid(row=1, column=3)

        self.button_sin = tk.Button(master, text="sin", width=5, command=lambda: self.append_to_expression("sin("), **button_config)
        self.button_sin.grid(row=1, column=4)

        self.button_cos = tk.Button(master, text="cos", width=5, command=lambda: self.append_to_expression("cos("), **button_config)
        self.button_cos.grid(row=1, column=5)

        # Row 2
        self.button_7 = tk.Button(master, text="7", width=5, command=lambda: self.append_to_expression("7"), **button_config)
        self.button_7.grid(row=2, column=0)

        self.button_8 = tk.Button(master, text="8", width=5, command=lambda: self.append_to_expression("8"), **button_config)
        self.button_8.grid(row=2, column=1)

        self.button_9 = tk.Button(master, text="9", width=5, command=lambda: self.append_to_expression("9"), **button_config)
        self.button_9.grid(row=2, column=2)

        self.button_multiply = tk.Button(master, text="*", width=5, command=lambda: self.append_to_expression("*"), **button_config)
        self.button_multiply.grid(row=2, column=3)

        self.button_tan = tk.Button(master, text="tan", width=5, command=lambda: self.append_to_expression("tan("), **button_config)
        self.button_tan.grid(row=2, column=4)

        self.button_sqrt = tk.Button(master, text="√", width=5, command=lambda: self.append_to_expression("sqrt("), **button_config)
        self.button_sqrt.grid(row=2, column=5)

        # Row 3
        self.button_4 = tk.Button(master, text="4", width=5, command=lambda: self.append_to_expression("4"), **button_config)
        self.button_4.grid(row=3, column=0)

        self.button_5 = tk.Button(master, text="5", width=5, command=lambda: self.append_to_expression("5"), **button_config)
        self.button_5.grid(row=3, column=1)

        self.button_6 = tk.Button(master, text="6", width=5, command=lambda: self.append_to_expression("6"), **button_config)
        self.button_6.grid(row=3, column=2)

        self.button_minus = tk.Button(master, text="-", width=5, command=lambda: self.append_to_expression("-"), **button_config)
        self.button_minus.grid(row=3, column=3)

        self.button_log = tk.Button(master, text="log", width=5, command=lambda: self.append_to_expression("log10("), **button_config)
        self.button_log.grid(row=3, column=4)

        self.button_ln = tk.Button(master, text="ln", width=5, command=lambda: self.append_to_expression("log("), **button_config) #Natural log
        self.button_ln.grid(row=3, column=5)

        # Row 4
        self.button_1 = tk.Button(master, text="1", width=5, command=lambda: self.append_to_expression("1"), **button_config)
        self.button_1.grid(row=4, column=0)

        self.button_2 = tk.Button(master, text="2", width=5, command=lambda: self.append_to_expression("2"), **button_config)
        self.button_2.grid(row=4, column=1)

        self.button_3 = tk.Button(master, text="3", width=5, command=lambda: self.append_to_expression("3"), **button_config)
        self.button_3.grid(row=4, column=2)

        self.button_plus = tk.Button(master, text="+", width=5, command=lambda: self.append_to_expression("+"), **button_config)
        self.button_plus.grid(row=4, column=3)

        self.button_pi = tk.Button(master, text="π", width=5, command=lambda: self.append_to_expression(str(math.pi)), **button_config)
        self.button_pi.grid(row=4, column=4)

        self.button_e = tk.Button(master, text="e", width=5, command=lambda: self.append_to_expression(str(math.e)), **button_config)
        self.button_e.grid(row=4, column=5)

        # Row 5
        self.button_0 = tk.Button(master, text="0", width=5, command=lambda: self.append_to_expression("0"), **button_config)
        self.button_0.grid(row=5, column=0)

        self.button_decimal = tk.Button(master, text=".", width=5, command=lambda: self.append_to_expression("."), **button_config)
        self.button_decimal.grid(row=5, column=1)

        self.button_power = tk.Button(master, text="^", width=5, command=lambda: self.append_to_expression("**"), **button_config)
        self.button_power.grid(row=5, column=2)

        self.button_equal = tk.Button(master, text="=", width=5, command=self.evaluate, **button_config, bg="#90EE90")
        self.button_equal.grid(row=5, column=3)

        self.button_open_paren = tk.Button(master, text="(", width=5, command=lambda: self.append_to_expression("("), **button_config)
        self.button_open_paren.grid(row=5, column=4)

        self.button_close_paren = tk.Button(master, text=")", width=5, command=lambda: self.append_to_expression(")"), **button_config)
        self.button_close_paren.grid(row=5, column=5)

        # Configure grid weights to allow resizing
        for i in range(6):
            master.grid_columnconfigure(i, weight=1)
            master.grid_rowconfigure(i, weight=1)


    def append_to_expression(self, char):
        self.expression += char
        self.entry_value.set(self.expression)

    def clear(self):
        self.expression = ""
        self.entry_value.set("")

    def backspace(self):
        self.expression = self.expression[:-1]
        self.entry_value.set(self.expression)

    def evaluate(self):
        try:
            # **Important security note:**  Using eval() is inherently risky, *especially* if the
            # expression comes from an untrusted source (e.g., user input from a website).  It can allow
            # arbitrary code execution.  A safer alternative would be to use the `ast.literal_eval`
            # function, or a dedicated math expression parser library.  However, for this self-contained
            # example, I am using eval() with input validation to minimize the risk.

            # Input validation:  Allow only digits, operators, parentheses, '.', 'pi', 'e', 'sin', 'cos', 'tan', 'log', 'sqrt'
            allowed_chars = "0123456789+-*/().%^pisincostanlogqrt e"
            # Clean up the expression to remove spaces and make it easier to validate
            cleaned_expression = "".join(c for c in self.expression.lower() if c in allowed_chars)

            if any(c not in allowed_chars for c in self.expression.lower()):
               raise ValueError("Invalid character in expression")


            #Replace pi and e for safe eval
            safe_expression = cleaned_expression.replace("pi", str(math.pi)).replace("e", str(math.e))

            # Evaluate using safe expression
            result = eval(safe_expression, {"__builtins__": None}, {
                'math': math,
                'sin': math.sin,
                'cos': math.cos,
                'tan': math.tan,
                'log': math.log,  # Natural logarithm (base e)
                'log10': math.log10, # Base 10 logarithm
                'sqrt': math.sqrt,
                'pi': math.pi,
                'e': math.e,

            })
            self.expression = str(result)
            self.entry_value.set(self.expression)

        except (SyntaxError, TypeError, ZeroDivisionError, ValueError) as e:
            self.entry_value.set("Error")
            self.expression = ""  # Reset expression after error
        except Exception as e:  #Catch any other unexpected exceptions
            self.entry_value.set("Error")
            self.expression = ""


root = tk.Tk()
calculator = ScientificCalculator(root)
root.mainloop()