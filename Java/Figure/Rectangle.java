/* Author Norman Bernardi
   CIT-130
   3/4/22
   Rectangle Class
 */
package Figure;

public class Rectangle extends Figure {
   int length, height;
   public Rectangle(){
      super(0,0,"none");
      setLength(0);
      setHeight(0);
   }
   public Rectangle(String n, int a, int b, int w, int h){
      super(a,b,n);
      setLength(w);
      setHeight(h);
   }
   public String toString(){
      return "In Rectangle Drawing "+getName()+" centered at ("+getX()+","+getY()+") length "+getLength()+" height "+getHeight();
   }
   public void erase(){
      System.out.println("In Rectangle erasing");
   }
  public void draw(){
      center();
      erase();
      System.out.println(""+this);
   }
   public void setLength(int l){length = l;}
   public void setHeight(int h){height = h;}
   public int getLength(){return length;}
   public int getHeight(){return height;}

}
