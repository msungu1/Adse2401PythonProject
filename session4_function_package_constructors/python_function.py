# functions_demo.py
# This script demonstrates defining and calling/invoking user-defined functions in Python

# Define a function to display a greeting message when called/invoked
def greeting():
    print("Hello Roberto!")


# Define a function that accepts the user's name and then greets them
def greet_user(username):
    print("Hello %s from Python functions!" % username)


# Define a function that accepts two numbers & an operator ('+', '*', or '/')
# to add, multiply, or divide them
def add_or_multiply(first_num, second_num, op='+'):
    """
    Perform addition, multiplication, or division on two numbers.

    Args:
        first_num (float): The first number
        second_num (float): The second number
        op (str): Operator ('+', '*', 'x', '/')

    Returns:
        float: Result of the operation
    """
    if op == '+':
        return first_num + second_num
    elif op in ('*', 'x'):
        return first_num * second_num
    elif op == '/':
        if second_num == 0:
            raise ZeroDivisionError("Division by zero is not allowed.")
        return first_num / second_num
    else:
        raise ValueError("Unsupported operator. Use '+', '*', 'x', or '/'.")


# -------------------------------
# Demonstration of function calls
# -------------------------------

# Call/invoke the greeting() function
greeting()

# Prompt the user for their name and invoke greet_user()
name = input("What is your name? :\n")
greet_user(name)

# Prompt the user for two numbers and an operator
try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operator (+, *, x, /): ")

    # Call add_or_multiply() with user input
    result = add_or_multiply(num1, num2, op)
    print(f"Result of {num1} {op} {num2} = {result}")

except ValueError as ve:
    print(f"Error: {ve}")
except ZeroDivisionError as zde:
    print(f"Error: {zde}")

# display the documentation string for the add_or_multiply function
print(f"\nThe documentation string for the add_or_multiply function is:\n{add_or_multiply.__doc__}")

# anonymous function
plus_five = lambda num: num + 5  # use lambda to add five

# same functionality as the lambda above but using a full function
def add_five(num):
    return num + 5  # define a function to add 5 to the value passed in

# anonymous /lambda function to get the difference between 2 numbers
difference = lambda num1, num2: num1 - num2

# sample usage of the above lambda
print(f"The difference between 3 and 5 using a lambda function is: {difference(3, 5)}")

# function with a varying number of parameters
def get_sum(*values):
    """
    Returns the sum of all the numbers/values passed.

    Args:
        *values: variable number of values to be totaled/summed

    Returns:
        int or float: The sum of the values
    """
    total = 0
    for value in values:
        total += value
    return total


# create a list of numbers and sum them using the get_sum() function
num_list = [1, 2, 3, 4, 5]
print(f"Sum of num_list using get_sum: {get_sum(*num_list)}")

nums_with_decimal = [4.5, 1.5]
print(f"Sum of nums_with_decimal using get_sum: {get_sum(*nums_with_decimal)}")

# Demonstrate plus_five and add_five
print(f"Using plus_five lambda on 10: {plus_five(10)}")
print(f"Using add_five function on 10: {add_five(10)}")
