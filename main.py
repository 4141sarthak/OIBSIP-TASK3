import tkinter as tk
from tkinter import messagebox
import random
import string
import pyperclip

# Password Generator Logic 

def generate_password():
    try:
        length = int(length_var.get())

        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4")
            return

        use_upper = upper_var.get()
        use_lower = lower_var.get()
        use_digits = digit_var.get()
        use_symbols = symbol_var.get()

        if not (use_upper or use_lower or use_digits or use_symbols):
            messagebox.showerror("Error", "Select at least one character type!")
            return

        exclude_chars = exclude_entry.get()

        char_pool = ""

        if use_upper:
            char_pool += string.ascii_uppercase
        if use_lower:
            char_pool += string.ascii_lowercase
        if use_digits:
            char_pool += string.digits
        if use_symbols:
            char_pool += string.punctuation

        # Remove excluded characters
        char_pool = ''.join([c for c in char_pool if c not in exclude_chars])

        if not char_pool:
            messagebox.showerror("Error", "No characters left after exclusion!")
            return

        password = []

        # Enforce complexity rules
        if complexity_var.get() == "High":
            if use_upper:
                password.append(random.choice(string.ascii_uppercase))
            if use_lower:
                password.append(random.choice(string.ascii_lowercase))
            if use_digits:
                password.append(random.choice(string.digits))
            if use_symbols:
                password.append(random.choice(string.punctuation))

        # Fill remaining length
        while len(password) < length:
            password.append(random.choice(char_pool))

        random.shuffle(password)
        final_password = ''.join(password)

        password_var.set(final_password)

    except ValueError:
        messagebox.showerror("Error", "Enter a valid number!")


def copy_to_clipboard():
    pwd = password_var.get()
    if pwd:
        pyperclip.copy(pwd)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password to copy!")


# ------------------ GUI ------------------ #

root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("500x500")
root.configure(bg="#1e1e2f")

# Variables
length_var = tk.StringVar(value="12")
password_var = tk.StringVar()

upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
digit_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

complexity_var = tk.StringVar(value="Medium")

# Title
tk.Label(root, text="Password Generator", font=("Arial", 18, "bold"),
         bg="#1e1e2f", fg="white").pack(pady=10)

# Length Input
tk.Label(root, text="Password Length", bg="#1e1e2f", fg="white").pack()
tk.Entry(root, textvariable=length_var).pack(pady=5)

# Checkboxes
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=10)

tk.Checkbutton(frame, text="Uppercase", variable=upper_var,
               bg="#1e1e2f", fg="white", selectcolor="#333").grid(row=0, column=0)

tk.Checkbutton(frame, text="Lowercase", variable=lower_var,
               bg="#1e1e2f", fg="white", selectcolor="#333").grid(row=0, column=1)

tk.Checkbutton(frame, text="Numbers", variable=digit_var,
               bg="#1e1e2f", fg="white", selectcolor="#333").grid(row=1, column=0)

tk.Checkbutton(frame, text="Symbols", variable=symbol_var,
               bg="#1e1e2f", fg="white", selectcolor="#333").grid(row=1, column=1)

# Complexity Dropdown
tk.Label(root, text="Complexity Level", bg="#1e1e2f", fg="white").pack()
tk.OptionMenu(root, complexity_var, "Low", "Medium", "High").pack(pady=5)

# Exclude characters
tk.Label(root, text="Exclude Characters", bg="#1e1e2f", fg="white").pack()
exclude_entry = tk.Entry(root)
exclude_entry.pack(pady=5)

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password,
          bg="#4CAF50", fg="white", width=20).pack(pady=15)

# Output
tk.Entry(root, textvariable=password_var, width=30,
         font=("Arial", 12), justify="center").pack(pady=10)

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard,
          bg="#2196F3", fg="white").pack(pady=10)

root.mainloop()