
package curso;

public class MethodsAccesores {


    //encapsulates the data edad, y la string nombre
    private int edad;
    private String nombre;

    //metodo setter, establecemos la edad, y este siempre va a tener el void, porque no retorna un valor, solo lo establece 
    public void setEdad(int edad){
       this.edad=edad;

    }
    public void setNombre(String nombre){
        this.nombre=nombre;
    }
    //metodo getter, mostramos la edad 
    public int getEdad(){
        return edad;
}

    public String getNombre(){
        return nombre;
    }


}
