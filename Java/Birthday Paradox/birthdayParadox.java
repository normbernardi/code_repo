/* Author Norman Bernardi
   4/23/22
   CIT-130
   Monte Carlo Birthday
*/
import java.util.*;
public class birthdayParadox
{
   public static void main(String[] args)
   {
      System.out.println("Probability : " + birthdayCalc(10, 100000));
      System.out.println("Probability : " + birthdayCalc(20, 100000));
      System.out.println("Probability : " + birthdayCalc(30, 100000));
      System.out.println("Probability : " + birthdayCalc(40, 100000));
      System.out.println("Probability : " + birthdayCalc(50, 100000));
      System.out.println("Probability : " + birthdayCalc(60, 100000));
      System.out.println("Probability : " + birthdayCalc(70, 100000));
      System.out.println("Probability : " + birthdayCalc(80, 100000));
      System.out.println("Probability : " + birthdayCalc(90, 100000));
      System.out.println("Probability : " + birthdayCalc(100, 100000));
   }
   
   public static float birthdayCalc(int people, int test)
   {
      int collision = 0;
      int j = test;
      
      while (--j >= 0)
      {
         Random rand = new Random();
         Set<Integer> BdayList = new HashSet<>(365);
         
         for (int i = 0; i < people; i++)
         {
            int rBday = rand.nextInt(365);
            if (BdayList.contains(rBday))
            {
               collision++;
               break;
            }
            BdayList.add(rBday);
         }
      }
      System.out.println("Across " + test + " tests there were " + collision + " shared brithdays in a group of " + people + " people.");
      return (float)collision / (float)test;
   }
}

     
      
         