import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("400x600")
        self.resizable(0, 0)
        self.init_ui()

    def init_ui(self):
        layout = tk.Frame(self)
        layout.pack(padx=10, pady=10)
        
        # Input fields
        self.num1_entry = tk.Entry(layout, width=10)
        self.num2_entry = tk.Entry(layout, width=10)
        self.function_entry = tk.Entry(layout, width=10)
        self.result_entry = tk.Entry(layout, width=10)

        # Labels
        num1_label = tk.Label(layout, text="Number 1:")
        num2_label = tk.Label(layout, text="Number 2:")
        function_label = tk.Label(layout, text="Function:")
        
        # Buttons
        calculate_button = tk.Button(layout, text="Calculate", command=self.calculate)
        clear_button = tk.Button(layout, text="Clear", command=self.clear)
        exit_button = tk.Button(layout, text="Exit", command=self.destroy)

        # Layout arrangement
        num1_label.grid(row=0, column=0, padx=5, pady=5)
        self.num1_entry.grid(row=0, column=1, padx=5, pady=5)
        num2_label.grid(row=2, column=0, padx=5, pady=5)
        self.num2_entry.grid(row=2, column=1, padx=5, pady=5)
        function_label.grid(row=1, column=0, padx=5, pady=5)
        self.function_entry.grid(row=1, column=1, padx=5, pady=5)
        calculate_button.grid(row=3, column=0, columnspan=2, pady=10)
        clear_button.grid(row=4, column=0, columnspan=2, pady=10)
        exit_button.grid(row=5, column=0, columnspan=2, pady=10)

    def calculate(self):
        try:
            num1 = int(self.num1_entry.get())
            num2 = int(self.num2_entry.get())
            operation = self.function_entry.get()

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
            elif operation == "%":
                result = num1 % num2 if num2 != 0 else "Error: Division by zero"
            elif operation == "**":
                result = num1 ** num2
            elif operation == "//":
                result = num1 // num2 if num2 != 0 else "Error: Division by zero"
            elif operation == "sqrt":
                result = num1 ** 0.5 if num1 >= 0 else "Error: Invalid input"
            elif operation == "cbrt":
                result = num1 ** (1/3) if num1 >= 0 else "Error: Invalid input"
            else:
                result = "Invalid function symbol"
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
        except ValueError:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, "Error: Numeric input required")

    def clear(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.function_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()

