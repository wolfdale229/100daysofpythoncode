import math
from typing import Any, List, Callable

class Point(object):
    """Represent a point on a two dimensional plane"""

    def __init__(self, x=0, y=0):
        """Initialize the x and y positions of a point to default 0"""
        self.x = x
        self.y = y

    def distance_from_original(self)-> float:
        """Returns the difference between the points current position
        and it original position (x=0, y=0)"""
        return math.hypot(self.x, self.y)

    def __eq__(self, other:Any)-> bool:
        """Checks equality between two objects"""
        return (self.x == other.x) and (self.y == other.y)

    def __str__(self)-> str:
        """string representation of object"""
        return '{0.x!r}, {0.y!r}'.format(self)

    def __repr__(self)-> str:
        return 'Point{0.x!r}, {0.y!r}'.format(self)

class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def area(self):
        return math.pi * (self.radius**2)

    def circumference(self):
        return 2 * math.pi * self.radius

    def __eq__(self, other):
        return self.radius == other.radius and super().__eq__(other)
    
    def __repr__(self):
        return "Circle({0.radius!r}, {0.x!r}, {0.y!r})".format(self)
    
    def __str__(self):
        return repr(self)


















