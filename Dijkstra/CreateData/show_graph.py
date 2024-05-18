import sys


from graphics import *
import point_utils
import point


def read_lines(in_file):
    lines = []
    for line in in_file:
        fields = line.strip().split()
        pt1 = point.parse_point(fields[0])
        pt2 = point.parse_point(fields[1])
        lines.append((pt1, pt2))
    return lines


def convert_point(pt, size, window_size):
    x = (pt.x / size) * window_size
    y = (pt.y / size) * window_size
    return Point(x, y)


<<<<<<< HEAD
def show_graph(in_file_name: str, size: int) -> None:
    margin = 10
    window_size = 800
    win = GraphWin(in_file_name,
            window_size + 2 * margin,
            window_size + 2 * margin)
    win.setCoords(-margin, -margin,
            window_size + margin,
            window_size + margin)
    in_file = open(in_file_name, "r")
    lines = read_lines(in_file)
    in_file.close()
    if size == None:
        x_max = max(lines, key = lambda l : max(l[0].x, l[1].x))
        y_max = max(lines, key = lambda l : max(l[0].y, l[1].y))
        size = max(x_max, y_max)
    for line in lines:
        pt1 = convert_point(line[0], size, window_size)
        pt2 = convert_point(line[1], size, window_size)
        Line(pt1, pt2).draw(win)
    win.getMouse()
    win.close()


def main(argv):
    if len(argv) < 2:
        print("usage: show_points <pointfile> [<size>]")
        print("    Display the points in <pointfile> in")
        print("    a 600x600 window, mapped as <size>x<size>.")
        sys.exit()

    if len(argv) > 3:
        size = None
    else:
        size = int(argv[2])
    show_graph(argv[1], size)


if __name__ == "__main__":
    main(sys.argv)
