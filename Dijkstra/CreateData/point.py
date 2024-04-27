import math

class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y


    def __str__(self):
        return f"({self.x},{self.y})"


    def __hash__(self):
        return hash((self.x, self.y))
    

    def distance_to(self, pt):
        dx = pt.x - self.x
        dy = pt.y - self.y
        return math.sqrt(dx*dx + dy*dy)


def distance_between(pt1, pt2):
    return pt1.distance_to(pt2)


def parse_point(s):
    if s[0] != "(":
        raise Exception(f"parse_point: does not start with '('")
    if s[-1] != ")":
        raise Exception(f"parse_point: does not end with ')'")
    fields = s[1:-1].replace(" ", "").split(",")
    if len(fields) != 2:
        raise Exception(f"parse_point: {len(fields)} fields found, 2 expected")
    return Point(int(fields[0]), int(fields[1]))
