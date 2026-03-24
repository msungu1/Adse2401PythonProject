# Python script to demonstrate various arithmetic operations with user input

print("Arithmetic Operations Demonstration")
print("_" * 100)

# Prompt the user for input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
firstName = str(input("please enter  your name "))
secondName = str(input("pleas enter your second name kindly"))

print("\nYou entered:")
print(f"a = {a}")
print(f"b = {b}\n")
print(f"yor first name is ", firstName)
print("yourfirst name is ", secondName)

# Addition
print(f"{firstName},{secondName},you just added the following number and the Addition is : {a} + {b} = {a + b}")

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

# print("_" * 40)
print("Demonstration complete!")

