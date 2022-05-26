/* Author Kenneth Moore
`  CIT-130
   3/4/22
   Figure Class
*/
package Figure;

public abstract class Figure{
   private int X, Y; // the center of the object.
   private String name;
   private static int numberOfShapes=0;  
    
   public Figure(){
      X = 0;
      Y = 0;
      name = "none";
   }
   public Figure(int a, int b, String n){
      setX(a);
      setY(b);
      setName(n);
      numberOfShapes++;
   }
   public void setX(int a){X = a;}
   public void setY(int b){Y = b;}
   public void setName(String n){name = n;}
   public int getX(){return X;}
   public int getY(){return Y;}
   public String getName(){return name;}
   public static int getNumberOfShapes(){return numberOfShapes;}
   public abstract void erase();
   public abstract void draw();
   public void center(){
      System.out.println("\nIn Figure. Centering at ("+getX()+","+getY()+")");
    }
}
