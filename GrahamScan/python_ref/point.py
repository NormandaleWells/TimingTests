''' Definition of a Point.

For the reference version we'll have a point class,
since that seems to me to be the most straightforward
way to implement it, since it allows us to use .x
and .y instead of [0] and [1].
'''

import math
from typing import Self


class Point:
    def __init__(self, x: int = 0, y: int = 0) -> None:
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x},{self.y})"

    def __repr__(self):
        return f"Point({self.x},{self.y})"

    def angle_to(self, pt: Self) -> float:
        ''' Compute the angle formed by pt-self with the x axis.'''
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.atan2(dy, dx)

    def manhattan_distance(self, pt: Self) -> int:
        ''' Compute the distance from self to pt.'''
        return abs((pt.x - self.x)) + abs((pt.y - self.y))


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
