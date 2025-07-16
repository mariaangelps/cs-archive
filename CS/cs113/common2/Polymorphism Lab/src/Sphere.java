public class Sphere extends Shape {
    private double radius;  //radius in feet

    //----------------------------------
    //  Constructor: Sets up the sphere.
    //----------------------------------
    public Sphere(double r) //no le ponen el nombre porque ser'ia redundqar a preguntar por el nombre de la esfera
    {
        super("Sphere"); //calling the shape constructor with the parameter
        radius = r;
    }
    //-----------------------------------------
    //  Returns the surface area of the sphere.
    //-----------------------------------------

    //override the method
    public double area() {
        return 4 * Math.PI * radius * radius;
    }

    //-----------------------------------
    //Returns the sphere as a String.
    //-----------------------------------
    public String toString() {
        return super.toString() + " of radius " + radius;
    }

}
