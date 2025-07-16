public class CiclosForAnidados {


public static void main(String[]args){


       //cuando se lo hace desde el beginning
    // String[][]cities=new String[4][2];//8 elementos
       String [] androidVersiones = {"Apple pie","Banana Bread","Cupcake","Donut"};

        for(int i=0;i<androidVersiones.length;i++){
            System.out.println("Este es el index  ->" +i);
            System.out.println("En el index: "+i+" se tiene: "+androidVersiones[i]);
            //seria lo mismo que lo de abajo
            // System.out.println(androidVersiones[0]);
            //         System.out.println(androidVersiones[1]);
            //         System.out.println(androidVersiones[2]);
            //         System.out.println(androidVersiones[3]);
        }



        System.out.println();
        System.out.println();

    //ciclo for para las ciudades

    String[][] cities = {{"Mexico,CDMX"},{"Mexico,Guadalajara"},{"Colombia,Bogota"},{"Colombia,Medellin"}};

    /**
     *primer for se refiere para ir por rows, o sea cada fila
     *segudno for va a ir por cada columna
     */
    for(int i=0;i<cities.length;i++){
        for (int j = 0; j < cities[i].length; j++) {
            System.out.println("Este es el index de fila: "+ i + " y el index de columna: " + j + " -->"+cities[i][j] );

        }

    }




        }
        }
