
/*Metodo constructor o default method:
Se llaman igual que la clase
Construye Objetos
Inicializan Objeto`s
Su nombre va con la mayuscula 
 Por ejemplo: 
 public class Die{
   public Die(){}
}

// Cuando se llama al metodo constructor, se utiliza el new. */


public class HolaMari {
    //default constructor
    public HolaMari(){
        System.out.println("Hola Mari, soy java ji");

    }

    public static void main(String[]args){ //aqui solo estoy llamando al constructor
        new HolaMari();
    }
}



