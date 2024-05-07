'''
    generate_points.py

    Program to generate a list of random points.
'''
import sys


import point_utils


def main(argv):
    ''' main function '''
    if len(argv) < 3:
        print("usage: generate_points <size> <numpoints> [<filename>]")
        print("    generates <numpoints> points in a grid of <size> by <size>")
        print("    if specified, the points are written to <filename>,")
        print("    otherwise they are written to stdout")
        sys.exit()

    size = int(argv[1])
    num_points = int(argv[2])
    if len(argv) >= 4:
        out_file = open(argv[3], "w", encoding="utf_8")
    else:
        out_file = sys.stdout

    pts = point_utils.generate_points(size, num_points)
    point_utils.write_points(pts, out_file)

    if len(argv) >= 4:
        out_file.close()


if __name__ == "__main__":
    main(sys.argv)
