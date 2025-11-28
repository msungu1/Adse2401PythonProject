# Function to get nth Fibonacci number using recursion
def fibonacci(n):
    """
    Calculates the n-th Fibonacci number using recursion.

    :param n (int): the n-th Fibonacci number
    :return: the n-th Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# Fibonacci function decorator
def fib_decorator(func):
    """
    Decorator function that adds print statements before and after executing
    the decorated function.

    :param func (function): the decorated function
    :return: the decorated function
    """

    def wrapper(n):
        print("Calculating the Fibonacci numbers ...")
        result = func(n)
        print(f"Fibonacci numbers generated: {result}")
        return result

    return wrapper


# Make use of the above decorator
@fib_decorator
def generate_fibonacci_numbers(n):
    """
    Generate list of Fibonacci numbers up to the value of n using the fibonacci function.

    :param n (int): the count of the Fibonacci numbers to generate
    :return (list): A list of Fibonacci numbers
    """
    return [fibonacci(a) for a in range(n)]


print("\nFirst 18 Fibonacci numbers:")
generate_fibonacci_numbers(18)
