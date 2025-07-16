public class E{
private int range;
private String model;

//constructor
public E(int r, String m){
range=r;
model = m;
}
//setter
public void setRange(int newRange){
range=newRange;
}
//getterrange
public int getRange(){
	return range;}

//getmodel
public String model(){
	return model; 
}

//toString
public String toString(){
return "Model: " + "Range: " +range;
}

//compareTo method
public int compareTo (E other){
	
	if(range==other.range){	
		return 0;}
else if(range>other.getRange()){
	return 1;}
else{
return  -1;}

}

//sameModel
public boolean sameModel(E other){
if(model.equals(other.model())){
	return true;}
else{
return false; 
} 
}
}

