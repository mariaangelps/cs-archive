import java.util.Scanner;
public class ReversingArray {


    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);
        System.out.println("How many values you want to populate the array with: ");
        int size = scan.nextInt();
        int[] values = new int[size];
        System.out.println("Enter the values you want to add: ");
        for (int i = 0; i < values.length; i++) {
            values[i] = scan.nextInt();
            System.out.println("The value for position " + i + " is : " + values[i] + ".");
        }
        for (int i = 0; i < values.length; i++) {
            if(values[0] != values[values.length-1] && values[i] != values[values.length-1 -1]){
                System.out.println("The new value for position " + i + " is : " + values[i] + ".");
            }




        }
    }
}




