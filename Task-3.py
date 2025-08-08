import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Invalid Input", "Password length must be a positive number.")
            return

        characters = ""
        if uppercase_var.get():
            characters += string.ascii_uppercase
        if lowercase_var.get():
            characters += string.ascii_lowercase
        if digits_var.get():
            characters += string.digits
        if special_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showerror("Invalid Selection", "Please select at least one character type.")
            return

        password = "".join(random.choice(characters) for _ in range(length))
        password_label.config(text=f"Generated Password: {password}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number for the password length.")


window = tk.Tk()
window.title("Password Generator")
window.geometry("500x500")


title_label = tk.Label(window, text="Password Generator", font=("Times New Roman", 20, "bold"))
title_label.pack(pady=10)

length_frame = tk.Frame(window)
length_frame.pack(pady=5)
tk.Label(length_frame, text="Password length:",font = ("Arial",12)).pack(side=tk.LEFT)
length_entry = tk.Entry(length_frame, width=10)
length_entry.pack(side=tk.LEFT)

complexity_frame = tk.LabelFrame(window, text="Complexity Options")
complexity_frame.pack(pady=10, padx=10, fill="x")

uppercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(complexity_frame, text="Use Uppercase Letters", variable=uppercase_var).pack(anchor="w")

lowercase_var = tk.BooleanVar(value=True)
tk.Checkbutton(complexity_frame, text="Use Lowercase Letters", variable=lowercase_var).pack(anchor="w")

digits_var = tk.BooleanVar(value=True)
tk.Checkbutton(complexity_frame, text="Use Digits", variable=digits_var).pack(anchor="w")

special_var = tk.BooleanVar(value=True)
tk.Checkbutton(complexity_frame, text="Use Special Characters", variable=special_var).pack(anchor="w")

generate_button = tk.Button(window, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

password_label = tk.Label(window, text="Generated Password: ", font=("Arial Black", 12,"bold"))
password_label.pack(pady=10)

window.mainloop()