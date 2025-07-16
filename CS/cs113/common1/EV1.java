public class EV1{
    int range;
    String model;

    //constructor
    public EV1(int range, String model){
        this.range=range;
        this.model=model;
    }
    //getter method

    public String getModel(String model){
        return model;
    }

    public int getRange(){
        return range;
    }

    public void setRange(int newRange){
        range = newRange;
    }

    public String toString(){
        return "The car's model is: " + model + ", the car range is: " +range;   }

    public int CompareTo(EV1 other){
        if (range>other.range){
            return 1;
            }
        else if (range==other.getRange()){
            return 0;
            }   
        else return -1;   }

    

    public boolean sameModel(EV1 other){
        if(model.equals(other.model)){
            return true;}
            
            else{
                return false;

            }
        }
    }






