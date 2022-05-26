/* author Norman Bernardi
   CIT-130
   3/18/22
   counterController Class File
*/
package Counter;
import Counter.*;
public class counterController {
   private int startValue;
   private int endValue;
   public counterController() {
      startValue = 0;
      endValue = 0;
   }
   public void counterController(int startValue, int endValue) throws InterruptedException {
      counterModel count1 = new counterModel();
      count1.counterModel(startValue);
      Start();
      try {
         for (int i = 0; i < endValue; i++) {
            count1.Increment();
         }
      }
      catch (InterruptedException e) {
         System.out.println(e);
      }
   }
   public void Start() {
      System.out.println("Counter starting.");
   }
}