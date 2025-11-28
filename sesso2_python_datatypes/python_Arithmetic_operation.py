# Python script to demonstrate various arithmetic operations with user input

print("Arithmetic Operations Demonstration")
print("_" * 40)

# Prompt the user for input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

print("\nYou entered:")
print(f"a = {a}")
print(f"b = {b}\n")

# Addition
print(f"Addition: {a} + {b} = {a + b}")

# Subtraction
print(f"Subtraction: {a} - {b} = {a - b}")

# Multiplication
print(f"Multiplication: {a} * {b} = {a * b}")

# Division (returns float)
print(f"Division: {a} / {b} = {a / b}")

# Floor Division (integer quotient)
print(f"Floor Division: {a} // {b} = {a // b}")

# Modulus (remainder)
print(f"Modulus: {a} % {b} = {a % b}")

# Exponentiation (power)
print(f"Exponentiation: {a} ** {b} = {a ** b}")

print("_" * 40)
print("Demonstration complete!")

