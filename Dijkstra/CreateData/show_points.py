import sys


from graphics import *
import point_utils


def show_points(in_file, size):
    margin = 10
    window_size = 600
    win = GraphWin("Points",
            window_size + 2 * margin,
            window_size + 2 * margin)
    win.setCoords(-margin, -margin,
            window_size + margin,
            window_size + margin)
    pts = point_utils.read_points(in_file)
    if size == None:
        x_max = max(pts, key = lambda pt : pt[0])
        y_max = max(pts, key = lambda pt : pt[1])
        size = max(x_max, y_max)
    for pt in pts:
        x = (pt.x / size) * window_size
        y = (pt.y / size) * window_size
        Circle(Point(x, y), 2).draw(win)
    win.getMouse()
    win.close()


def main(argv):
    if len(argv) < 2:
        print("usage: show_points <pointfile> [<size>]")
        print("    Display the points in <pointfile> in")
        print("    a 600x600 window, mapped as <size>x<size>.")
        sys.exit()

    in_file = open(argv[1], "r")
    if len(argv) > 3:
        size = None
    else:
        size = int(argv[2])
    show_points(in_file, size)
    in_file.close()


if __name__ == "__main__":
    main(sys.argv)
