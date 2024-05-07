'''
    show_graph

    Program to display a graph created by create_graph.
'''
import sys

from typing import Tuple


import graphics
import point


def read_lines(in_file) -> list[Tuple[point.Point, point.Point]]:
    ''' Read the lines from the given file. '''
    lines = []
    for line in in_file:
        fields = line.strip().split()
        pt1 = point.parse_point(fields[0])
        pt2 = point.parse_point(fields[1])
        lines.append((pt1, pt2))
    return lines


def convert_point(pt: point.Point, size: int, window_size: int) -> graphics.Point:
    ''' Convert the given point to a graphics point'''
    x = (pt.x / size) * window_size
    y = (pt.y / size) * window_size
    return graphics.Point(x, y)


def show_graph(in_file, size: int) -> None:
    ''' Display the graph stored in 'infile' '''
    margin = 10
    window_size = 800
    win = graphics.GraphWin("Points",
            window_size + 2 * margin,
            window_size + 2 * margin)
    win.setCoords(-margin, -margin,
            window_size + margin,
            window_size + margin)
    lines: list[Tuple[point.Point, point.Point]] = read_lines(in_file)
    for line in lines:
        pt1 = convert_point(line[0], size, window_size)
        pt2 = convert_point(line[1], size, window_size)
        graphics.Line(pt1, pt2).draw(win)
    win.getMouse()
    win.close()


def main(argv: list[str]) -> None:
    ''' main function '''
    if len(argv) < 3:
        print("usage: show_points <pointfile> <size>")
        print("    Display the points in <pointfile> in")
        print("    a 600x600 window, mapped as <size>x<size>.")
        sys.exit()

    in_file = open(argv[1], "r", encoding="utf_8")
    size = int(argv[2])
    show_graph(in_file, size)
    in_file.close()


if __name__ == "__main__":
    main(sys.argv)
