import bisect
import sys


from point_utils import *


def create_edge(idx1, idx2):
    return min(idx1, idx2), max(idx1, idx2)


def check_point(nearest_pts, pts, idx, check_idx, degree, edges):
    ''' Check to see if this point can be added to the list of nearest points.

        Returns True if the point is added, False otherwise
    '''
    dist = distance_between(pts[idx], pts[check_idx])

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


def create_graph(pts, degree, outfile):
    
    # Sort the points by x coordinate.  We don't
    # care about the y coordinates; in fact, we're
    # probably better off keeping the y ordering
    # random for a given x value.
    pts = sorted(pts, key = lambda pt : pt.x)

    # We keep track of the set of edges we've already
    # added so we don't add an edge twice.  Each edge
    # is identified by its start and end vertices,
    # with the smaller vertex first.
    edges = set()

    # For each point, we want to alternate moving
    # one point to the left and one point to the right
    # looking for a point closer than any other point
    # so far.  We can stop moving in a given direction
    # whenever the index hits the end, or the x distance
    # between the point we're processing and the next
    # point in that direction is greater than the
    # farthest of the closest `degree` points.
    for i in range(len(pts)):

        prev = next = i

        # nearest_pts will hold tuples (idx,dist) where
        # idx is the index of one of the degree'th nearest
        # points and dist is the distance to that point
        # from point i
        nearest_pts = []

        # We want to enter the loop with one point already
        # in the list.
        done = False
        while prev != 0 and not done:
            prev -= 1
            if (prev, i) not in edges:
                nearest_pts.append((prev, distance_between(pts[i], pts[prev])))
                edges.add((prev, i))
                done = True

        while not done:
            next += 1
            if (i, next) not in edges:
                nearest_pts.append((next, distance_between(pts[i], pts[next])))
                edges.add((i, next))
                done = True

        while (True):

            # Figure out if we can go left or right.
            max_dist = nearest_pts[-1][1]
            have_enough = len(nearest_pts) == degree
            done_left = prev == 0 or \
                    pts[i].x - pts[prev-1].x > max_dist and have_enough
            done_right = next == len(pts) - 1 or \
                    pts[next+1].x - pts[i].x > max_dist and have_enough

            # If we have enough points, and we can't go either
            # direction, get out now.
            if have_enough and done_left and done_right:
                break

            if not done_left:
                prev -= 1
                if (prev, i) not in edges:
                    check_point(nearest_pts, pts, i, prev, degree, edges)
            if not done_right:
                next += 1
                check_point(nearest_pts, pts, i, next, degree, edges)
            
        for near_pt in nearest_pts:
            idx = near_pt[0]
            dist = near_pt[1]
            outfile.write(f"{pts[i]} {pts[idx]} {dist:.4f}\n")


def main(argv):
    if len(argv) < 3:
        print("usage: create_graph <pointfile> <degree> [<graphfile>]")
        print("    Creates graph from the points in <pointfile>")
        print("    by connected each point with its <degree> closest neighbors.")
        print("    If <graphfile> is not specified, the graph is written")
        print("    to standard output.")
        sys.exit()

    in_file = open(argv[1], "r")
    pts = read_points(in_file)
    in_file.close()

    degree = int(argv[2])

    if len(argv) >= 4:
        out_file = open(argv[3], "w")
    else:
        out_file = sys.stdout

    create_graph(pts, degree, out_file)

    if len(argv) >= 4:
        out_file.close()


if __name__ == "__main__":
    main(sys.argv)
