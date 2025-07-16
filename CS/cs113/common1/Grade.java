public class Grade{


private int numGrade;
private char letterGrade;

public Grade(int g){

numGrade=g;
if (g>=65){
letterGrade = 'S';
}
else{ 
letterGrade = 'U';
}
}

   //getter numgrade
   public int getNumGrade(){
      return numGrade;
   }
   
   //getter letterGrade
   public char getLetterGrade(){
      return letterGrade;
      }
      
   //setter letterGrade
   public void setLetterGrade(char newLetter){
      letterGrade = newLetter;
      }
      
   //toString
   public String toString(){
      return "Score: " + numGrade + ", Letter Grade: " + letterGrade;
      }
      
    //isSatisfactory
    
    public boolean isSatisfactory(){
      return letterGrade == 'S';
      }
      
    //equals
    
    public boolean equals(Grade other){
    
    
    if(letterGrade==other.letterGrade){
    return true;}
    else{
    return false;}
    }
   
   
 







}














