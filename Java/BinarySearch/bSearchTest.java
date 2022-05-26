/* Author Norman Bernardi
   CIT-130
   3/23/22
   Binary Search Test Program
*/
package BinarySearch;
import java.util.*;
import java.io.*;
public class bSearchTest
{
      public static void main(String[] args)      {
         int result = 0;
         String strQuery = "null";
         Scanner kbd = new Scanner(System.in);
         Integer[] intArr = new Integer[15];
         for (int i = 0; i < intArr.length; i++)
            intArr[i] = (i * 2);
         String[] strArr = new String[5];
         strArr[0] = "audi";
         strArr[1] = "bmw";
         strArr[2] = "ford";
         strArr[3] = "chevy";
         strArr[4] = "honda";
         System.out.println("Integer array contains:");
         System.out.println(Arrays.toString(intArr));
         System.out.println("Searching the array for values in range");
         for (int i = -4; i <= 4; i++)
         {
            result = Searches.<Integer>binarySearch(intArr, i);
            if (result == -1)
            {
               System.out.println(i + " is not in the array.");
            }
            else
            {
               System.out.println(i + " is found at index " + result);
            }
         }
         System.out.println("String array contains:");
         Arrays.sort(strArr);
         System.out.println(Arrays.toString(strArr));
         {
            String str = "chevy";
            int car = Searches.<String>binarySearch(strArr, str);
            if (car == -1)
               {
                  System.out.println(str + " is not in the array." );
               }
            else
            {
               System.out.println(str + " is found at index " + car);
            }
      }
   }
}
         
      

            