import java.util.Scanner;
public class Sales
{
//ToDo: write a method biggerThanTarget that takes two parameters,--> SalesArray(int[]) -- SalesTarget(int). The method returns the total number of sales person that returns 

public static int biggerThanTarget(int[]salesArray,int salesTarget){

int exceed = 0; //how many people exceed the target
//number of personas que sobrepasan el numero the sales
for(int i=0;i<salesArray.length;i++) {
if(salesArray[i]>salesTarget){
    System.out.println("SalesPerson " +i+ "sold: " +salesArray[i]);
    exceed ++;
    

}

}
return exceed;
}

public static void main(String[] args){
final int SALESPEOPLE = 5;
int[] sales = new int[SALESPEOPLE];
double sum;
Scanner scan = new Scanner(System.in);
for (int i=0; i<sales.length; i++)
    {
System.out.print("Enter sales for salesperson " + i + ": ");
sales[i] = scan.nextInt();

}
System.out.println("\nSalesperson  Sales");
System.out.println(" ------------------ "); 
sum = 0;
double max = 0; //this means that we start with 0, everytieme i find a bigger number, we update our max value to that
int indexofMax = -1;//para que i haga skip de una position 
double min =max;
int indexofMin=0;

for (int i=0; i<sales.length; i++)
    {
System.out.println("     " + i + "         " + sales[i]);
sum += sales[i];

//Encontrar el m'inimo y el m'aximo --> i representa la persona

if(sales[i]>max){ 
                     //sales value of this posiiton i, is greater than i
max = sales[i];
indexofMax = i;
}

if(sales[i]<min){
min=sales[i];
indexofMin=i;
}



}
System.out.println("\nTotal sales: " + sum);
double ave;
ave = sum/sales.length;
System.out.println("Average: " + ave);


System.out.println("Saleperson " + indexofMax +" had the highest sale with: " + max+ "$");
System.out.println("Saleperson " + indexofMin+" had the lowest sale with: " + min+ "$");
int totalExceed = biggerThanTarget(sales, 200);



}
}