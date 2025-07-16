public class Circle2{

private radius;

//nondefault
public Circle2(){

   radius=1;
   }
   
   //default
   public Circle2(int radius){
   
   radius=r;
   }
   
   //getter
   public int getRadius(){
      return radius;
      }
   //setter
   public void setRadius(int newRadius){
      radius=newRadius;
      }
      
   //toString 
   public String toString(){
      return "The value of your radius is: " +radius;
      }
      
   //area
   public double Area(){
      return Math.PI*radius*radius;
      }











}