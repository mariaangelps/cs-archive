package common1;

public class DemoMetodos{
    //default constructor, doesnt return value 
    public DemoMetodos(){
        sumaNumeros();
        sumaNumeros(10.0,30.0);
        
        divisionNumerosReturn();
        double result= divisionNumerosReturn();
        System.out.println(result);

        divisionNumerosReturn("Hola Mari, si soy yo",6.9,9.6);
        String fraseCompleta= divisionNumerosReturn("Hola Mari, si soy yo",6.9,9.6);
        System.out.println(fraseCompleta);
        
    }

    public void sumaNumeros(){
        
        double a= 20.0;
        double b=10.0;
        double result;
        result= a+b;
        System.out.println(result);
    }

    public void sumaNumeros(double a, double b){ //sobrecarga de metodo sumaNumeros
        double result;
        result = a+b;
        System.out.println(result);
    }

    /*si me va a dar un valor, utilizando return*/
     public double divisionNumerosReturn(){
        double a = 100.5;
        double b= 20.1;
        double result=a/b;
        return result;
     }

     public String divisionNumerosReturn(String fraseCompleta, double a, double b){
        double result=a/b;
        return fraseCompleta + result;

     }

    public static void main(String[] args){
            new DemoMetodos(); //metodo constructor, siempre el metodo se pone con public dentro del main







    }
}