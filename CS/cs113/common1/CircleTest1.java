import java.util.Scanner;
import java.util.Random;

public class CircleTest1{
public static void main (String[] args){

//circle 1
Scanner scan = new Scanner(System.in);
System.out.println("Enter the value of the radius");
int c1Radius = scan.nextInt();
Circle2 c1= new Circle2 (c1Radius);

//circle 2

Random random = new Random();
int randRadius = random.nextInt(11)+5;
Circle2 c2 = new Circle2 (randRadius);

//Print Area

System.out.println("Area of circle 1 is: " + c1.area());
System.out.println("Area of circle 2 is: " + c2.area());

//swap the radii

int swapRadii = c1.getRadius();
c1.setRadius(c2.getRadius());
c2.setRadius(swapRadii);

//Print
System.out.println("Circle 1:  "+ c1.toString());
System.out.println("Circle 2:  "+ c2.toString());




}



}