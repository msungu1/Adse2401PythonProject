# Define the logger decorator
def log_dimensions(cls):
    class Wrapper(cls):
        def __init__(self, *args, **kwargs):
            print(f"Logging dimensions for {cls.__name__}")
            super().__init__(*args, **kwargs)

    return Wrapper


@log_dimensions
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)

    def __str__(self):
        return (f"Rectangle dimensions\n"
                + "-" * 45 + "\n"
                + f"Width: {self.width}\n"
                + f"Height: {self.height}\n"
                + f"Area: {self.calculate_area()}\n"
                + f"Perimeter: {self.calculate_perimeter()}")


# prompt the user for the dimensions  of the rectangle
length = int(input("Enter length: "))
width = int(input("Enter width: "))

# create/instantiate a rectangle object with above dimensions
rectangle = Rectangle(length, width)
print = (rectangle)
