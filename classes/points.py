#! /usr/bin/python3

import math

class Point():
    """Represents a point in teo-demensional geometric coordinate """

    def __init__(self, x=0, y=0):
        """ Initialize the positions of a new point.
        If not given they are assigned a default value of 0

        parameter:
        ----------
        x : position on the x-axis
        y : position on the y-axis
        """
        self.move(x, y)

    def move(self, x:int, y:int)-> None:
        """Moves the points to a new position """
        self.x = x
        self.y = y

    def reset(self)->None:
        """returns the points to it's original position (0, 0)"""
        self.move(0, 0)

    def calculate_distance(self:object, other_point:object)-> float:
        """Calculates the distance between two points

        This function uses the Pythagorean Theorem to calculate
        the distance between the two points. The distance is
        returned as a float.
        """
        return math.sqrt(
            (self.x - other_point.x)**2 + (self.y - other_point.y)**2
        )

    def __str__(self):
        return f'point x: {self.x}, point y :{self.y}'

if __name__ == '__main__':
    point = Point(3, 5)
    print(point)





#point1 = Point()
#point2 = Point()
#point1.reset()
#point2.move(5, 0)

#print(point2.calculate_distance(point1))
#assert point2.calculate_distance(point1) == point1.calculate_distance(point2)

#point1.move(3, 4)

#print(point1.calculate_distance(point2))
#print(point1.calculate_distance(point1))
