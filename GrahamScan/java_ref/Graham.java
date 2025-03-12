import java.util.ArrayList;
import java.util.Comparator;

public class Graham {
    
    // Collections.min returns an object, not an index.
    // We need the index.
    private static int minPoint(ArrayList<Point> pts) {
        Comparator<Point> comp = Point.getYXComparator();
        int minIdx = 0;
        for (int i = 1; i < pts.size(); i++) {
            if (comp.compare(pts.get(i), pts.get(minIdx)) < 0) {
                minIdx = i;
            }
        }
        return minIdx;
    }

    private static int ccw(Point pt1, Point pt2, Point pt3) {
        int dx21 = pt2.x() - pt1.x();
        int dy31 = pt3.y() - pt1.y();
        int dy21 = pt2.y() - pt1.y();
        int dx31 = pt3.x() - pt1.x();
        return dx21 * dy31 - dy21 * dx31;
    }

    public static ArrayList<Point> graham(ArrayList<Point> origPts) {
        
        int minIdx = minPoint(origPts);
        Point p0 = origPts.get(minIdx);

        // There's probably a faster, more Java-ish way to do this.
        ArrayList<Point> pts = new ArrayList<Point>(origPts);
        pts.remove(minIdx);
        pts.sort(Point.getAngleDistanceComparator(p0));

        var hull = new ArrayList<Point>();
        hull.add(p0);
    
        for (Point pt : pts) {
            int np = hull.size();
            while ((hull.size() > 1) && (ccw(pts.get(np-2), pts.get(np-1), p0) <= 0)) {
                hull.removeLast();
            }
            hull.add(pt);
        }
        return hull;
    }

    public static void main(String[] args) {
        ArrayList<Point> pts = new ArrayList<Point>();
        pts.add(new Point(-1, 0));
        pts.add(new Point(1, 1));
        pts.add(new Point(0, -1));
        pts.add(new Point(1, 0));
        ArrayList<Point> hull = graham(pts);
        System.out.println(hull);
    }
}
