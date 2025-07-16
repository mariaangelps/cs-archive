import java.util.Random;

public class RollingDice{

   public static void main(String[] args){
   
   int die1,die2,totalRoll;
   
   Random generator = new Random();
   
   die1= generator.nextInt(7)+1;
   die2= generator.nextInt(7)+1;
   totalRoll= die1+die2;
  
  System.out.println("die 1: " +die1+ "die2: "+die2 +"=" + totalRoll);







   }
   
   
   
   
 }