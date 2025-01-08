import tkinter as tk
from tkinter import messagebox
import random

advice_list = [
    "Believe in yourself.",
    "Stay positive.",
    "Never give up.",
    "Be kind to others.",
    "Take it one step at a time.",
    "Learn from your mistakes.",
    "Stay focused.",
    "Be patient.",
    "Take care of your health.",
    "Keep learning."
]

def give_advice():
    advice = random.choice(advice_list)
    messagebox.showinfo("Advice", advice)

# Create the main window
root = tk.Tk()
root.title("Advice Generator")

# Create a button to generate advice
advice_button = tk.Button(root, text="Give me advice", command=give_advice)
advice_button.pack(pady=20)

# Run the application
root.mainloop()