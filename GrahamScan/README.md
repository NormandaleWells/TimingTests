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

Each test should have a function called `graham()`
which takes an array of points,
and returns an array of points describing the
convex hull for the input point array.
The `point` datatype is undefined here;
that may be one of the things being tested.
(For example, the `python_ref` test has a Point class,
while the `python_point_as_tuple` test uses a
tuple to define the points.)

The input file names have the formats
```
test_<size>_<numpoints>.input.txt
test<n>.input.txt
```
where `<size>` is the range of the data (from 0..size
in both x and y), `<numpoints>` is the number
of points in the input, and `<n>` is simply a test
number.  The first format is used for timing tests,
while the second is used for functionality tests.

There are also files containing the expected output
for each test.  These have names in the form
```
test_<size>_<numpoints>.expected.txt
```
where `<size>` and `<numpoints>` are defined as above.

For both input and output files,
the points are given one per line in integer coordinates,
in the format
```
(<x>,<y>)
```
where `<x>` and `<y>` are the x and y coordinates
respectively of the point.  The parentheses are
required, and no, I do not rememeber why I chose
to do it that way.

The input files may also include blank lines,
and comment lines starting with `#`.