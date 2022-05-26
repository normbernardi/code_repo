import java.util.*;
public class testHash
{
  public static void main(String[] args)
  {
       // Do 100,000 tests on 10 persons.
       System.out.println(birthDayExperiment(10, 100000));
  }

  public static float birthDayExperiment(int person, int test)
  {
      int count = 0;
      int j = test;

      while(--j >= 0) {
          Random random = new Random();
          Set<Integer> birthdays = new HashSet<>(365);

          for(int i = 0; i < person; i++) {
             int tmp = random.nextInt(365);
             if (birthdays.contains(tmp)) { count++; break; }
             birthdays.add(tmp);
          } 
      }

      return (float)count / (float)test;
   }
}