
from io import TextIOWrapper
import sys
import time
from typing import Any

from graham import graham
from point import Point


def read_points(filename: str) -> list[Point]:
    pts_file: TextIOWrapper = open(filename, "r")
    pts: list[Point] = []
    for line in pts_file:
        if len(line) == 0: continue
        if line[0] == "#": continue
        line = line.strip()
        if line[0] != "(":
            raise ValueError("parse_point: does not start with '('")
        if line[-1] != ")":
            raise ValueError("parse_point: does not end with ')'")

        fields = line[1:-1].replace(" ", "").split(',')
        if len(fields) != 2:
            raise ValueError(f"parse_point: {len(fields)} fields found, 2 expected")
        pt: Point = (int(fields[0]), int(fields[1]))
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
        pts_file.write(f"({pt[0]},{pt[1]})\n")

    if filename != "":
        pts_file.close()


def main() -> None:
    if len(sys.argv) == 1:
        print("usage: main <infile> [<outfile>]")
        sys.exit()

    infile:str = sys.argv[1]
    outfile: str = ""
    if len(sys.argv) > 2:
        outfile = sys.argv[2]

    pts: list[Point] = read_points(infile)
    start: float = time.thread_time()
    hull = graham(pts)
    end: float = time.thread_time()

    write_points(hull, outfile)
    print(f"{end-start:.4f}")


if __name__ == "__main__":
    main()
