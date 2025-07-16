import java.util.Scanner;
public class Sales {
 // ***************************************************************
 // Sales.java
// Reads in and stores sales for each of 5 salespeople.  Displays
// sales entered by salesperson id and total sales for all salespeople.
//
    // ***************************************************************
        public static void main(String[] args)
        {
            final int SALESPEOPLE = 5;
            int[] sales = new int[SALESPEOPLE];
            int sum;
            Scanner scan = new Scanner(System.in);
            for (int i=0; i<sales.length; i++)
            {
                System.out.print("Enter sales for salesperson " + i + ": ");
                sales[i] = scan.nextInt();
            }
            System.out.println("\nSalesperson  Sales");
            System.out.println(" ------------------ ");
            int average=0;
            sum = 0;
            int max = 0;
            int min= sales[0];
            for (int i=0; i<sales.length; i++)
            {
                System.out.println("     " + (i+1) + "         " + sales[i]);
                sum += sales[i];
                average = sum / sales.length ;
            }
            for(int i=0;i<sales.length;i++) {

                if (sales[i] > max) {
                    max = sales[i];
                }
            }
            for (int i=0;i<sales.length;i++){
                if(sales[i]<min){
                    min = sales[i];

                }
            }


            System.out.println("\nTotal sales: " + sum);

            System.out.println("\nTotal average: " + average);
            System.out.println("\nTotal max: " + max);
            System.out.println("\nTotal min: " + min);
            System.out.println("\n Enter a Random Value: ");
            int val = scan.nextInt();
            int people = 0;


            for(int i=0;i<sales.length;i++)
            {
                if(sales[i]>val){
                    people+=1;
                    System.out.println("Id number: "+ i + ", number of sales:" + sales[i] ) ;
                    System.out.println("People in total: " +  people) ;

                }

            }


        }

    }

