//* File:     Errors.java
// Purpose: A program with lots of syntax errors
// Correct all of the errors (STUDY the program carefully!!)
#import java.util.Scanner; //---> este est'a mal porque se est'a empezando con el #y java no permite esto
public class errors
{//---> este est'a mal porque nunca se lo cerr'o
public static void main (String[] args)
{
String Name; / Name of the user // un solo "/" es divisi'on por lo tanto ir'ian 2 si es que se desea hacer un comentario. El name deberia ir en minuscula.
int number;
int numSq;
Scanner scan = new Scanner(System.in);
System.out.print ("Enter your name, please: ")//missing a semicolon
Name = scan.nextInt();//should be next or next line
System.out.print ("What is your favorite number?);"//---> falta cerrar comillas
number = scan.nextInt();
numSq = number * number;
System.out.println (Name  ", the square of your number is "//-> le falta un +
numSquared);//---> numSquared no est'a a'un declarada, solo el numSq, revisar bien el nombre de las variables
}
//*