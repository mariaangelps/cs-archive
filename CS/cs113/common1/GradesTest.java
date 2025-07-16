import java.util.Scanner;
import java.util.Random;

public class GradesTest {
public static void main(String[] args) {
Random gen=new Random();
Scanner scan=new Scanner(System.in);
System.out.println("Enter your score: ");
Grade entry=new Grade(scan.nextInt());
System.out.println(entry);
Grade grade=new Grade(gen.nextInt(61)+40);
System.out.println(grade);
int count=0;
while (grade.equals(entry)){
if (grade.getNumGrade()>entry.getNumGrade())
count++;
grade=new Grade(gen.nextInt(61)+40);
System.out.println(grade);
}
System.out.println(count);
}
}
