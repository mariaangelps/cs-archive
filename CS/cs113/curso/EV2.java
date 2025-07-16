

public class EV2{
   private int range;
   private String model;
   
   
   //constructor, default constructor

   public EV2(int r, String m){
   
      range=r;
      model=m; }
   
         
   //setter method for range
   
   public void setRange(int newRange){
      range=newRange;
      }

   //A getter method for range.
   
   public int getRange(){
      return range;
      }
   
   //A getter method for model
   public String getModel(){
      return model;
      }

   
   //A toString method that returns the car’s model and range.
   public String toString(){
      return "model"+model+"range:" +range;
      }
      
    
    // A compareTo method that compares two electric cars and returns 1 if first car has higher range than other car, 0 if the ranges are the same and -1 otherwise.

   public int compareTo(EV2 other){
   if(range>other.range){
      return 1;
      }
      
     else if (range==other.getRange()){
      return 0;
      }
      
      else{ 
      return -1;
      }
      }
   //A method sameModel that compares two cars and returns true if they have same model and false otherwise
   
   public boolean sameModel(EV2 other){
   if (model==other.model){
      return true;}
      
    else{
      return false;
      }
    }
      
 
   
   
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 }