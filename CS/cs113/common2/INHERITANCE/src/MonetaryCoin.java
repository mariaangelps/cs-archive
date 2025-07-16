import java.util.Random;
public class MonetaryCoin extends Coin {
    /*
    Store an int value in the monetary coin that represents its value in cents (1-100, inclusive), add getter and
    setter methods for the monetary value as well as a toString method (override) to return the monetary value and face.
     */

    private int cents;

    public MonetaryCoin() {
        super();
        Random random = new Random();
       this.cents = random.nextInt(100) + 1;
    }

    //getter
    public int getValue() {
        return cents;
    }
    //setter

    public void setValue(int cents) {
        this.cents = cents;
    }

    //override method
    public String toString() {
        String faceName;
        if(isHeads()) {
            faceName = "HEADS";
        }
        else{
            faceName = "TAILS";
        }
        return cents + faceName;
    }
}

