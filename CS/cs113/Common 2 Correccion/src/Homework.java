public class Homework {
    private int score;
    public Homework(int score){
        this.score =score;
    }
    public boolean equals(Homework other){
        return this.score == other.score;
    }
    public void setScore(int score){
        this.score = score;
    }
    public int getScore(){
        return score;
    }
    public String toString(){
        return "HW: "  + Integer.toString(score);
    }








}
