
public class MyMethods1{

  public int add(int num1, int num2){ //header of the method
   
      int sum=num1+num2;
      return sum;
  
   }
   
   //rollTwo method---> takes two Die object parameters, rolls both and returns the smallest face
   
   public int rollTwo(Die d1,Die d2){
   
      d1.roll();
      d2.roll();
   
      if (d1.getFaceValue() < d2.getFaceValue()) //face of first die is smaller than other)
         return d1.getFaceValue();//first die's face
         
      else
         return d2.getFaceValue();//second die's face
   
   }




















}