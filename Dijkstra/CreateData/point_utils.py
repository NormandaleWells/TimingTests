import random


from point import *


def generate_points(size, num_points):
    num_generated = 0
    pts = set()
    while num_generated < num_points:
        x = random.randint(0, size)
        y = random.randint(0, size)
        pt = Point(x, y)
        if pt not in pts:
            pts.add(pt)
            num_generated += 1
    pts = list(pts)
    random.shuffle(pts)
    return pts


def write_points(pts, out_file):
    for pt in pts:
        out_file.write(f"{str(pt)}\n")


def read_points(in_file):
    pts = []
    for line in in_file:
        pt = parse_point(line.strip())
        pts.append(pt)
    return pts
