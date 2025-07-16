/*Write an application TestEV that creates 2 EV car objects. 
One of the cars should be of the model “Tesla Model S” with a random range between 250 and 300, inclusive. 
The other car should have a model and range entered from the keyboard.
The program prints to the screen the information about the car with the longest range. 
If the cars have the same range, print “same”. Also, the program should print whether they are 
of the same model. */

import java.util.Random;
import java.util.Scanner;
public class TestEV1{

  public static void main (String[]args){
    Random rand = new Random();
    int randomRange = rand.nextInt(250,301);
    EV1 car1 = new EV1(randomRange,"Tesla Model S");


    Scanner scan = new Scanner(System.in);
    System.out.println("Enter the range of your car: ");
    int range;
    String model;
    range = scan.nextInt();
    scan.nextLine();
    System.out.println("Enter the model of your car: ");
    model= scan.nextLine();
    EV1 car2 = new EV1(range,model);

    //compare Ranges 

   int longestRange = car1.CompareTo(car2);
    if(longestRange==1){
      System.out.println(car1);}
      else if(longestRange==0){
        System.out.println("Same Range");
      }
      else{
        System.out.println(car2);
      }

    //compare Models
    if(car1.sameModel(car2)){
      System.out.println("Both cars have the same Model:)");
    }
    
  }



}
