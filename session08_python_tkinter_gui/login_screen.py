import tkinter as tk
from tkinter import messagebox

# function to authenticate the user
def login():
    username = entry_username.get()
    password = entry_password.get()

    # check that the user has filled both their username and password
    if username.strip() == '' or password.strip() == '':
        messagebox.showerror("Missing Credentials", "Please enter both username and password")
        return

    # hard-coded username & password
    if username == 'admin' and password == 'mzungu':
        messagebox.showinfo("Login Successful", "Welcome admin, you are now logged in successfully")
    else:
        messagebox.showerror("Login Failed", "Incorrect username or password")

# function to toggle password visibility
def toggle_password():
    if show_password_var.get():
        entry_password.config(show="")
    else:
        entry_password.config(show="*")

# create/instantiate the main window
root = tk.Tk()
root.title("Login Screen")
root.geometry("640x480")
root.resizable(width=False, height=False)

# create a centered frame
frame = tk.Frame(root)
frame.place(relx=0.5, rely=0.5, anchor='center')

# labels
label_username = tk.Label(frame, text="Username")
label_username.grid(row=0, column=0, padx=10, pady=10, sticky='e')

label_password = tk.Label(frame, text="Password")
label_password.grid(row=1, column=0, padx=10, pady=10, sticky='e')

# entry fields
entry_username = tk.Entry(frame)
entry_username.grid(row=0, column=1, padx=10, pady=10)

entry_password = tk.Entry(frame, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=10)

# checkbox for showing/hiding the password
show_password_var = tk.BooleanVar()
check_show_password = tk.Checkbutton(frame, variable=show_password_var, text="Show Password", command=toggle_password)
check_show_password.grid(row=2, column=1, padx=10, pady=10, sticky='w')

# login button
button_login = tk.Button(frame, text="Login", command=login)
button_login.grid(row=3, columnspan=2, padx=10, pady=20)

# run the application
root.mainloop()
