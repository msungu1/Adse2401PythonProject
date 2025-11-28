# demo.py
# Python script to demonstrate working with user-defined/custom classes
# and instantiating them

# Import the required modules
from circle import Circle
from sphere import Sphere

# Prompt the user for the circle radius
radius = int(input("Enter radius of circle: "))

# Create / instantiate a Circle object
circle1 = Circle(radius)

# Prompt the user for the sphere radius
radius = int(input("Enter radius of sphere: "))

# Create / instantiate a Sphere object
sphere1 = Sphere(radius)

# Display the circle & sphere dimensions
print(circle1)
print(sphere1)
