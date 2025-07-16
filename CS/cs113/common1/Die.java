package common1;

public class Die{
   
   
  //Esto es un visibility modifier, como es private, it enforces encapsulation,
  // doesnt provide services to clientts en el method
  //--> cuando hay este se necesitan accessor and mutator ethods to access the dta 
  //pedirle a java que lo guarde, que lo esconda practicamente--> esto ser'ia como los attributes del dibujo
  private int faceValue; 
  
  
  // default constructor--> initialize your data just to 3, CONSTRUCTORS DO NOT NEED A RETURN TYPE
  //SIEMPRE EL CONSTRUCTOR tiene MISMO NOMBRE de la CLASE
  
  public Die(){ //si quiero poner un random numero, pongo faceValue=math.random(;
       
     faceValue=3;
       }
       
  //nondeFault constructor 
  
  
  public Die(int newVal){
   faceValue=newVal; //funciona como un scan scanner, donde se le pide al usuario que ingrese 
  
  }
  
  //Method roll, no parameters porque se sobrentiende
  public void roll(){
   faceValue=(int)(Math.random()*6)+1; //generates 1 to 6 integer (1 al 6, tomandolo en cuenta al 6
  }
  
  //getter method---> return the value of the private instance data, it doesnt change, just RETURN
  public int getFaceValue(){
      return faceValue;
 }

  //setter method ---> this method will work on the data from the private class
  public void setFaceValue(int newFace){
      faceValue=newFace;
      
   }   
  
  //// we want to compare the internal faces of this die and otherDie
  public boolean equals(Die otherDie){
  
      return faceValue==otherDie.getFaceValue(); //this is a comparison of integers 
      //Alternate solution: return faceValue=otherdie.faceValue;
  }
  
  //one die parameter
  public int compareTo(Die otherDie){
   //method should be returning a 0,a posiitive, or negative number
   
      if (faceValue==otherDie.getFaceValue()){
         return 0;
      }
         
      else if(faceValue>otherDie.getFaceValue()){
       
         return 1;
      }
      else{
         return -1;
      }
       
       
   
  }
  
  
  public String toString(){
      return "Die with facevalue equal to = " + faceValue;
      
   }   // it will only return a string
      
      
//toString will give me the name of the method
  //public String toString(){//doesnt take parameteres 
  }
  

  
      
       
      

    
     
      
