public class Dados{
      private int die1, die2;
    //default constructor
    public Dados(int d1, int d2){
        die1= d1;
        die2=d2;
    }

    //setter for Dado1 face
    public void setDadosFace(int newDadosFace){
        die1= newDadosFace;}

    //getter for dado 1 face
    public int getDadosFace1(){
        return die1;
    }
    //getter for dado 2 face
    public int getDadosFace2(){
        return die2;
    }
   
    //toString Method
    public String toString(){
        return "The face of Die1 is: "+die1+", the face of die 2 is: "+die2;
    }
    }

