import tkinter as tk
from tkinter import messagebox, ttk

# Define a function to read in the values from the user
def calc():
    first_number = entry_first.get()
    second_number = entry_second.get()
    operation = entry_operation.get()

    # Check if any of the above fields are empty
    if not first_number.strip() or not second_number.strip() or not operation.strip():
        messagebox.showerror("Missing Values or Operation",
                             "Please enter all values and the arithmetic operation")
        return

    try:
        # Convert the values from input fields to numbers
        first_number = float(first_number)
        second_number = float(second_number)
    except ValueError:
        messagebox.showerror("Invalid Values",
                             "Please enter valid numeric values for first & second number.")
        return

    # Check for division by zero
    if operation == "/" and second_number == 0:
        messagebox.showerror("Divide by Zero Error",
                             "Cannot divide by zero. Please enter a non-zero denominator.")
        return

    # Define the arithmetic operator mappings
    operations = {
        '+': first_number + second_number,
        '-': first_number - second_number,
        'x': first_number * second_number,
        '/': first_number / second_number,
    }

    # Show the result
    if operation in operations:
        result = operations[operation]
        label_answer.config(text=f"Result: {result}")
    else:
        messagebox.showerror("Invalid Operation",
                             "Please choose a valid operation (+, -, x, or /).")

# Create the main window
root = tk.Tk()
root.title("Calculator")
root.geometry("640x480")
root.resizable(False, False)

# Create a centered frame
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor="center")

# Labels
label_first = tk.Label(frame, text="Enter first number")
label_first.grid(row=0, column=0, padx=10, pady=10, sticky="w")

label_operation = tk.Label(frame, text="Operation (+, -, x, /)")
label_operation.grid(row=1, column=0, padx=10, pady=10, sticky="w")

label_second = tk.Label(frame, text="Enter second number")
label_second.grid(row=2, column=0, padx=10, pady=10, sticky="w")

label_answer = tk.Label(frame, text="Answer")
label_answer.grid(row=3, column=0, padx=10, pady=10, sticky="w")

# Entry widgets and combobox
input_width = 25

entry_first = tk.Entry(frame, width=input_width)
entry_first.grid(row=0, column=1, padx=10, pady=10)
entry_first.insert(0, "enter first number")
entry_first.focus_set()

operation_choices = ["+", "-", "x", "/"]
entry_operation = ttk.Combobox(frame, values=operation_choices, state="readonly", width=input_width)
entry_operation.grid(row=1, column=1, padx=10, pady=10)
entry_operation.set("select operation")

entry_second = tk.Entry(frame, width=input_width)
entry_second.grid(row=2, column=1, padx=10, pady=10)
entry_second.insert(0, "enter second number")

# Calculate button
button_calc = tk.Button(frame, text="Calculate", command=calc)
button_calc.grid(row=4, columnspan=2, padx=10, pady=20)

# Run the application
root.mainloop()
