import tkinter as tk
from tkinter import messagebox

def calculate():
    
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                messagebox.showerror("Error", "Cannot divide by zero.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return

        result_label.config(text=f"Result: {result}")

    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")


window = tk.Tk()
window.title("Simple Calcy")
window.geometry("500x500")



title_label = tk.Label(window, text="Calculator", font=("Arial Black", 25, "bold"))
title_label.pack(pady=10)

frame_num1 = tk.Frame(window)
frame_num1.pack(pady=5)
tk.Label(frame_num1, text="First Number:",font = (10)).pack(side=tk.LEFT)
entry_num1 = tk.Entry(frame_num1, width=15)
entry_num1.pack(side=tk.LEFT)

frame_num2 = tk.Frame(window)
frame_num2.pack(pady=5)
tk.Label(frame_num2, text="Second Number:",font = (10)).pack(side=tk.LEFT)
entry_num2 = tk.Entry(frame_num2, width=15)
entry_num2.pack(side=tk.LEFT)


frame_operation = tk.Frame(window)
frame_operation.pack(pady=10)
tk.Label(frame_operation, text="Operation:",font =(10)).pack(side=tk.LEFT)

operation_var = tk.StringVar(value="+")  
operations = ["+", "-", "*", "/"]
for op in operations:
    tk.Radiobutton(frame_operation, text=op, variable=operation_var, value=op).pack(side=tk.LEFT)

calculate_button = tk.Button(window, text="Calculate", command=calculate,font = (10))
calculate_button.pack(pady=10)

result_label = tk.Label(window, text="Result: ", font=( 10))
result_label.pack(pady=10)

window.mainloop()