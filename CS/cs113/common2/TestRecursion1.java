public class TestRecursion1{

    //method factorial (non-recursive)
    //N! = N*(N-1)*(N-2)*...*2*1
    //el N factorial es factorial abajo
    
    //este metodo no es recursive, porqque no se utiliza el metodo dentro del metodo, (o sea el factorial method)
    public static int factorial(int N){
        int answer = 1; //1 porque es un good atarting para un product

        for(int number = N; number>=1;number--)
            answer*=number;
            return answer;

    }




    //recursive factorial method
    
    public static int factorialRec(int N){
        int answer;
        //handle the base case and the general/recursive case
        if(N==1){
            answer =1;
        }
        else
            answer = N*factorialRec(N-1);

            return answer;
    }








    public static void main(String[] args){
        System.out.println(factorial(5)+" <----Not recursive");
        System.out.println(factorialRec(5)+" ---> Recursive way");


    }














}