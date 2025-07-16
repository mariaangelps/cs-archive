//MARIA ANGEL PALACIOS SARMIENTO -31589951
//HOMEWORK 2 


import java.util.Random;

public class RandomPlate{

   public static void main(String[] args){
   
   Random plateNumber= new Random();
   
   int firstLetter,secondLetter,thirdLetter,fourthLetter,fifthLetter;
   int digit1,digit2;
   
  
   
	firstLetter = 'A' + plateNumber.nextInt(26);
	secondLetter = 'A'+ plateNumber.nextInt(26);
	thirdLetter = 'A'+ plateNumber.nextInt(26);	
   fourthLetter = 'A'+ plateNumber.nextInt(26);
   fifthLetter = 'A'+ plateNumber.nextInt(26);		

	//convert to int the digits 
	digit2 = (int)(Math.random() * 10);
   digit1 = (int)(Math.random() * 10);
	
	System.out.println(""+(char)(firstLetter) + ((char)(secondLetter)) + ((char)(thirdLetter)) + ((char)(fourthLetter))+ ((char)(fifthLetter))+ digit1 + digit2 );
   
   
   
   
   
   
   
   
   
   
   
   }













   }
   