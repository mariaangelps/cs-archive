// Question 12 Practice 3
public class Student1{
    private String name;
    private GPA gpa;
    //constructor
public Student1(string name, GPA gpa){
    this.name = name ;//attribute of name
    this.gpa = gpa; //significa my gpa
}
public GPA getGpa(){
    return gpa;
}
public void setname(String name){
    this.name =name;
}

public boolean honorRoll(GPA targetGPA){
    if(this.gpa.compareTo(targetGPA)>=0){
        return true;
    
    }
    else{
        return false;
    }

}
public String toString(){
    return this.name+":" +this.gpa;
}



}











