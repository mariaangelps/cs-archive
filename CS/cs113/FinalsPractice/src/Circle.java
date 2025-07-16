public class Circle {
    protected double radius;
    public Circle(double radius){
        this.radius = radius;
    }

    public void setRadius(double radius){
        this.radius = radius;

    }

    public double getRadius(){
        return radius;
    }
    public double area(){
        return Math.PI*radius*radius;
    }
    public String toString(){
        return "tHIS IS A CIRCLE WITH RADIUS " + radius;
    }
}
