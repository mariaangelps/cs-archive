/*MIDTERM PRACTICE 2 */

public class EV{

    private int range;
    private String model;


//default constructor, here we inicialismos nuestra data.
public EV(int r, String m){
    range=r; //--> r solo existe aqu'i dentro del default contsructo
    model=m;
}

public void setRangeNumber(int newRange){ //setter are voids ACUERDATE
     range =newRange;
}

//getter for range
public int getRange(){
    return range;
}
//getter for Model
public String getModel(){
    return model;
}

//toString method

public String toString (){ //el toString significa que: este permite que se produzca una string en vez del address del string. 
    String x="-->This is the model of the car";
    String y="-->This is the range of the car";

    return model + x + range + y;
    //o tb se puede poner return "Model"+model+",Range" +range;
}

public int compareTo (EV other) {/*--> siempre va a ser 1 PARAMETRO, preguntar si es que yo le pongo aqui un: outside, abajo ir'ia
range> outside.range???
*/
    if(range>other.range) {//if my range, as'i se lee  {
        return 1;
    } 

    else if (range== other.getRange()){
        return 0;
    }
    else return -1;
}

public boolean sameModel(EV other){
    if (model.equals(other.model))
    return true;
    else return false;

}
   
}
    





/*A constructor that accepts parameters and creates an EV object with the specified range and model.
 A getter method for each instance data.
 A setter method for the range (only).
 A toString method that returns the car’s model and range.
 A compareTo method that compares two electric cars and returns 1 if first car has higher range than
other car, 0 if the ranges are the same and -1 otherwise.
 A method sameModel that compares two cars and returns true if they have same model and false
otherwise. */