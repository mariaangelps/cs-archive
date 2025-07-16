//Question 2 hw 
//Maria Angel Palacios Sarmiento -3158891


import java.util.Random;
import java.util.Scanner;
class CircleTest {

    public static void main(String[] args) {
       Scanner scan = new Scanner(System.in);
        Random randomnum = new Random();
        int x1 = randomnum.nextInt(25)+1;
        int y1 = randomnum.nextInt(25)+1;
        Point p1 = new Point(x1, y1);
        Point p2 = new Point(0,0);
        System.out.println("Please, insert the number for the radius: ");
        
        int radius = scan.nextInt();

        Circle c1 = new Circle(p1,radius);
        Circle c2 = new Circle(p2,5);
        
        System.out.println(c1.toString());
        System.out.println(c2.toString());

        if(c1.equals(c2)) {
            System.out.println(p1.distance(p2)+" -> That is the total distance between the circles.");
        }
        else {
            double averageCircumference = (c1.circumference() + c2.circumference())/2.0;
            System.out.println("The value of the Average Circumference: is " + averageCircumference);

        }
        scan.close();
    }

}
