
from io import TextIOWrapper
import sys
from typing import Any

from graham import graham
from point import Point


def read_points(filename: str) -> list[Point]:
    pts_file: TextIOWrapper = open(filename, "r")
    pts: list[Point] = []
    for line in pts_file:
        if len(line) == 0: continue
        if line[0] == "#": continue
        fields = line.strip().split(',')
        if len(fields) != 2:
            print(f"Invalid input: {line.strip()}")
            sys.exit()
        pt: Point = Point(int(fields[0]), int(fields[1]))
        pts.append(pt)
    return pts


def write_points(pts: list[Point], filename: str = "") -> None:
    ''' Write a list of points to a file.
    
    If filename is a blank string, stdout is used.
    '''
    if filename != "":
        pts_file: Any = open(filename, "w")
    else:
        pts_file = sys.stdout

    for pt in pts:
        pts_file.write(f"{str(pt)}\n")

    if filename != "":
        pts_file.close()


def main() -> None:
    if len(sys.argv) == 1:
        print("usage: main <filename>")
        sys.exit()
    pts: list[Point] = read_points(sys.argv[1])
    hull = graham(pts)
    write_points(hull)


if __name__ == "__main__":
    main()
