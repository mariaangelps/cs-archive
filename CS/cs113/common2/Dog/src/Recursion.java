public class Recursion {
    /*5Implement a recursive method that takes as parameters a String s and an integer i and returns a String that
     has s repeated i times. For example, if the given string is "MATH 111" and the integer is 3 then the return
     valuewould be " MATH 111 MATH 111 MATH 111". (Note that if the integer is 0, then the empty string
     "" should be returned.

     */

    public static String repeatedString (String s, int i) {
        //base case
        if(i<=0){
            return"";
        }
        else{

        }



        //general case
        return repeatedString(s,i-1)+ " " +s;
    }

    /* 3. Implement a recursive method printDigits that takes an integer num as a parameter and prints its digits in
reverse order, one digit per line*/

    public static void printDigits(int num){
        //base case
        if(num<10){
            System.out.println(num);
        }
        //general case
        else{
            System.out.println(num%10);
            printDigits(num/10);
        }

    }



    public static void main(String[]args){
        printDigits(2574);
        repeatedString("Hola",45);
    }
}
