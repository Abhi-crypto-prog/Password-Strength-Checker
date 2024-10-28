import tkinter as tk
from tkinter import messagebox
import re

# Function to validate the password
def validate_password():
    password = entry_password.get()  # Get the entered password
    if len(password) < 8:
        messagebox.showwarning("Weak Password", "Password must be at least 8 characters long.")
    elif not re.search("[A-Z]", password):
        messagebox.showwarning("Weak Password", "Password must contain at least one uppercase letter.")
    elif not re.search("[a-z]", password):
        messagebox.showwarning("Weak Password", "Password must contain at least one lowercase letter.")
    elif not re.search("[0-9]", password):
        messagebox.showwarning("Weak Password", "Password must contain at least one number.")
    else:
        messagebox.showinfo("Strong Password", "Your password is strong!")

# Set up the GUI
root = tk.Tk()
root.title("Password Validator by Abhishek Chatterjee")
root.geometry("300x200")

# Add label and entry widget
label = tk.Label(root, text="Enter your password:")
label.pack(pady=10)

entry_password = tk.Entry(root, show="*", width=25)
entry_password.pack(pady=10)

# Add validate button
validate_button = tk.Button(root, text="Validate Password", command=validate_password)
validate_button.pack(pady=10)

# Start the GUI event loop
root.mainloop()
