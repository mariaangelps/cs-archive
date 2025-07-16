import java.util.Scanner;
public class doWhileLoop {
    public static void main(String[] args) {
        int response = 0;
        do{
            System.out.println("Selecciona el nro de opcion deseada:");
            System.out.println("1.Movies:");
            System.out.println("2.Series:");
            System.out.println("3.Salir:");
            Scanner scan = new Scanner(System.in);
            response = Integer.valueOf(scan.nextLine());
             switch(response) {
                 case 0:
                     System.out.println("GRACIAS POR VISITARNOS");
                     break;
                 case 1:
                     System.out.println("Movies:");
                     break;
                 case 2:
                     System.out.println("Series:");
                     break;
                 default:
                     System.out.println("Selecciona una opcion correcta");
             }
             } while (response!=0);
        System.out.println("se termino el programa" +
                "");

        }

    }

