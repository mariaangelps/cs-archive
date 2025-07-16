public class DieProg{

public static void main(String[] args){

 Die die1 = new Die(); //ESTO ES CREAR A NEW OBJECT ---> The Constructor aqu'i es Die, es un default porque no tiene parameters 
 Die die2 = new Die(2); //esto es un nodefault constructor, el 2 es el start value 
 //Die die2.setFaceValue(2);//Incorrecto
 
 
 
 die1.roll();
 die2.roll();
 
 System.out.println(die1.getFaceValue()+ ", " + die2.getFaceValue()); // pedirle que me de el numero de caras del dado
 die1.setFaceValue(5);
 die1.setFaceValue(1);
 System.out.println(die1+ ", " + die2.toString());
 
 
 
 
 









      }
}





