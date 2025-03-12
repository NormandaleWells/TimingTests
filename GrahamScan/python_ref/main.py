
from io import TextIOWrapper
import sys
import time
from typing import Any

from graham import graham
from point import Point
from point import parse_point


def read_points(filename: str) -> list[Point]:
    pts_file: TextIOWrapper = open(filename, "r")
    pts: list[Point] = []
    for line in pts_file:
        line = line.strip()
        if len(line) == 0: continue
        if line[0] == "#": continue
        pt = parse_point(line)
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
