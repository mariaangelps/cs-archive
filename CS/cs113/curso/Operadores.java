public class Operadores {
    //default constructor
    int valor1=1;
    int valor2=2;

    public Operadores(){
        int result=1+2;

        /* No le pongo -->return result;
        porque The constructor must have no return type.*/

        System.out.println("Operador aritmetico "+result);
        result=result*2;
         System.out.println("Operador aritmetico "+result);

        if(valor1==valor2)
            System.out.println(valor1==valor2);
            
        else System.out.println("Operadores de Relacion: valor 1 es menor a valor 2");
        /*valor1=4;
        System.out.println(valor1); --> resultado seria 4, esto es la mala practica, indentacion */
        
    }

    public static void main(String[] args){ 
        /*void methods cannot return a value 
        por lo tanto si es que yo pongo el return dentro del default constructor
        me va a dar ese error */
        new Operadores();

    }
}
