public class Die {
    private int value;

    public Die() {
        // Constructor to initialize the die with a default value
        roll();
    }

    public void roll() {
        // Simulate rolling the die by generating a random value between 1 and 6
        value = (int) (Math.random() * 6) + 1;
    }

    public int getFaceValue() {
        // Retrieve the current value of the die
        return value;
    }
}