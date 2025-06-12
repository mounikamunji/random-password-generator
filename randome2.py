import tkinter as tk
from tkinter import messagebox
import string
import random

def generate_password():
    length = length_var.get()
    if length <= 0:
        messagebox.showerror("Error", "Please enter a positive length")
        return
    
    char_set = ""
    if var_lowercase.get():
        char_set += string.ascii_lowercase
    if var_uppercase.get():
        char_set += string.ascii_uppercase
    if var_numbers.get():
        char_set += string.digits
    if var_special.get():
        char_set += string.punctuation
    
    if not char_set:
        messagebox.showerror("Error", "Select at least one character type")
        return
    
    password = ''.join(random.choice(char_set) for _ in range(length))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

# Setup window
root = tk.Tk()
root.title("Password Generator")

# Variables
length_var = tk.IntVar(value=8)
var_lowercase = tk.BooleanVar(value=True)
var_uppercase = tk.BooleanVar(value=True)
var_numbers = tk.BooleanVar(value=True)
var_special = tk.BooleanVar(value=False)

# Layout
tk.Label(root, text="Password Length:").grid(row=0, column=0, sticky="w")
tk.Spinbox(root, from_=4, to=64, textvariable=length_var, width=5).grid(row=0, column=1)

tk.Checkbutton(root, text="Lowercase (a-z)", variable=var_lowercase).grid(row=1, column=0, sticky="w")
tk.Checkbutton(root, text="Uppercase (A-Z)", variable=var_uppercase).grid(row=2, column=0, sticky="w")
tk.Checkbutton(root, text="Numbers (0-9)", variable=var_numbers).grid(row=3, column=0, sticky="w")
tk.Checkbutton(root, text="Special Characters (!@#$)", variable=var_special).grid(row=4, column=0, sticky="w")

tk.Button(root, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=2, pady=10)

password_entry = tk.Entry(root, width=40)
password_entry.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
