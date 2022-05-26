/* Author Norman Bernardi
   CIT-130
   3/4/22
   Circle Class
*/
package Figure;
public class Circle extends Figure {
   int radius;
   public Circle(){
      super(0,0,"none");
      setRadius(0);
   }
   public Circle(String n, int a, int b, int r){
      super(a,b,n);
      setRadius(r);
   }
   public String toString(){
      return "In Circle Drawing "+getName()+" centered at ("+getX()+","+getY()+") radius " + getRadius();
   }
   public void erase(){
      System.out.println("In Circle erasing");
   }
  public void draw(){
      center();
      erase();
      System.out.println(""+this);
   }
   public void setRadius(int r){radius = r;}
   public int getRadius(){return radius;}

    
    }
