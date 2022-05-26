/* author Norman Bernardi
   CIT-130
   3/18/22
   Counter Driver Code
*/
package Counter;
import Counter.*;
import java.util.Scanner;
public class counterTest {
   public static void main(String[] args) throws InterruptedException {
      Scanner kbd = new Scanner(System.in);
      counterController contr1 = new counterController();
      int startValue = 0;
      int endValue = 0;
      System.out.println("-----Counter Test Program-----");
      while(true) {
         System.out.println("Enter a start value: ");
         startValue = kbd.nextInt();
         kbd.nextLine();
         System.out.println("Enter a end value: ");
         endValue = kbd.nextInt();
         kbd.nextLine();
         try {
            contr1.counterController(startValue, endValue);
            Thread.sleep(500);
         }
         catch (InterruptedException e) {
            System.out.println(e);
         }
         System.out.println("Continue? (y)es/(n)o: ");
         Character answer = kbd.next().charAt(0);
         answer = Character.toUpperCase(answer);
         if (answer.equals('N')) {
            System.out.println("Program will now close.");
            break;
         }         
      }
   }
}


