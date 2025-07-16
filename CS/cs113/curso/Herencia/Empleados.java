public class Empleados extends Persona{

//Atributos propios
int num_archivo;
String cargo;
Double sueldo;
//constructor vacio
public Empleados(){
    }

//herencia


public Empleados(int id, String dni, String nombre, String apellido, String domicilio, String telefono, int num_archivo,
        String cargo, Double sueldo) {
    super(id, dni, nombre, apellido, domicilio, telefono);
    this.num_archivo = num_archivo;
    this.cargo = cargo;
    this.sueldo = sueldo;
}

public int getNum_archivo() {
    return num_archivo;
}


public String getCargo() {
    return cargo;
}

public Double getSueldo() {
    return sueldo;
}

public void setNum_archivo(int num_archivo) {
    this.num_archivo = num_archivo;
}

public void setCargo(String cargo) {
    this.cargo = cargo;
}

public void setSueldo(Double sueldo) {
    this.sueldo = sueldo;
}










}