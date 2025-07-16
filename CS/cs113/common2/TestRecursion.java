// HOMEWORK 08 
//Maria Angel Palacios Sarmiento -3158891

public class TestRecursion {
    // Problem 1

    public static void printDigits(int num) {
        if (num < 10) { //base case
            System.out.println(num);
        } else {
            printDigits(num / 10);
            System.out.println(num % 10);
        } 
    }
     //Problem 2
    
     public static int sumArray(int[]numArray,int count){
     
            if(count <= 0 || count > numArray.length){ //base case
            return 0;
            }
            else{
               return numArray[count-1]+ sumArray(numArray,count -1);

            }
     }

     //test
      public static void main(String[] args) {
        // Problem 1:
        printDigits(123147);
        //Problem2:
        int[]a ={1,3,2,5};
        System.out.println(sumArray(a,3));
        System.out.println(sumArray(a,4));
    }
  

}











   