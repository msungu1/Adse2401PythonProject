import inspect
from functools import lru_cache

def add(a, b):
    """
    Calculates the sum of two numbers.
    :param a(int, float): The first number.
    :param b(int, float): The second number.
    :returns:
        int, float: The sum of two numbers. Return type depends on the type of input.
    """
    return a + b


@lru_cache(maxsize=None)
def fibonacci(n):
    """
    Computes the nth Fibonacci number using dynamic programming (memoization).
    :param n(int): The position in the Fibonacci sequence (0-indexed).
    :returns:
        int: The nth Fibonacci number.
    """
    if n < 0:
        raise ValueError("n must be a non-negative integer")
    if n in (0, 1):
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def show_function_docs(func):
    """
    Prints the documentation of a given function using introspection.
    """
    print(f"Function name: {func.__name__}")
    print("Signature:", inspect.signature(func))
    print("Documentation:\n", inspect.getdoc(func))
    print("-" * 60)


def perform_operation(operation, x, y):
    """
    Performs a mathematical operation on two numbers.
    Supported values: add, subtract, multiply, divide.
    """
    op = operation.lower()  # normalize case
    if op == "add":
        return x + y
    elif op == "subtract":
        return x - y
    elif op == "multiply":
        return x * y
    elif op == "divide":
        if y == 0:
            raise ZeroDivisionError("Division by zero is not allowed")
        return x / y
    else:
        raise ValueError(f"Unsupported operation: {operation}")


if __name__ == "__main__":
    # Demonstrate add function
    print("Add function result:", add(5, 7))

    # Demonstrate Fibonacci with dynamic programming
    print("Fibonacci(10):", fibonacci(10))

    # Show documentation using introspection
    show_function_docs(add)
    show_function_docs(fibonacci)
    show_function_docs(perform_operation)

    # Example with case-insensitive operation
    operation, num1, num2 = 'AdD', 5, 3
    print(f"Results of Operation: {operation} on {num1} and {num2} is:\n"
          f"{perform_operation(operation, num1, num2)}\n")

    # Get values from the user
    operation = input("Enter operation (add, subtract, multiply, divide): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print(f"Results of Operation: {operation} on {num1} and {num2} is:\n"
          f"{perform_operation(operation, num1, num2)}\n")
