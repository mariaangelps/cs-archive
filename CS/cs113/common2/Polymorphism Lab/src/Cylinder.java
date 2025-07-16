public class Cylinder extends Shape {
    private double height;
    private double radius;
    public Cylinder(double height, double radius)
    {
        super("Cylinder:");
        this.height = height;
        this.radius = radius;
    }

    @Override
    public double area() {
        return Math.PI*radius*Math.pow(2, height);
    }

    public String toString(){
        return super.toString() + "wth height: " + height + "radius: " + radius + ", and area: " ;
    }
}
