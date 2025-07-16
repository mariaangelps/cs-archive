public class Circle3{

private Point center;
private double radius;

//constructor

public Circle3(Point center, double radius){
this.center=center;
this.radius=radius;

}

//getter for the center 

public Point getCenter(){
return center;
}

//setter for the radius
public void setRadius(double radius){
this.radius = radius;
}

//liesOnCircle method

public boolean liesOnCircle(Point targetPoint){
// tb puede ser as'i :
//if(targetPoint.distance(targetPoint.getCenter())==radius){
if (targetPoint.distance(center)==radius);{
return true;
}
else{
return false;}

}


}


//Question 12
import java.util.Scanner;

public class CircleTest{


public static void main(String[] args){

final int SIZE = 50; //constant 

Circle3[] arr = new Circle3[SIZE];

Scanner scan = new Scanner(System.in);

Point obj = new Point(0,0);
int count =0;
for(int i=0; i<array.length<i++)
//coordinates
int x = scan.nextInt();
int y = scan.nextInt();

//radius
int radius = scan.nextInt();

arr[i] = new Circle(new Point(x,y), scan.nextInt());
if (arr[i].liesOnCircle(obj))
count++;
}
System.out.println(count);




}



}


//Practice 3


//Question 11 

public class Student{
private String name;
private GPA gpa;

//constructor
public Student(String name, GPA gpa){

this.name = name;
this.gpa =gpa;
}

//getter for gpa
public GPA getGpa(){
return gpa;
}
//setter for name
public void setName(String name){
this.name=name;
}
//honorRoll method

public boolean honorRoll(GPA otherGpa){
if(gpa.compareTo(otherGpa)>=0){
return true;
}
else{ return false;}
}

//toString
public String toString(){
return gpa + name;
}


}
//question 12

public double[]bestInMonths (double[][]famCellBills){

int numRows = famCellBills.length;
int numColumns = famCellBills[0].length;

double[] BestBill = new double[numColumns];
for(int j=0; j<numColumns; j++){
double lowestBill = Double.MAX_VALUE;
for(int i = 0; i<numRows; i++){
if(lowestBill>famCellBills[i][j]){
lowestBill=famCellBills[i][j];
bestBill[j] = lowestBill;
}
return bestBill;
}


}


