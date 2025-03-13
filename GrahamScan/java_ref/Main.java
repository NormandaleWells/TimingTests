import java.io.FileInputStream;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Scanner;

public class Main {
    
    private static ArrayList<Point> readPoints(String filename) throws IOException {
        ArrayList<Point> pts = new ArrayList<Point>();
        FileInputStream ptsFile = new FileInputStream(filename);
        Scanner sc = new Scanner(ptsFile);
        while (sc.hasNextLine()) {
            String line = sc.nextLine();
            line = line.strip();
            if (line.length() == 0) continue;
            if (line.charAt(0) == '#') continue;
            Point pt = Point.parsePoint(line);
            pts.add(pt);
        }
        ptsFile.close();
        return pts;
    }

    public static void main(String[] args) throws IOException {

        if (args.length < 1) {
            System.out.println("usage: java main <infile> [<outfile>]");
            System.exit(0);
        }

        String inFile = args[0];
        String outFile = "";
        if (args.length > 1) {
            outFile = args[1];
        }

        ArrayList<Point> pts = readPoints(inFile);
        ArrayList<Point> hull = Graham.graham(pts);
        System.out.println(hull);
    }
}
