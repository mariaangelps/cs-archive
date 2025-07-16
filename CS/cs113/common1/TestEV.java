/*Write an application TestEV that creates 2 EV car objects. 
One of the cars should be of the model “Tesla Model S” with a random range between 250 and 300, inclusive. 
The other car should have a model and range entered from the keyboard.
The program prints to the screen the information about the car with the longest range. 
If the cars have the same range, print “same”. Also, the program should print whether they are 
of the same model. */

import java.util.Scanner;
public class TestEV1{

public static void main(String[]args){
    int random=(int)Math.random()*51 +250;//este mat.radnm() me da valores de 0 a 1
    EV1 car1= new EV1(random,"Tesla Model 5");

   
    Scanner scan = new Scanner(System.in);
    System.out.println("Enter range: ");
    int car2Range =scan.nextInt();

    scan.nextLine(); //consume la linea, para que no se se salte la linea

    System.out.println("Enter the model");
    String car2Model = scan.nextLine();
    EV1 car2= new EV1(car2Range,car2Model);



    //Compare two objects
     
     comparisonResult=car1.compareTo(car2);

    if(comparisonResult==1){
    System.out.print(car1);}
    else if (comparisonResult == 0){
    System.out.println("SAME");}
    else {
    System.out.println(car2);
    }


    //print whether they are the same model

    if(car1.sameModel(car2)){
    System.out.println("same model");}
    
    else {
    System.out.println("different models");}

    


}
}