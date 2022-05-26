/* author Norman Bernardi
   CIT-130
   3/18/22
   counterModel Class File
*/
package Counter;
import Counter.*;
public class counterModel {
   private int counter;
   public void counterModel(int initialValue) {
      counter = initialValue;
   }
   public void Increment() throws InterruptedException {
   counterView counterView = new counterView();
      try {
         Thread.sleep(1000);
         counter += 1;
         counterView.Display(counter);
      }
      catch (InterruptedException e) {
         System.out.println(e);
      }
   }
}