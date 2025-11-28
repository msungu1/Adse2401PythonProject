# sphere.py
# Define a Sphere class with volume and surface area calculations

from circle import Circle
import math


class Sphere(Circle):
    """
    A class to represent a sphere, inheriting from Circle.

    Parameters
    ----------
    radius : float
        The radius of the sphere in centimeters.

    Methods
    -------
    calc_volume():
        Calculate the volume of the sphere.
    calc_surface_area():
        Calculate the surface area of the sphere.
    from_diameter(diameter):
        Create a Sphere instance using diameter instead of radius.
    __str__():
        Return a string representation of the sphere with radius, volume, and surface area.
    """

    def __init__(self, radius: float):
        """
        Initialize a Sphere instance.

        Parameters
        ----------
        radius : float
            The radius of the sphere in centimeters.
        """
        super().__init__(radius)

    def calc_volume(self) -> float:
        """
        Calculate the volume of the sphere.

        Returns
        -------
        float
            The volume of the sphere, computed as (4/3) * π * r³.
        """
        return (4.0 / 3.0) * math.pi * math.pow(self.radius, 3)

    def calc_surface_area(self) -> float:
        """
        Calculate the surface area of the sphere.

        Returns
        -------
        float
            The surface area of the sphere, computed as 4 * π * r².
        """
        return 4 * math.pi * math.pow(self.radius, 2)

    @classmethod
    def from_diameter(cls, diameter: float):
        """
        Create a Sphere instance using diameter.

        Parameters
        ----------
        diameter : float
            The diameter of the sphere in centimeters.

        Returns
        -------
        Sphere
            A new Sphere instance with radius = diameter / 2.
        """
        return cls(diameter / 2)

    def __str__(self) -> str:
        """
        Return a string representation of the sphere.

        Returns
        -------
        str
            A formatted string with radius, volume, and surface area.
        """
        return (
            f"Sphere's dimensions\n"
            + "-" * 48 +
            f"\nRadius: {self.radius} cm\n"
            f"Volume: {self.calc_volume():.2f} cubic cm\n"
            f"Surface Area: {self.calc_surface_area():.2f} square cm"
        )
