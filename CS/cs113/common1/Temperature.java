// Maria Angel Palacios Sarmiento - 31589951
// Homework #1

import java.util.Scanner;
import java.lang.Math;
public class Temperature {



   //Question #1
   
   public static void main (String[] args){
   Scanner scan= new Scanner(System.in);
   double tempf;
   double tempc;
   int hour; 
   int min; 
   int sec;
   int seconds;
   
   tempf= 36.5;
   tempc= (tempf-32)/1.8; //Conversion from Fahrenheit to Celsius
   System.out.print("Temp in Fahrenheit: " + tempf + ","+ " Temp in Celsius: " + tempc);
   
   
  
  // Question 2:
  
  
   System.out.print("\nEnter total number of seconds: ");
   seconds= scan.nextInt();
   sec= seconds%60; // Remainder Number of the division between total seconds by 60
   hour= seconds/3600; // Total seconds divided by 3600 seconds that 1 hour has
   min= (seconds%3600)/60; //Remainder seconds divided by 60
  
  
   System.out.print(hour+ " hour, "  + min + " minutes, " + sec + " seconds ");
 
  
  
  }
   
  
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
   
  }
  
    