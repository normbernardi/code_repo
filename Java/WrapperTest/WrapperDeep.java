/* @author Norman Bernardi
2/25/22
CIT-130
Shallow Wrapper Class
*/
package WrapperTest;
import java.util.Arrays;
public class WrapperDeep {
    private int[] b = new int[3];

   //default constructor   
   public void WrapperDeep() {
       b[0] = 0;
       b[1] = 0;
       b[2] = 0;
   }
   
   
      public void getArray() {
      for (int i = 0; i < b.length; i++) {
         System.out.print(b[i] + " ");
      }
   }
   
   //override constructor
   public void setArray(int i, int j, int k) {
      b[0] = i;
      b[1] = j;
      b[2] = k;
   }
   
   //copy constructor
   public void WrapperDeep(WrapperDeep wd) {
      b = new int[3];
    for(int i = 0; i < 3; i++) {
        b[i]=wd.b[i];
        }
   }
   
   //toString method
   public String wrapperToString() {
      return Arrays.toString(b);
   }
   
   // equals method
   public boolean wrapperEquals(WrapperDeep wd) {
        return wd.b == b;
   }
}
