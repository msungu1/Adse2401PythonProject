# circle.py
# Define a Circle class with area and perimeter calculations

import math


class Circle:
    """
    A class to represent a circle.

    Parameters
    ----------
    radius : float
        The radius of the circle in centimeters.

    Methods
    -------
    calc_area():
        Calculate the area of the circle.
    calc_perimeter():
        Calculate the perimeter (circumference) of the circle.
    __str__():
        Return a string representation of the circle with radius, area, and perimeter.
    """

    def __init__(self, radius):
        """
        Initialize a Circle instance.

        Parameters
        ----------
        radius : float
            The radius of the circle in centimeters.
        """
        self.radius = radius

    def calc_area(self):
        """
        Calculate the area of the circle.

        Returns
        -------
        float
            The area of the circle, computed as π * r².
        """
        return math.pi * math.pow(self.radius, 2)

    def calc_perimeter(self):
        """
        Calculate the perimeter (circumference) of the circle.

        Returns
        -------
        float
            The perimeter of the circle, computed as 2 * π * r.
        """
        return 2 * math.pi * self.radius

    def __str__(self):
        """
        Return a string representation of the circle.

        Returns
        -------
        str
            A formatted string with radius, area, and perimeter.
        """
        return f"Circle with radius {self.radius}, area {self.calc_area():.2f}, perimeter {self.calc_perimeter():.2f}"
