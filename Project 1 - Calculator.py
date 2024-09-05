import tkinter as tk
from tkinter import messagebox
import math

class ExtendedCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Extended Calculator")
        
        # Entry widget to show the expression
        self.entry = tk.Entry(root, width=20, font=("Arial", 24), borderwidth=2, relief="ridge")
        self.entry.grid(row=0, column=0, columnspan=5)
        
        # Button layout
        buttons = [
            '1', '2', '3', '/', 'sqrt',
            '4', '5', '6', '*', '^2',
            '7', '8', '9', '-', '^3',
            'C', '0', '=', '+', '<-'
        ]
        
        # Create and place buttons
        row_val = 1
        col_val = 0
        for button in buttons:
            self.create_button(button, row_val, col_val)
            col_val += 1
            if col_val > 4:
                col_val = 0
                row_val += 1
    
    def create_button(self, text, row, column):
        button = tk.Button(self.root, text=text, width=5, height=2, font=("Arial", 18), command=lambda t=text: self.on_button_click(t))
        button.grid(row=row, column=column)
    
    def on_button_click(self, char):
        if char == 'C':
            self.entry.delete(0, tk.END)
        elif char == '=':
            try:
                expression = self.entry.get()
                # Replace power operator '^' with '**' for evaluation
                expression = expression.replace('^', '**')
                result = str(eval(expression))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif char == 'sqrt':
            try:
                value = float(self.entry.get())
                result = str(math.sqrt(value))
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif char == '^2':
            try:
                value = float(self.entry.get())
                result = str(value ** 2)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif char == '^3':
            try:
                value = float(self.entry.get())
                result = str(value ** 3)
                self.entry.delete(0, tk.END)
                self.entry.insert(0, result)
            except Exception as e:
                messagebox.showerror("Error", "Invalid Input")
        elif char == '<-':
            current_text = self.entry.get()
            if len(current_text) > 0:
                self.entry.delete(len(current_text)-1, tk.END)
        else:
            self.entry.insert(tk.END, char)

if __name__ == "__main__":
    root = tk.Tk()
    calculator = ExtendedCalculator(root)
    root.mainloop()
