This directory contains timing tests for the Graham scan algorithm
for find the convex hull of a set of points.

For details on the algorithm,
see https://en.wikipedia.org/wiki/Graham_scan .

After writing the Python version I realized that this is really
just testing the speed of a non-trivial sort in the given
language, since the set of points is sorted by the angle
formed by the point and reference point, and for points
with the same angle, by distance to the reference point.

The main part of the algorithm is O(N),
so the sort dominates the run time.