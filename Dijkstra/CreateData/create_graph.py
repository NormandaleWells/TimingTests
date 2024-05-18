'''
    create_graph.py

    Program to create a weighted graph from a file of points.
'''
import bisect
import sys

from typing import Tuple

import point_utils
import point


def create_edge(idx1: int, idx2: int) -> Tuple[int,int]:
    ''' Create a edge '''
    return min(idx1, idx2), max(idx1, idx2)


def check_point(
        nearest_pts: list[Tuple[int,float]],
        pts: list[point.Point],
        idx: int,
        check_idx: int,
        degree: int,
        edges: set[Tuple[int,int]]):
    ''' Check to see if this point can be added to the list of nearest points.

        Returns True if the point is added, False otherwise
    '''
    dist = point.distance_between(pts[idx], pts[check_idx])

    edge = create_edge(idx, check_idx)

    # If we don't have enough points yet, we just add it.
    if len(nearest_pts) < degree:
        bisect.insort(nearest_pts, (check_idx, dist), key = lambda pt_data : pt_data[1])
        edges.add(edge)
        return True

    # If this is greater or equal to the last point, then
    # it is not a nearest point.
    elif dist >= nearest_pts[-1][1]:
        return False

    # Otherwise we remove the last element (the point with the
    # longest distance) and insert it into the list where it belongs.
    # We also need to remove the edge from the list of edges.
    else:
        old_edge = create_edge(idx, nearest_pts[-1][0])
        edges.remove(old_edge)

        nearest_pts.pop()
        bisect.insort(nearest_pts, (check_idx, dist), key = lambda pt_data : pt_data[1])
        edges.add(edge)
        return True


def create_graph(pts: list[point.Point], degree: int, outfile):
    ''' Create a graph '''

    # Sort the points by x coordinate.  We don't
    # care about the y coordinates; in fact, we're
    # probably better off keeping the y ordering
    # random for a given x value.
    pts = sorted(pts, key = lambda pt : pt.x)

    # We keep track of the set of edges we've already
    # added so we don't add an edge twice.  Each edge
    # is identified by its start and end vertices,
    # with the smaller vertex first.
    edges: set[Tuple[int,int]] = set()

    # For each point, we want to alternate moving
    # one point to the left and one point to the right
    # looking for a point closer than any other point
    # so far.  We can stop moving in a given direction
    # whenever the index hits the end, or the x distance
    # between the point we're processing and the next
    # point in that direction is greater than the
    # farthest of the closest `degree` points.
    for i, pt in enumerate(pts):

        prev_idx = next_idx = i

        # nearest_pts will hold tuples (idx,dist) where
        # idx is the index of one of the degree'th nearest
        # points and dist is the distance to that point
        # from point i
        nearest_pts = []

        # We want to enter the loop with one point already
        # in the list.
        done = False
        while prev_idx != 0 and not done:
            prev_idx -= 1
            if (prev_idx, i) not in edges:
                nearest_pts.append((prev_idx, point.distance_between(pt, pts[prev_idx])))
                edges.add((prev_idx, i))
                done = True

        while not done:
            next_idx += 1
            if (i, next_idx) not in edges:
                nearest_pts.append((next_idx, point.distance_between(pt, pts[next_idx])))
                edges.add((i, next_idx))
                done = True

        while True:

            # Figure out if we can go left or right.
            max_dist = nearest_pts[-1][1]
            have_enough = len(nearest_pts) == degree
            done_left = prev_idx == 0 or \
                    pts[i].x - pts[prev_idx-1].x > max_dist and have_enough
            done_right = next_idx == len(pts) - 1 or \
                    pts[next_idx+1].x - pts[i].x > max_dist and have_enough

            # If we have enough points, and we can't go either
            # direction, get out now.
            if have_enough and done_left and done_right:
                break

            if not done_left:
                prev_idx -= 1
                if (prev_idx, i) not in edges:
                    check_point(nearest_pts, pts, i, prev_idx, degree, edges)
            if not done_right:
                next_idx += 1
                check_point(nearest_pts, pts, i, next_idx, degree, edges)

        for near_pt in nearest_pts:
            idx = near_pt[0]
            dist = near_pt[1]
            outfile.write(f"{pt} {pts[idx]} {dist:.4f}\n")


def main(argv):
    ''' main function '''
    if len(argv) < 3:
        print("usage: create_graph <pointfile> <degree> [<graphfile>]")
        print("    Creates graph from the points in <pointfile>")
        print("    by connected each point with its <degree> closest neighbors.")
        print("    If <graphfile> is not specified, the graph is written")
        print("    to standard output.")
        sys.exit()

    in_file = open(argv[1], "r", encoding="utf_8")
    pts = point_utils.read_points(in_file)
    in_file.close()

    degree = int(argv[2])

    if len(argv) >= 4:
        out_file = open(argv[3], "w", encoding="utf_8")
    else:
        out_file = sys.stdout

    create_graph(pts, degree, out_file)

    if len(argv) >= 4:
        out_file.close()


if __name__ == "__main__":
    main(sys.argv)
