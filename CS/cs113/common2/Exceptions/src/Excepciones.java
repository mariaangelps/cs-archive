public class Excepciones {



    public static void main(String [] args) {
        /*
         Va a dar exception, asi que  creamos una para desviar y el programa
         siga funcionando
        int resultado  = 3/0;
        System.out.println(resultado);

        //Ejemplo de edades
          int edades [] = {15,44,5,64};
          Systout("LA EDAD DE LA POSICION 4 ES: "+ EDADES[4]);
          No existe index 4 solo es hasta 3
         */

        try {
            int resultado = 3 / 0;
            int edades []= {15,44,5,64};


        }
        catch(Exception e){ //typo de Excpetions seguido de un nombre, funciona como un header

            System.out.println("No se puede dividir por cer0");
            System.out.println("Est'as intentando acceder al index 4, y este no existe");
        }
    }
}
