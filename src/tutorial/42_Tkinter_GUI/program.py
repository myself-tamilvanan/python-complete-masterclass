# Chapter 42: Tkinter GUI
# 12 Hours Python Masterclass in Tamil - Data Engineering (Gowtham)
# Video: https://youtu.be/HAxm8n9QY50 | Timestamp: 10:07:44
# ============================================
# Run this script: python3 program.py

import tkinter as tk
from tkinter import messagebox, ttk

# -----------------------------------------------
# EXAMPLE 1: Simple Hello World Window
# -----------------------------------------------


def show_hello():
    """Simple Tkinter window demonstration."""
    root = tk.Tk()
    root.title("Hello Tkinter")
    root.geometry("300x200")

    label = tk.Label(root, text="Hello, World!", font=("Arial", 20), fg="blue")
    label.pack(pady=20)

    def on_click():
        label.config(text="Button Clicked!", fg="green")

    btn = tk.Button(root, text="Click Me", command=on_click, bg="lightblue")
    btn.pack(pady=10)

    root.mainloop()


# -----------------------------------------------
# EXAMPLE 2: Simple Calculator
# -----------------------------------------------


class Calculator:
    """A simple calculator GUI application."""

    def __init__(self, root):
        self.root = root
        self.root.title("Python Calculator")
        self.root.geometry("320x450")
        self.root.resizable(False, False)

        self.expression = ""
        self._build_ui()

    def _build_ui(self):
        # Display
        self.display = tk.Entry(
            self.root, font=("Arial", 24), bd=10, relief=tk.SUNKEN, justify=tk.RIGHT
        )
        self.display.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)

        # Button layout
        buttons = [
            ("C", 1, 0),
            ("(", 1, 1),
            (")", 1, 2),
            ("/", 1, 3),
            ("7", 2, 0),
            ("8", 2, 1),
            ("9", 2, 2),
            ("*", 2, 3),
            ("4", 3, 0),
            ("5", 3, 1),
            ("6", 3, 2),
            ("-", 3, 3),
            ("1", 4, 0),
            ("2", 4, 1),
            ("3", 4, 2),
            ("+", 4, 3),
            ("0", 5, 0),
            (".", 5, 1),
            ("DEL", 5, 2),
            ("=", 5, 3),
        ]

        for text, row, col in buttons:
            cmd = lambda t=text: self._on_button(t)
            btn = tk.Button(
                self.root,
                text=text,
                font=("Arial", 16),
                command=cmd,
                bg="#f0f0f0",
                relief=tk.RAISED,
            )
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

    def _on_button(self, char):
        if char == "=":
            try:
                result = str(eval(self.expression))
                self.display.delete(0, tk.END)
                self.display.insert(0, result)
                self.expression = result
            except:
                messagebox.showerror("Error", "Invalid expression")
                self.expression = ""
                self.display.delete(0, tk.END)
        elif char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        elif char == "DEL":
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        else:
            self.expression += char
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)


# -----------------------------------------------
# EXAMPLE 3: Form with Validation
# -----------------------------------------------


class RegistrationForm:
    """Registration form with validation."""

    def __init__(self, root):
        self.root = root
        self.root.title("User Registration")
        self.root.geometry("400x350")

        # Form fields
        fields = ["Name", "Email", "Phone", "Age"]
        self.entries = {}

        for i, field in enumerate(fields):
            label = tk.Label(root, text=field + ":", font=("Arial", 12))
            label.grid(row=i, column=0, padx=10, pady=10, sticky="e")

            entry = tk.Entry(root, font=("Arial", 12), width=25)
            entry.grid(row=i, column=1, padx=10, pady=10)
            self.entries[field] = entry

        # Gender selection
        tk.Label(root, text="Gender:", font=("Arial", 12)).grid(
            row=4, column=0, padx=10, sticky="e"
        )
        self.gender = ttk.Combobox(root, values=["Male", "Female", "Other"], width=22)
        self.gender.grid(row=4, column=1, padx=10, pady=10)

        # Submit button
        tk.Button(
            root, text="Register", command=self._submit, bg="green", fg="white", font=("Arial", 12)
        ).grid(row=5, column=1, pady=10)

    def _submit(self):
        name = self.entries["Name"].get()
        email = self.entries["Email"].get()

        if not name:
            messagebox.showerror("Error", "Name is required!")
            return
        if "@" not in email:
            messagebox.showerror("Error", "Invalid email address!")
            return

        messagebox.showinfo("Success", f"Welcome, {name}!\nRegistered: {email}")


# -----------------------------------------------
# MAIN - Run the app
# -----------------------------------------------

if __name__ == "__main__":
    # Run the calculator
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
