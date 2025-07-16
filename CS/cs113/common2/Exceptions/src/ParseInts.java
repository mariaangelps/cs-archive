
import java.util.Scanner;
public class ParseInts {
// ParseInts.java
// Reads a line of text and prints the integers in the line.
        public static void main(String[] args) {
            int val, sum = 0;
            Scanner scan = new Scanner(System.in); //input from the keyboard
            String line;
            System.out.println("Enter a line of text: ");

            //scanLine es un object, que lee desde una string que es el scan.nextLine
            Scanner scanLine = new Scanner(scan.nextLine());
            //hasNext significa --> do i have data to read from a keyboard input, something
            //left to read


                while (scanLine.hasNext()) {
                    try{
                    val = Integer.parseInt(scanLine.next());
                    sum += val; //value converted to the sum
                }
                    catch(NumberFormatException e){

                    }


            }

                System.out.println("The sum of the integers on this line is " +
                        sum);
            }


    }