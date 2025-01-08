import math

# Base class Coordinate
class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        # 2D distance formula
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def __str__(self):
        return f"<{self.x}, {self.y}>"

# Subclass Point3D
class Point3D(Coordinate):
    def __init__(self, x, y, z):
        super().__init__(x, y)  # Initialize x and y from Coordinate
        self.z = z  # Add z coordinate

    def distance(self, other):
        # 3D distance formula
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2 + (self.z - other.z) ** 2)

    def __str__(self):
        # Format output as "<x, y, z>"
        return f"<{self.x}, {self.y}, {self.z}>"

# Testing the Point3D class
point1 = Point3D(1, 2, 3)
point2 = Point3D(4, 6, 8)

# Print the points using the __str__ method
print(point1)  # Expected output: "<1, 2, 3>"
print(point2)  # Expected output: "<4, 6, 8>"

# Calculate and print the 3D distance
print(point1.distance(point2))  # Expected output: 7.071...
