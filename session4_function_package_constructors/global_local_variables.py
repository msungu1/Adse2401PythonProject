# python script to demonstrate the scope of global and local variables

# declare a global variable
global_var = 5

# define a function to display a value
def display_value(value):
    print(f"Value passed in: {value}")

# call the display_value function and pass in the global variable (global_var)
display_value(global_var)

# define a function that has its own local variable
def random_function():
    random_variable = 10  # local variable
    print(f"Inside random_function, local random_variable = {random_variable}")
    print(f"Inside random_function, global_var = {global_var}")  # can access global_var

# call the random_function
random_function()

# define a function that modifies the global variable
def modify_global():
    global global_var  # explicitly declare we want to use the global variable
    global_var = global_var + 20
    print(f"Inside modify_global, global_var modified to = {global_var}")

# call the modify_global function
modify_global()

# show that global_var has been changed globally
print(f"Outside functions, global_var = {global_var}")
