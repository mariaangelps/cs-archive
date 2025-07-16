
package curso;

public class LlamarObjetos {
    
String color;
String marca;
int km;

public static void main(String[]args){
        LlamarObjetos coche1 = new LlamarObjetos(); //coche es el objeto que tiene marca, color e int

        coche1.color="blanco";
        coche1.marca="Toyota";
        coche1.km=38372;
        System.out.println("Tu carro es de marca: "+coche1.color+coche1.marca+coche1.km );

    


}



}
