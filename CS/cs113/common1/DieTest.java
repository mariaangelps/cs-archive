package common1;
public class DieTest{
   public static void main (String[] args){
   //instaniate default Die object with face 3
   Die d1= new Die();
   //instaniate default Die object with face 3
   Die d2= new Die();
   //System.out.println (d1+ "\n" + d2);~ prints out the address
   //prints facevalue
   System.out.println (d1.getFaceValue()+ ", " + d2.getFaceValue()); // valor de 3 set antes
   //rolls both die objects and print face values
   d1.roll();
   d2.roll();//we get the random values
   System.out.println (d1.getFaceValue()+ ", " + d2.getFaceValue());
   //change the value of Second die object to 5
   d2.setFaceValue(5);
   //print information about both Die objects
   System.out.println (d1.getFaceValue()+ ", " + d2.getFaceValue());
   System.out.println (d1+ ", " +d2); //same System.out.println (d1+ ", " +d2.toString());
   


   
   }
}   
   
   //Die()~ call to the default constructor
   //Die(2)~ call to the non default constructor,it has a parameter
   //value of D2~D2 is an object, reference variable, address