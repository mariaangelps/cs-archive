// ****************************************************************
// Labrador.java
//
// A class derived from Dog that holds information about
// a labrador retriever. Overrides Dog speak method and includes
// information about avg weight for this breed.
//
// ****************************************************************
public class Labrador extends Dog{ 
private String color; //black, yellow, or chocolate?
private static int breedWeight = 75;
public Labrador(String name, String color)
{
    super(name); //RULE SIEMPRE SIEMPRE ESTO, Y DEBE SER ANTES DE LOS OTROS ATRIBUTOS
    this.color = color;

}
// ------------------------------------------------------------
// Big bark -- overrides speak method in Dog, ; LO PONE EN MAYUSUCLAS AL WOOF 
// ------------------------------------------------------------
public String speak()
{
return "WOOF"; 
}
// ------------------------------------------------------------
// Returns weight --> Static no pueden devolver instance data 
// breedweigth es no static, por eso ahora lo cambio arriba al int breedwifgth a private static int breedweight 
//o simplemente ponerlos a los dos no ponerlos nonstatic, o sea object type, por lo tanto le quito static abajo

// ------------------------------------------------------------
//igual se le quita el static
public int avgBreedWeight()
{
return breedWeight;
}
}

