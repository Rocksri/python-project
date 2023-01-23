import math


class AreaCalculator:

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def calculate_area(self):
        try:
            area = math.sqrt((self.x1 - self.x2) ** 2 + (self.y1 - self.y2) ** 2)
            return area
        except ValueError:
            print("Invalid input, please enter valid coordinates.")


# create object of DistanceCalculator class
coordinates = AreaCalculator(1, 3, 5, 7)

# call the calculate_distance method
print("The Distance is:", coordinates.calculate_area())
