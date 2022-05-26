/* @author Norman Bernardi
2/25/22
CIT-130
Shallow Wrapper Class
*/
package WrapperTest;
import java.util.Arrays;


public class WrapperShallow{

   private int[] a = new int[3];

   //default constructor   
   public void WrapperShallow() {
       a[0] = 0;
       a[1] = 0;
       a[2] = 0;
   }
   
   
      public void getArray() {
      for (int i = 0; i < a.length; i++) {
         System.out.print(a[i] + " ");
      }
   }
   
   //override constructor
   public void setArray(int i, int j, int k) {
      a[0] = i;
      a[1] = j;
      a[2] = k;
   }
   
   //copy constructor
   public void WrapperShallow(WrapperShallow ws) {
      a = ws.a;
   }

   //toString method
   public String wrapperToString() {
      return Arrays.toString(a);
   }
   
   // equals method
   public boolean wrapperEquals(WrapperShallow ws) {
       return ws.a == a;
   }
}
