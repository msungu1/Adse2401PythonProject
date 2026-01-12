"""
Email Validator GUI Application
--------------------------------
This script creates a simple graphical user interface (GUI) using Tkinter
to validate email addresses with regular expressions (regex).

Features:
- Input field for entering an email address
- "Validate" button to check if the email is valid
- "Quit" button to close the application
- Pop-up message boxes showing validation results
- Styled labels, buttons, and background for a clean look
"""

# Import required modules
import re                       # For regular expression (regex) validation
import tkinter as tk            # Tkinter for GUI creation
from tkinter import messagebox  # For pop-up message dialogs

# -------------------------------
# Function to validate email input
# -------------------------------
def validate_email():
    """
    Validates the email entered in the input field using regex.

    Rules:
    - Must contain one '@' symbol
    - Local part (before @) can include letters, digits, dots, underscores, hyphens
    - Domain part (after @) must be valid (letters, digits, hyphens, dots)
    - Must end with a top-level domain (e.g., .com, .org, .net, .ke)

    Displays:
    - Warning if input is empty
    - Info message if email is valid
    - Error message if email is invalid
    """
    email = entry.get().strip()  # Get user input and remove extra spaces
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if not email:
        messagebox.showwarning("Input Error", "Please enter an email address.")
        return

    if re.match(pattern, email):
        messagebox.showinfo("Validation Result", f"The email {email} is a valid email address ✅")
    else:
        messagebox.showerror("Validation Result", f"The email {email} is NOT a valid email address ❌")

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()                        # Create main window
root.title("Email Validator")         # Window title
root.geometry("400x200")              # Window size (width x height)
root.config(bg="#f0f4f7")             # Background color

# Title label
title_label = tk.Label(
    root, text="Email Validator",
    font=("Arial", 16, "bold"),
    bg="#f0f4f7", fg="#333"
)
title_label.pack(pady=10)

# Entry label
entry_label = tk.Label(
    root, text="Enter your email:",
    font=("Arial", 12),
    bg="#f0f4f7"
)
entry_label.pack()

# Entry field
entry = tk.Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=5)

# Validate button
validate_btn = tk.Button(
    root, text="Validate",
    command=validate_email,
    bg="#4CAF50", fg="white",
    font=("Arial", 12, "bold")
)
validate_btn.pack(pady=10)

# Quit button
quit_btn = tk.Button(
    root, text="Quit",
    command=root.quit,
    bg="#f44336", fg="white",
    font=("Arial", 12, "bold")
)
quit_btn.pack()

# -------------------------------
# Run the application
# -------------------------------
root.mainloop()
