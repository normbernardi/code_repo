/* Author Norman Bernardi
   CIT-130
   3/23/22
   MyMathClass Class for pkg Standard Deviation
*/
package StandardDeviation;
import java.lang.Math;
import java.util.ArrayList;
public class MyMathClass 
{
   public static <T extends Number> double stdev(ArrayList<T> a, double average)
   {
      double total = 0;
      for (T num : a)
         {
            total += Math.pow((num.doubleValue() - average), 2);
         }
      return Math.sqrt(total / (a.size() - 1));
   }
   public static <T extends Number> double getAvg(ArrayList<T> arr)
   {
      double total = 0;
      for (int i = 0; i < 10; i++)
         total += arr.get(i).doubleValue();
      return total / 10;
   }
}
   
         
         
   
