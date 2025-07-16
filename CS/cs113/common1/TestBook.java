//Maria Angel Palacios Sarmiento-3158891
//HOMEWORK #4


package common1;
import java.util.Scanner;



public class TestBook{

    public static void main(String[]args){

        
                Book object1 = new Book();
                Book object2 = new Book();
                Scanner scan = new Scanner (System.in);


                String firstBook,secondBook;
                int numPages1,numPages2;
                
                System.out.println("Please enter the Title of the first Book: ");
                firstBook = scan.nextLine();
                System.out.println("Please enter the number of pages of the First Book: ");
                numPages1=scan.nextInt();
                
                object1.setBookTitle(firstBook);
                object1.setPageNumber(numPages1);
                
               /*Consumes my newline character,porque sin este,
                se va a seguir saltando la linea*/

                scan.nextLine();
                
                System.out.println("Please enter the Title of the second Book: ");
                secondBook= scan.nextLine();
                
                 
                 
                System.out.println("Please enter the number of pages of the Second Book: ");
                numPages2=scan.nextInt();

              
                object2.setBookTitle(secondBook);
                object2.setPageNumber(numPages2);
                
               
                System.out.println(object1);
                System.out.println(object2);
                
                System.out.println("The average number of the pages of the two books is: " +(object1.getPageNumber()+object2.getPageNumber())/2.0);
  
  }


    }
    

 