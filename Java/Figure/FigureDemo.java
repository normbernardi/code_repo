package Figure;
import java.util.Scanner;
public class FigureDemo {
    public static void main(String[] args) {
        int i;
        Figure[] figureArr = new Figure[4];
        Rectangle r1 = new Rectangle("rec1", 25, 100, 10, 15);
        Rectangle r2 = new Rectangle("rec2", 30, 75, 15, 20);
        Circle c1 = new Circle("cir1", 22, 45, 50);
        Circle c2 = new Circle("cir2", 33, 54, 25);
        figureArr[0] = r1;
        figureArr[1] = r2;
        figureArr[2] = c1;
        figureArr[3] = c2;
        int numShapes = Figure.getNumberOfShapes();
        for (i = 0; i < numShapes; i++) {
            figureArr[i].draw();
        }
    }
}