public class StudentMidterm2P3 {
    private GPA gpa;
    private String name;
    public StudentMidterm2P3(GPA gpa, String name){
        this.gpa =gpa;
        this.name = name;
    }

    public GPA getGpa(){

        return this.gpa;
    }

    public void setName(String name){
        this.name=name;
    }

    public boolean honorRoll(GPA other) {
        if(this.gpa.compareTo(other.getValue())>=0) {
            return true;
        } else {
            return false;
        }
    }


    public String toString(){
            return name+gpa;}






    }