public class Circle2{
	private int radius;

public Circle2(){
radius=1;
}

public Circle2(int r){
radius = r;
}

public int getRadius(){
	return radius;
}

public void setRadius(int newRadius){
	radius = newRadius ;
}

public String toString(){
	return "The radius is:" +radius;
}
public double area(){
	return Math.PI * radius *radius;
}


}

