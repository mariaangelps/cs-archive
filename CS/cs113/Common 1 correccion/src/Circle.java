public class Circle {
    private  Point center;
    private double radius;

    public Circle(Point center, double radius){
        this.center=center;
        this.radius=radius;
    }
    public Point getCenter(){
        return center;
    }
    public void setRadius( double radius){
        this.radius =radius;
    }
    public boolean liesOnCircle(Point p){
        if(this.radius==p.distance(center)){
            return true;

        }
        else{
            return false;
        }
}
}