import tkinter as tk
from tkinter import filedialog, messagebox
import sys

variables = {}

def interpret(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    output = ""
    for line in lines:
        line = line.strip()
        if line.startswith("say "):
            output += line[4:].strip('"') + '\n'
        elif line.startswith("let "):
            parts = line.split()
            variables[parts[2]] = int(parts[4])
        elif " plus " in line:
            parts = line.split(" ")
            result = variables[parts[1]] + int(parts[3])
            output += f"{parts[1]} plus {parts[3]} = {result}\n"
    return output

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("NeonScript files", "*.neo")])
    if file_path:
        try:
            result = interpret(file_path)
            messagebox.showinfo("Output", result)
        except Exception as e:
            messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("NeonScript Runner")

open_button = tk.Button(root, text="Open .neo file", command=open_file)
open_button.pack(pady=20)

root.mainloop()
