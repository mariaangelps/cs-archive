/*Write a program that declares and initializes a variable representing a made-up temperature in Fahrenheit 
The program will print to the screen both the Fahrenheit temperature and the equivalent Celsius temperature.
     For example, if temperature is set up to 36.5, a sample program output would be:

     Temp in Fahrenheit: 36.5, Temp in Celsius: 2.5

 

Write a program that will ask the user to enter the total number of seconds. The method will print the number of hours,
 minutes and seconds that make up that total.
 */



public class Temp{
    public static void main(String[]args){
    double temp = 36.5;
    double tempC= temp-32*(5/9);

    System.out.println("Temp in celsius:-->"+tempC + "temp in fahr: "+ temp);
    }
    

}