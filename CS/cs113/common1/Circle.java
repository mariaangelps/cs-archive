
//Question 2 hw 
//Maria Angel Palacios Ssrmiento -3158891


public class Circle{

    private Point center;
    private int radius;

    //default constructor
    public Circle(Point center, int radius){
       this.center=center;
       this.radius=radius;
        }
     //getter method for Center
     public Point getCenter() {
        return center;
    }
    //setter method for Center
    public void setCenter(Point newCenter) {
        center = newCenter;
    }
    //getter method for Radius
    public double getRadius() {
        return radius;
    }
    //setter method for Radius
    public void setRadius(int newRadius) {
        radius = newRadius;
    }

    //boolean condition
    public boolean equals(Circle otherCircle) {
        return this.radius ==otherCircle.radius;  
          }
    public double circumference() {
        return 2 *radius *  Math.PI;
    }
    
    public String toString() {
        return "The Circle center is: "+ center + ", and" + " the radius is "+ radius;
    }
    
}