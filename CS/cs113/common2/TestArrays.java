//Homework 6
//Maria Angel Palacios Sarmiento


import java.util.Random;
import java.util.Scanner;
import java.util.Arrays;

public class TestArrays {

//Frequences numbers

    public static int[] numberFreq() {
        Random rand = new Random();
        int[] frequence = new int[6]; // Array to store frequencies of numbers 0 to 5

        for (int index = 0; index < frequence.length; index++) {
            int integer = rand.nextInt(6); // Generate a random number between 0 and 5
            frequence[integer]++; // Increment the corresponding frequency
        }

        return frequence;
    }

//Fibonacci Numbers Problem
    
    public static int[] fibo(int total){
            int [] totalFibonacciNumbers = new int[total];
            for(int index=2;index<totalFibonacciNumbers.length;index++){
                totalFibonacciNumbers[0]=1;
                totalFibonacciNumbers[1]=1; 
                totalFibonacciNumbers[index]= totalFibonacciNumbers[index-1]+totalFibonacciNumbers[index-2];
        }
        return totalFibonacciNumbers;
    }
    
    
    //Die Problem 

      public static int oddDice(Die[] dice) {
        int count = 0;
        for (Die die : dice) {
            die.roll();
            if (die.getValue() % 2 == 1) {
                count++;
            }
        }

        return count;
    }
    
    
    //Testing:
    
    
public static void main(String[] args){

   //Question 1:

    int[] frequence = numberFreq();
    System.out.println("The Number of Frequencies for each number is:");
    for (int index = 0; index< frequence.length; index++) {
        System.out.println("Num: " + index + ": " + frequence[index]);
    }

    // Question 2: 
         Scanner scan = new Scanner(System.in);
       System.out.print("Enter the total number of Fibonacci numbers: ");
        int totalFibo = scan.nextInt();
        int[] fibonacciNumbers = fibo(totalFibo);
        System.out.println("Fibonacci numbers: " + Arrays.toString(fibonacciNumbers));

    // Question 3: Dados 
    System.out.print("Enter the number of dice you are going to play with: ");
    int numberOfDice = scan.nextInt();
    Die[] diceArray = new Die[numberOfDice];

        for (int i = 0; i < numberOfDice; i++) {
        diceArray[i] = new Die();
    }

    int oddDiceCount = oddDice(diceArray);
    System.out.println(oddDiceCount + " dice have an odd face:)");
    scan.close();
    }
    }