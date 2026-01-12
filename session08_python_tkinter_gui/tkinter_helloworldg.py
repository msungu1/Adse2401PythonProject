#python tkinter script/file with a lable and button to display a message  on the screen once the button is cliked

# import the tkinter module

import tkinter as tk

# instantiate a tk object

root = tk.Tk()

# get the screen width and height

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# calculate the x and y position to center the window/gui

x = (screen_width - 620) // 2
y = (screen_height - 480) // 2

# set the dimensions of the window
root.geometry('640*480+{}+{}'.format(x, y))
root.mainloop()

label = tk.Label(root, text='Hello World', font=('Arial', 25), fg='red')
label.pack()

# function defination
def toggle_text():
    if label['text'] == "Hello World":
        label['text'] = 'By world'
    else:
        label['text'] = 'Hello World'

        # create a button with its content and font size

        button = tk.Button(root, text='Toogle Button', command=toggle_text, font=('Arial', 25), fg='blue')
        button.pack()

        # run the application
        root.mainloop()