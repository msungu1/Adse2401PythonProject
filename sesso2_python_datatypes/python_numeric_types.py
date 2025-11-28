# Python script to demonstrate Python's number/numeric types

# Import modules for decimal and fraction types
from decimal import Decimal, ROUND_HALF_UP, ROUND_DOWN, getcontext
from fractions import Fraction

# Demonstrate integers (whole numbers, both +ve and -ve)
int_value = -8
print("Integer Demonstration")
print(f"The value in the variable int_value is {int_value}")
print(f"The type of int_value is {type(int_value)}\n")

# Demonstrate floats (numbers with fractional component, both +ve and -ve)
float_value = 3.11232
print("Float Number Demonstration")
print(f"The value in the variable float_value is {float_value}")
print(f"The type of float_value is {type(float_value)}\n")

# Demonstrate decimals (with fixed precision and rounding)
getcontext().prec = 7  # set higher precision when you need accuracy

decimal_value = Decimal('10.4567')
print("Decimal Number Demonstration")
print(f"The value in the variable decimal_value is {decimal_value}")
print(f"The type of decimal_value is {type(decimal_value)}\n")

# Using ROUND_DOWN to ensure no rounding up takes place
decimal_value = Decimal('1.2345678').quantize(Decimal('0.0001'), rounding=ROUND_DOWN)
print(f"The value in the variable decimal_value after quantize is {decimal_value}")
print(f"The type of decimal_value is {type(decimal_value)}\n")

# Demonstrate complex numbers
complex_value = 3 + 4j
print("Complex Number Demonstration")
print("_" * 32)
print(f"The value in the variable complex_value is {complex_value}")
print(f"The type of complex_value is {type(complex_value)}\n")
print(f"The real part of complex_value is {complex_value.real}")
print(f"The imaginary part of complex_value is {complex_value.imag}\n")

# Demonstrate fractions (rational numbers as numerator/denominator)
fraction_value = Fraction(3, 4)
print("_" * 32)
print("Fraction Number Demonstration")
print(f"The value in the variable fraction_value is {fraction_value}")
print(f"The type of fraction_value is {type(fraction_value)}\n")

# Demonstrate booleans (subclass of int, used in logical operations)
true_value = True
false_value = False
print("_" * 32)
print("Boolean Demonstration")
print(f"The value in the variable true_value is {true_value}")
print(f"The type of true_value is {type(true_value)}")
print(f"The value in the variable false_value is {false_value}")
print(f"The type of false_value is {type(false_value)}\n")

# Booleans in arithmetic operations
print("Booleans in Arithmetic")
print(f"True + True = {True + True}")
print(f"True + False = {True + False}")
print(f"False + False = {False + False}")
print(f"True * 10 = {True * 10}")
print(f"False * 10 = {False * 10}")
print(f"True - False = {True - False}")
print(f"False - True = {False - True}\n")

# Demonstrate boolean conversions and usage
print("_" * 32)
print("Boolean Conversions and Usage")
print(f"int(True) = {int(True)}")
print(f"int(False) = {int(False)}")
print(f"bool(1) = {bool(1)}")
print(f"bool(0) = {bool(0)}")
print(f"bool(-5) = {bool(-5)}")  # any non-zero number is True
