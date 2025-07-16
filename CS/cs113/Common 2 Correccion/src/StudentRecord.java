public class StudentRecord {
    private Homework hw1;
    private Homework hw2;
    //constructor
    public StudentRecord(Homework hw1, Homework hw2){
        this.hw1 = hw1;
        this.hw2 = hw2;
    }

    public Homework getHw1(){
        return hw1;
    }
    public void setHw2(){
        this.hw2 = hw2;
    }
    public boolean equals(StudentRecord other){
        if(hw1.equals(other.hw1)&& hw2.equals(other.hw2)){
            return true;
        }
        else{
            return false;
        }

    }

    public void applyIncentive(){
        int difference = hw2.getScore() - hw1.getScore();
        if(difference>=16){
            hw1.setScore(hw1.getScore()+difference/2);
        }
    }
    public String toString(){
        return hw1+"," +hw2;
    }




}
