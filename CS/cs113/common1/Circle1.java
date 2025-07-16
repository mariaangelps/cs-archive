// ************************************************************
//  Circle.java
//
//  Print the area of a circle with two different radii
// ************************************************************
import java.util.Scanner;

public class Circle1
{
   public static void main(String[] args)
   {
   final double PI = 3.14159;
   System.out.println("Please enter radius: " );
   int radius = scan.nextInt(); 
   Scanner scan = new Scanner(System.in);
    
   
 
   double area = PI * radius * radius;
   double circumference= 2*PI*radius;
   System.out.println("The area of a circle with radius " + radius +
   " is " + area);
   System.out.println("The circumference of a circle with radius " + radius +
   " is " + circumference);
   
   radius = 20;
   area = PI * radius * radius;
   circumference=2*PI*radius;
   System.out.println("The area of a circle with radius " + radius +
   " is " + area);
   System.out.println("The circumference of a circle with radius " + radius +
   " is " + circumference);
   
  

   } 
}
