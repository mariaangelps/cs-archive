//Maria Angel Palacios

class Circle{

    private Point center;
    private int radius;

    //default constructor
    public Circle(Point Center, int radius){
        center=c;
        radius=r;}
        
     //getter method for Center
     public Point getCenter() {
        return center;
    }
    //setter method for Center
    public void setCenter(Point newCenter) {
        center = newCenter;
    }
    //getter mthod for Radius
    public double getRadius() {
        return radius;
    }
    //setter method for Radius
    public void setRadius(int newRadius) {
        radius = newRadius;
    }

    //boolean condition
    public boolean equals(Circle num) {
        if(radius == (num.getRadius())) {
            return true;}
        else {
            return false; }
    }
    public String toString() {
        return center.toString() + "is the Circle center, and" + " the radius is "+ radius;
    }
    public double circumference() {
        return 2 *radius *  Math.PI;
    }
    
}