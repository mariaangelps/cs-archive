//Maria Angel Palacios Sarmiento - 31589951
//Homework #2

import java.util.Scanner; 

public class NameApp{
   public static void main(String[] args){
   
   Scanner scan= new Scanner(System.in);
   
   
   
   System.out.println("Enter your first name: ");
   String name=scan.next();
   System.out.println("Enter your last name: ");
   String lastName=scan.next();
   
   
   //Convert the Initials to Uppercase and take the first char of the string
   
   System.out.print("Initials: " + name.toUpperCase().charAt(0));
   System.out.println(lastName.toUpperCase().charAt(0));
   
   //Calculate the length of the name and last name together
   String totalLength= name+lastName;
   System.out.print("The total length is: " + totalLength.length());
    
  
   
   
   
   
   
   
   
   
   
   
   }



}