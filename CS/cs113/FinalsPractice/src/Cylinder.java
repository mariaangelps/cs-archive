
//Recalling that: Area of a Cylinder:   2*pi^r^2 + 2pi*r*h



public class Cylinder extends Circle{
    double height;

    public Cylinder(double height,double radius){
        super(radius);
        this.height = height;

    }

    public double getHeight(){
        return height;



    }
    public void setHeight(double h){
        this.height = height;


    }

    public boolean equals(Cylinder other) {
        if (this.radius == other.radius && this.height == other.height) {
            return true;
        }
	else{
                return false;
            }


        }

        public double Area() {
           return 2 * super.area() + 2 * Math.PI * radius * height;

        }

        public String toString () {

            return "Cylinder has radius of : " + radius + "and height of " + height;


        }


    }







