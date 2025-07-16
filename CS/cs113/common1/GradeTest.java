import java.util.Scanner;
import java.util.Random;

public class GradeTest {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter your score: ");
        int entryScore = scanner.nextInt();

        Grade entry = new Grade(entryScore);
        Random random = new Random();
        int totalHigherGrades = 0;

        while (true) {
            int randomScore = random.nextInt(61) + 40;
            Grade randomGrade = new Grade(randomScore);

            if (randomGrade.equals(entry)) {
                System.out.println(randomGrade);
            } else {
                break;
            }
        }

        while (true) {
        int randomScore = random.nextInt(61) + 40;

            if (randomScore > entryScore) {
                totalHigherGrades++;
            } else {
                break;
            }
        
        }
        System.out.println("Total number of random grades with higher numerical score than the entry: " + totalHigherGrades);
    }
        }
 