//Maria Angel Palacios Sarmiento
//31588891
//Homework 7

import java.util.Arrays;//libreria

public class TestArrays1 {
    
    
    //Question 1 
   public static int []salesRange(int[][] sales) {
        int greatest = sales[0][0]; //400 
        int lowest = sales[0][0]; // 150 
      for (int row = 0 ; row<sales.length;row++){ // rows 
      for(int col = 0 ; col<sales[row].length;col++) { 
         if(sales[row][col]<lowest) { 
         lowest = sales [row][col]; 
         } 

      if(sales[row][col]>greatest) { 
         greatest = sales[row][col]; }
            }
         } int [] results = {lowest, greatest, (greatest-lowest) }; 
         return results; 
         } 

    
    //Question 2 
    
    public static int[] dieStats(Die[][] dice) {
        int[] count = new int[dice.length];
        
        for (int row = 0; row < dice.length; row++) {
            int count1 = 0; // Initialize the count for the current row
            for (int col = 0; col < dice[row].length; col++) {
                dice[row][col].roll();
                if (dice[row][col].getFaceValue() % 2 == 1) {
                    count1++; // Increment the count for odd face values in the current row
                }
            }
            count[row] = count1; // Store the count in the array
        }
        return count;
    }

    
    
    //main method
    
    
    public static void main(String[] args) {
        
        
        //TESTING NRO 1 
         int[][] sales = { {200,150},{350,375},{400,225}};
          int[] results1 = TestArrays1.salesRange(sales); 
         System.out.println("["+results1[0]+","+results1[1]+","+results1[2]+"]"); 
  


   //TESTING NRO 2 
        Die Dice = new Die();
        Die[][] sales1 = new Die[2][3];
        
        for(int i=0;i<2;i++)
         {
            for(int j=0;j<3;j++)
                sales1[i][j] = Dice;
         }
        
        int [] result= new int [2];
        result = dieStats(sales1);
        
        
        for(int i=0;i<2;i++) {
             System.out.printf("Face Values: "+ " " + result[i]);
             }
        
        
        
    }
    

}
