import java.util.Scanner;


public class DemoScanner {
    

    public DemoScanner(){
        //Scanner con String
        Scanner scan /*scan es la variable */ = new Scanner(System.in);
        System.out.print("Cual es tu nombre: ");
        String name=scan.nextLine();//lee toda esa linea
        System.out.println(" hola como est'as " + name);
        
        //Scanner con Int-o un nro
         System.out.println("Dame un numero del 1 al 5");
        int numero=scan.nextInt();
        System.out.println(numero+ " ser'a tu lucky day");


    }

    public static void main(String[]args){
        new DemoScanner();


    }
}
