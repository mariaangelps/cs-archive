//Maria Angel Palacios Sarmiento
//Homework 4 
//Writing methods Question 1
package common1;
public class MyMethods {


    public int volume(int width,int length, int height){

        int result= length*width*height;
        return result;

    }

    public double avgFaceValues(Die die1, Die die2){

        double result;
        result= (die1.getFaceValue() + die2.getFaceValue())/2.0;
        return result;
        


    }


    
}
