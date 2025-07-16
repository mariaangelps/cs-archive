import java.util.Scanner;
public class Quizzes {
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        System.out.println("How many questions are in the quiz? ");
        int q = scan.nextInt();
        System.out.println("ENTER THE CORRECT ANSWERS: ");
        int[] key = new int[q];
        System.out.println(key.length);
        int correct = 0;
        int percentage = 0;
        for (int i = 0; i < key.length; i++) {
            key[i] = scan.nextInt();
            correct += 1;
        }
        System.out.println("Enter your answers: ");
        int answers = scan.nextInt();
        for (int i = 0; i < key.length; i++) {
            if (answers == key[i]) {
                percentage = 100;
                System.out.println("You got : " + correct + " answers correct" + ", your grade is: " + percentage);

            }
        }
    }
}


