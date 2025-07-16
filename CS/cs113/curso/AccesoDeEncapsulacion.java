package curso;

public class AccesoDeEncapsulacion{

public static void main(String[]args){

   MethodsAccesores valores = new MethodsAccesores();


        valores.setEdad(10);
        System.out.println("la edad es: "+valores.getEdad());
        valores.setNombre("Maria");
        System.out.println("Tu nombre es: "+valores.getNombre());



}


}