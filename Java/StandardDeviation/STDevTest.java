/* Author Norman Bernardi
   CIT-130
   3/23/22
   Test program for pkg Standard Deviation
*/
package StandardDeviation;
import java.util.ArrayList;
public class STDevTest
{
   public static void main(String[] args)
   {
      double excelConstant = 3.0276503541;
      ArrayList<Double> arrD = new ArrayList<Double>();
      ArrayList<Integer> arrI = new ArrayList<Integer>();
      for (int j = 1; j <= 10; j++)
      {
            arrD.add(Double.valueOf(j));
            arrI.add(j);
      }
      System.out.print("Double and Integer array set to: ");
      for (int i = 0; i < arrD.size(); i++)
         System.out.print(arrD.get(i));
      System.out.println("\nAverage for Double: " + MyMathClass.getAvg(arrD) + "\nAverage for Integer: " + MyMathClass.getAvg(arrI));
      System.out.println("Standard Deviation for Double ArrayList: " + MyMathClass.stdev(arrD, (MyMathClass.getAvg(arrD))));
      System.out.println("Standard Deviation for Integer ArrayList: " + MyMathClass.stdev(arrI,(MyMathClass.getAvg(arrI))));
      System.out.println("From Excel: " + excelConstant);
   }
}

      