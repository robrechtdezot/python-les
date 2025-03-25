import tkinter as tk

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("200x300")
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
        number_1 = tk.Button(layout, text="1", command=lambda: self.click_number(1))
        number_2 = tk.Button(layout, text="2", command=lambda: self.click_number(2))
        number_3 = tk.Button(layout, text="3", command=lambda: self.click_number(3))
        number_4 = tk.Button(layout, text="4", command=lambda: self.click_number(4))
        number_5 = tk.Button(layout, text="5", command=lambda: self.click_number(5))
        number_6 = tk.Button(layout, text="6", command=lambda: self.click_number(6))
        number_7 = tk.Button(layout, text="7", command=lambda: self.click_number(7))
        number_8 = tk.Button(layout, text="8", command=lambda: self.click_number(8))
        number_9 = tk.Button(layout, text="9", command=lambda: self.click_number(9))
        number_0 = tk.Button(layout, text="0", command=lambda: self.click_number(0))
        plus = tk.Button(layout, text="+", command=lambda: self.click_function("+"))
        minus = tk.Button(layout, text="-", command=lambda: self.click_function("-"))
        multiply = tk.Button(layout, text="*", command=lambda: self.click_function("*"))
        divide = tk.Button(layout, text="/", command=lambda: self.click_function("/"))
        modulo = tk.Button(layout, text="%", command=lambda: self.click_function("%"))
        power = tk.Button(layout, text="**", command=lambda: self.click_function("**"))
        floor_division = tk.Button(layout, text="//", command=lambda: self.click_function("//"))
        square_root = tk.Button(layout, text="sqrt", command=lambda: self.click_function("sqrt"))
        cube_root = tk.Button(layout, text="cbrt", command=lambda: self.click_function("cbrt"))
        
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

        number_1.grid(row=6, column=0, padx=5, pady=5)
        number_2.grid(row=6, column=1, padx=5, pady=5)
        number_3.grid(row=6, column=2, padx=5, pady=5)
        number_4.grid(row=7, column=0, padx=5, pady=5)
        number_5.grid(row=7, column=1, padx=5, pady=5)
        number_6.grid(row=7, column=2, padx=5, pady=5)
        number_7.grid(row=8, column=0, padx=5, pady=5)
        number_8.grid(row=8, column=1, padx=5, pady=5)
        number_9.grid(row=8, column=2, padx=5, pady=5)
        number_0.grid(row=9, column=0, padx=5, pady=5)
        plus.grid(row=9, column=1, padx=5, pady=5)
        minus.grid(row=9, column=2, padx=5, pady=5)
        multiply.grid(row=10, column=0, padx=5, pady=5)
        divide.grid(row=10, column=1, padx=5, pady=5)
        modulo.grid(row=10, column=2, padx=5, pady=5)
        power.grid(row=11, column=0, padx=5, pady=5)
        floor_division.grid(row=11, column=1, padx=5, pady=5)
        square_root.grid(row=11, column=2, padx=5, pady=5)
        cube_root.grid(row=12, column=0, padx=5, pady=5)

        # History list
        self.history_list = tk.Listbox(layout, height=10, width=30)
        self.history_list.grid(row=13, column=0, columnspan=3, padx=5, pady=5)

    def calculate(self):
        try:
            num1 = int(self.num1_entry.get() or 0)
            num2 = int(self.num2_entry.get() or 0)
            operation = self.function_entry.get()

            if not operation:
                raise ValueError("No operation selected")

            if operation == "+":
                result = num1 + num2
            elif operation == "-":
                result = num1 - num2
            elif operation == "*":
                result = num1 * num2
            elif operation == "/":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            elif operation == "%":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 % num2
            elif operation == "**":
                result = num1 ** num2
            elif operation == "//":
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 // num2
            elif operation == "sqrt":
                if num1 < 0:
                    raise ValueError
                result = num1 ** 0.5
            elif operation == "cbrt":
                if num1 < 0:
                    raise ValueError
                result = num1 ** (1/3)
            else:
                raise ValueError("Invalid function symbol")

            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, str(result))
        except (ValueError, ZeroDivisionError) as e:
            self.result_entry.delete(0, tk.END)
            self.result_entry.insert(0, f"Error: {e}")
            
        self.result_entry.grid(row=12, column=1, columnspan=2, padx=5, pady=5)
        self.history_list.insert(0, f"{num1} {operation} {num2} = {result}")
        # clear num 1 after calc
        self.num1_entry.delete(0, tk.END)
        # clear num 2 after calc
        self.num2_entry.delete(0, tk.END)
        self.function_entry.delete(0, tk.END)
    def clear(self):
        self.num1_entry.delete(0, tk.END)
        self.num2_entry.delete(0, tk.END)
        self.function_entry.delete(0, tk.END)
        self.result_entry.delete(0, tk.END)

    def click_number(self, number):
        if not self.function_entry.get():
            value = self.num1_entry.get()
            self.num1_entry.delete(0, tk.END)
            self.num1_entry.insert(0, str(value) + str(number))
        elif self.function_entry.get() in ["+", "-", "*", "/", "%", "**", "//", "sqrt", "cbrt"]:
            value = self.num2_entry.get()
            self.num2_entry.delete(0, tk.END)
            self.num2_entry.insert(0, str(value) + str(number))

    def click_function(self, function):
        value = self.function_entry.get()
        self.function_entry.delete(0, tk.END)
        self.function_entry.insert(0, str(value) + str(function))

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()


