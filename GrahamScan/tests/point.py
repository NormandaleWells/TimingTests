'''
    point.py
'''

import math

class Point:
    ''' The Point class

    This Point class represents a 2-dimensional
    point with integer coordinates.

    Since this class has no invariant, the
    x and y values are publicly available and
    may be modified by client code.
    '''

    def __init__(self, x: int, y: int):
        self.x: int = x
        self.y: int = y


    def __str__(self):
        return f"({self.x},{self.y})"


    def __repr__(self):
        return f"Point({self.x},{self.y})"


    def __hash__(self):
        return hash((self.x, self.y))


    def __eq__(self, pt):
        return self.x == pt.x and self.y == pt.y


    def distance_to(self, pt: 'Point') -> float:
        ''' Compute the distance from self to pt

        The distance is returned as a floating
        point number.
        '''
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx*dx + dy*dy)


def distance_between(pt1: Point, pt2: Point):
    ''' Compute the distance between two points

        The distance is returned as a floating
        point number.
    '''
    return pt1.distance_to(pt2)


def parse_point(s):
    ''' Convert a string to a Point

    The string must be in the format produced
    by __str__.
    '''
    if s[0] != "(":
        raise ValueError("parse_point: does not start with '('")
    if s[-1] != ")":
        raise ValueError("parse_point: does not end with ')'")
    fields = s[1:-1].replace(" ", "").split(",")
    if len(fields) != 2:
        raise ValueError(f"parse_point: {len(fields)} fields found, 2 expected")
    return Point(int(fields[0]), int(fields[1]))
