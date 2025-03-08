
from typing import Callable
import math

from point import Point


def min_point(pts: list[Point]) -> int:
    ''' Return the index of the point in pts
    with the smallest y coordinate, with ties
    broken by smallest x coordinate.

    This assumes pts is not empty.
    '''
    key: Callable = lambda pt : (pt[1], pt[0])
    min_idx: int = 0
    for i in range(1, len(pts)):
        if key(pts[i]) < key(pts[min_idx]):
            min_idx = i
    return min_idx


def ccw(pt1: Point, pt2: Point, pt3: Point) -> int:
    ''' Determine the direction of the turn along
     the path pt1 to pt2 to pt3.
     '''
    dx21 = pt2[0] - pt1[0]
    dy31 = pt3[1] - pt1[1]
    dy21 = pt2[1] - pt1[1]
    dx31 = pt3[0] - pt1[0]
    return dx21 * dy31 - dy21 * dx31


def angle(p0: Point, pt: Point) -> float:
    ''' Compute the angle formed by pt-p0 with the x axis.'''
    dy = pt[1] - p0[1]
    dx = pt[0] - p0[0]
    return math.atan2(dy, dx)


def manhattan_distance(p0, pt) -> int:
    ''' Compute the manhattan distance from p0 to pt. '''
    return abs((pt[0] - p0[0])) + abs((pt[1] - p0[1]))


def graham(orig_pts: list[Point]) -> list[Point]:
    ''' Python implementation of the Graham Scan algorithm
    for finding the convex hull of a set of points
    in a plan.

    A point is defined as a 2-element tuple, in the
    form (x, y).
    '''
    min_idx: int = min_point(orig_pts)
    p0: Point = orig_pts[min_idx]
    pts = orig_pts[:min_idx] + orig_pts[min_idx+1:]

    hull: list[Point] = [p0]

    # The lambda here returns a tuple containing the angle
    # and the distance; that way, points with identical angles
    # are sorted by distance from p0.
    pts.sort(key = lambda pt : (angle(p0, pt), manhattan_distance(p0, pt)))

    for pt in pts:
        while len(hull) > 1 and ccw(hull[-2], hull[-1], pt) <= 0:
            hull.pop()
        hull.append(pt)
    return hull


def main() -> None:
    pts: list[Point] = [(-1, 0), (0, 1), (0, -1), (1, 0)]
    hull = graham(pts)
    print(hull)


if __name__ == "__main__":
    main()
