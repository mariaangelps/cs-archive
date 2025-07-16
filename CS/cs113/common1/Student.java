import java.util.Scanner;

public class Student
{
    //declare instance data
    private int test1, test2;
    private String name;

    //constructor
    public Student(String studentName)
    {
        name = studentName;
    }
    // ---------------------------------------------
    //inputGrades: prompt for and read in student's grades for test1 and test2.
    //Use name in prompts, e.g., "Enter's Joe's score for test1".
    // ---------------------------------------------
    public void inputGrades()
    {
        Scanner input = new Scanner(System.in);

        System.out.print("Enter " + name + "'s test 1 grade: ");
        test1 = input.nextInt();

        System.out.print("Enter " + name + "'s test 2 grade: ");
        test2 = input.nextInt();
    }
    // ---------------------------------------------
    //getAverage: compute and return the student's test average
    // ---------------------------------------------
    public double getAverage()
    {
        return (test1 + test2)/2.0;
    }
    // ---------------------------------------------
    //getName: print the student's name
    // ---------------------------------------------
    public String getName()
    {
        return name;
    }
}