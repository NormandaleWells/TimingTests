import java.util.Comparator;

record Point(int x, int y)
{
    @Override
    public String toString() {
        return String.format("(%d,%d)", this.x, this.y);
    }

    public double angleTo(Point pt) {
        int dx = pt.x - this.x;
        int dy = pt.y - this.y;
        return Math.atan2(dy, dx);
    }

    public int manhattanDistance(Point pt) {
        return Math.abs(pt.x - this.x) + Math.abs(pt.y - this.y);
    }

    private static class CompareYX implements Comparator<Point> {

        @Override
        public int compare(Point pt1, Point pt2) {
            if (pt1.y < pt2.y) return -1;
            if (pt1.y > pt2.y) return  1;
            if (pt1.x < pt2.x) return -1;
            if (pt1.x > pt2.x) return  1;
            return 0;
        }
        
    }

    private static class CompareAngleDistance implements Comparator<Point> {

        private Point ptRef;
        public CompareAngleDistance(Point ptRef) {
            this.ptRef = ptRef;
        }

        @Override
        public int compare(Point pt1, Point pt2) {
            double angle1 = ptRef.angleTo(pt1);
            double angle2 = ptRef.angleTo(pt2);
            if (angle1 < angle2) return -1;
            if (angle1 > angle2) return  1;

            int dist1 = ptRef.manhattanDistance(pt1);
            int dist2 = ptRef.manhattanDistance(pt2);
            if (dist1 < dist2) return -1;
            if (dist1 > dist2) return  1;

            return 0;
        }
        
    }

    public static Comparator<Point> getYXComparator() {
        return new CompareYX();
    }

    public static Comparator<Point> getAngleDistanceComparator(Point ptRef) {
        return new CompareAngleDistance(ptRef);
    }

    public static Point parsePoint(String s) {
        if (s.charAt(0) != '(') {
            throw new RuntimeException("parsePoint: does not start with '('");
        }
        if (s.charAt(s.length()-1) != ')') {
            throw new RuntimeException("parsePoint: does not end with ')'");
        }
        String[] fields = s.substring(1, s.length()-1).split(",");
        if (fields.length != 2) {
            throw new RuntimeException("Invalid point format");
        }
        int x = Integer.parseInt(fields[0]);
        int y = Integer.parseInt(fields[1]);
        return new Point(x, y);
    }
}
