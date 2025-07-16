import java.util.Scanner;

public class DriverBonus {
    public static void main(String[] args) throws BonusTooHigh{
        Scanner scan = new Scanner(System.in);

        System.out.println("Enter the number of employees: ");
        int numEmployees = scan.nextInt();

        StaffMember[] employees = new Executive[numEmployees];

        scan.nextLine();

        for(int i = 0; i < numEmployees; i++){

            System.out.println("Enter employee's name" + " " +(i + 1) +":");
            String name = scan.nextLine();

            System.out.println("Enter address of the employee"+ " " + (i + 1) +":");
            String address = scan.nextLine();

            System.out.println("Enter employee  " + (i + 1) +" phone number:");
            String number = scan.nextLine();

            System.out.println("Enter Employee  " + (i + 1) + " SSN:");
            String social = scan.nextLine();

            System.out.println("Enter Employee " + (i + 1) + " rate: ");
            double rate = scan.nextDouble(); scan.nextLine();

            System.out.println("Employee " + (i+1) + " data finished");

            employees[i] = new Executive(name, address, number, social, rate);
        }

        BonusTooHigh exception = new BonusTooHigh("Bonus too high");
        for(int i = 0; i < numEmployees; i++){
            System.out.println("Bonus to award: " + (i+1) );
            double bonus = scan.nextDouble(); scan.nextLine();

            if(bonus >= 10000){
                throw exception;
            }
            else{
                ((Executive)employees[i]).awardBonus(bonus);
            }
        }

        scan.close();

    }
}
