import java.util.Scanner;
import java.util.Random;

public class Etest{

public static void main(String[] args){

//car1
Random rand = new Random();
int randNumber = rand.nextInt(51)+250;
E car1 = new E(randNumber,"Tesla Model S");


//car2

Scanner scan = new Scanner (System.in);
System.out.println("Enter the range: ");
int car2Range = scan.nextInt();
scan.nextLine();
System.out.println("Enter the model: ");
String car2Model = scan.nextLine();
E car2 = new E(car2Range,car2Model);

//print

  int comparisonResult=car1.compareTo(car2);

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





