'''
    create_graph.py

    Program to create a weighted graph from a file of points.
'''
import bisect
import sys

from typing import Tuple
from typing import TypeAlias

import point_utils
import point

IndexEdge: TypeAlias = Tuple[int,int]
''' type IndexEdge = Tuple[int,int] '''

def create_edge(idx1: int, idx2: int) -> IndexEdge:
    ''' Create a edge '''
    return min(idx1, idx2), max(idx1, idx2)


def check_point(
        nearest_pts: list[Tuple[int,float]],
        pts: list[point.Point],
        idx: int,
        check_idx: int,
        num_needed: int) -> bool:
    ''' Check to see if this point can be added to the list of nearest points.

        Returns True if the point is added, False otherwise
    '''
    dist = point.distance_between(pts[idx], pts[check_idx])

    # If we don't have enough points yet, we just add it.
    if len(nearest_pts) < num_needed:
        bisect.insort(nearest_pts, (check_idx, dist), key = lambda pt_data : pt_data[1])
        return True

    # If this is greater or equal to the last point, then
    # it is not a nearest point.
    if dist >= nearest_pts[-1][1]:
        return False

    # Otherwise we remove the last element (the point with the
    # longest distance) and insert it into the list where it belongs.
    # We also need to remove the edge from the list of edges.
    # Note that this edge has to be one that we added for this
    # vertex; otherwise it would have been ignored before this
    # was called.
    nearest_pts.pop()
    bisect.insort(nearest_pts, (check_idx, dist), key = lambda pt_data : pt_data[1])
    return True


def create_graph(pts: list[point.Point], degree: int, outfile):
    ''' Create a graph '''

    # Sort the points by x coordinate.  We don't
    # care about the y coordinates; in fact, we're
    # probably better off keeping the y ordering
    # random for a given x value.
    pts = sorted(pts, key = lambda pt : pt.x)

    # We need to get an upper bound on the maximum
    # length of an edge.
    x_min: int = min(pts, key = lambda pt : pt.x).x
    y_min: int = min(pts, key = lambda pt : pt.y).y
    x_max: int = max(pts, key = lambda pt : pt.x).x
    y_max: int = max(pts, key = lambda pt : pt.y).y
    max_max_dist = (x_max - x_min) + (y_max - y_min)

    # We keep track of the set of edges we've already
    # added so we don't add an edge twice.  Each edge
    # is identified by the indices of its start and end
    # vertices, with the smaller index first.
    edges: set[IndexEdge] = set()

    # For each vertex, we'll keep track of the number
    # of edges we found for it so far.
    num_vertex_edges: list[int] = [0] * len(pts)

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

        # It would be unusual, but it's possible that
        # we already have enough edges for this vertex,
        # all from vertices to the left of this one.
        num_needed: int = degree - num_vertex_edges[i]
        if num_needed <= 0:
            continue

        # nearest_pts will hold tuples (idx,dist) where
        # idx is the index of one of the degree'th nearest
        # points and dist is the distance to that point
        # from point i.  The list is ordered by distance.
        nearest_pts: list[Tuple[int,float]] = []

        # Until we have num_needed points in our nearest_pts
        # list, we'll take any point independent of its
        # distance from vertex i.
        max_dist: float = max_max_dist

        while True:

            # Each time through this loop we'll try to add one
            # point to the left and one to the right.

            # Note that having enough points does NOT mean we're
            # done!  We may find additional points that are closer
            # than ones we've already found.
            have_enough: bool = len(nearest_pts) == num_needed

            # Once we have at least num_needed new points,
            # we only care about points closer than the
            # farthest one in the list.
            if have_enough:
                max_dist = nearest_pts[-1][1]

            # Figure out if we can go left or right.  Note that
            # once the next point differs in x by more than
            # max_dist, we don't have to check that direction.
            done_left:  bool = prev_idx == 0            or pts[i].x - pts[prev_idx-1].x > max_dist
            done_right: bool = next_idx == len(pts) - 1 or pts[next_idx+1].x - pts[i].x > max_dist

            # If we enough points, and can't go either left or
            # right, we can leave.
            if have_enough and done_left and done_right:
                break

            # This should absolutely not happen unless the degree
            # parameter is absurdly high.  By the time
            # we're out of points to check, we should have
            # enough points and the previous 'if' statment
            # shoud have been true.
            if done_left and done_right:
                raise RuntimeError(f"could not find enough edges for vertex {i}")

            # Since we sorted the pts by their x coordinate, the
            # edge (prev_idx, i) may already be in the edge list, and
            # has already been taken into account in num_vertex_edges.
            if not done_left:
                prev_idx -= 1
                if (prev_idx, i) not in edges:
                    check_point(nearest_pts, pts, i, prev_idx, num_needed)

            if not done_right:
                next_idx += 1
                check_point(nearest_pts, pts, i, next_idx, num_needed)

        # We didn't drop out of the loop until we had num_needed
        # edges, which means this vertex now has degree edges.
        num_vertex_edges[i] = degree

        # Write out these new points, and update the edge counts
        # for the other vertices.  Note that any edges to vertices
        # at lower indices will end up with >degree edges because
        # of this.
        for near_pt in nearest_pts:
            idx = near_pt[0]
            dist = near_pt[1]
            num_vertex_edges[idx] += 1
            edges.add(create_edge(i, idx))
            outfile.write(f"{pt} {pts[idx]} {dist:.4f}\n")


def main(argv):
    ''' main function '''
    if len(argv) < 3:
        print("usage: create_graph <pointfile> <degree> [<graphfile>]")
        print("    Creates graph from the points in <pointfile>")
        print("    by connected each point with its <degree> closest neighbors.")
        print("    If <graphfile> is not specified, the graph is written")
        print("    to standard output.")
        print("    Note that some vertices may end up with more")
        print("    then <degree> incident edges.")
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
