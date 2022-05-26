/* author Norman Bernardi
   CIT-130
   3/18/22
   Towers of Hanoi Implementation
*/
import java.util.*;
import java.io.*;
import java.math.*;
class towerOfHanoi {
   static void towerOfHanoi (int n, char from_rod, char to_rod, char aux_rod) {
      if (n == 0) 
      {
         return;
      }
      towerOfHanoi(n - 1, from_rod, aux_rod, to_rod);
      System.out.println("Moving disk " + n + " from tower " + from_rod + " to tower " + to_rod);
      towerOfHanoi(n - 1, aux_rod, to_rod, from_rod);
   }
   public static void main(String[] args) {
      Scanner kbd = new Scanner(System.in);
      int disk = 0;
      System.out.println("-----Tower of Hanoi-----");
      while (true) {
            System.out.println("Enter the amount of disks in play: ");
            disk = kbd.nextInt();
            break;
            }
      towerOfHanoi(disk, 'A', 'B', 'C');
   }
}
            
            
               
   