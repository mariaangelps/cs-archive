//Maria Angel Palacios Sarmiento-31588891
//HW5-10-18-2023

package common2;

import java.util.Scanner;

public class TestDog {
    public static void main(String[]args){
         int dogAges = 0;

        Scanner scan = new Scanner(System.in);
        System.out.println("Number of Dogs in the kennel: ");
        int num = scan.nextInt();

        Dog dog = new Dog(0,"");//dog we dont care about
        
        
        for(int x=1;x<=num;x++){ //le pongo esto porque a numdogs, le doy el parametro de num
         scan.nextLine();
         System.out.println("Enter Dog breed:");
         String breed=scan.nextLine();
         
        
         System.out.println("Enter age::");
         int age=scan.nextInt();
         dogAges+=age;
         
         Dog a = new Dog(age,breed);
         //System.out.println(dogAges);para ver que la variable global si funciona
         boolean c=a.compareTo(dog)>0;
         if(c){
         dog=a;
         System.out.println(dog.getBreed());
         
         }
         
        }
        
        double average = dogAges/num;
        System.out.println(average);
        System.out.println(dog.toString());
         
         
         }
         }
      
      






      
        









    


