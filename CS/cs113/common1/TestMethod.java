//Maria Angel Palacios Sarmiento-3158891
//Homework #4 Test method question 1


package common1;

public class TestMethod {
    

    public static void main(String[]args){

       MyMethods object = new MyMethods();
       int totalVolume=object.volume(2,3,4);
       System.out.println(totalVolume+" Corresponds to the final Volume.");


       Die die1= new Die(3);
       Die die2=new Die(4);
       die1.roll();
       die2.roll();
       double avgFaceValues =object.avgFaceValues(die1,die2);
     System.out.println(avgFaceValues+" Corresponds to the Average Face Value");
        
        
        
    }
}
