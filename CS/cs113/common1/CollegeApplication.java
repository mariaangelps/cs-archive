import java.util.Random;

public class CollegeApplication{
private String name;
private int satScore;
//
public CollegeApplication(int s, String n){
   satScore = s;
   name = n;
}

//getter
public String getName(){
   return name;
   }
   
//getter 
public int getSatScore(){
   return satScore;
   }
   
//retakeSAT



public void retakeSAT(){

Random rand = new Random();
int random = rand.nextInt(1601);

   }
 
public void name(String newName){
   name=newName;   
   }
//
public void setSatScore(int newScore){
   satScore = newScore;
   }

//toString

public String toString(){
   return "CollegeApplication: { Name = " + name + ", Sat Score = " +satScore;
   }
   
//compareTo
public int compareTo(CollegeApplication other){

if(satScore <other.satScore){
return -1;}
else if(satScore==other.getSatScore()){
return 0;}
else{
return 1;}
}

}
   
   
   
   








