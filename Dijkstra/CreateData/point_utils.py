import random


import point


def generate_points(size, num_points) -> list[point.Point]:
    ''' generate a random list of points'''
    num_generated = 0
    pts = set()
    while num_generated < num_points:
        x = random.randint(0, size)
        y = random.randint(0, size)
        pt = point.Point(x, y)
        if pt not in pts:
            pts.add(pt)
            num_generated += 1
    pts_list: list[point.Point] = list(pts)
    random.shuffle(pts_list)
    return pts_list


def write_points(pts: list[point.Point], out_file):
    ''' write a list of points to the given file '''
    for pt in pts:
        out_file.write(f"{str(pt)}\n")


def read_points(in_file) -> list[point.Point]:
    ''' read a list of points from the given file '''
    pts = []
    for line in in_file:
        pt = point.parse_point(line.strip())
        pts.append(pt)
    return pts
