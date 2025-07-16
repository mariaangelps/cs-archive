
//Problem 2. Implement a class called BonusTooHighException,
// designed to be thrown when a bonus value is greater than $10000.
// Using the Executive class from Chapter 10, create a main program
// that creates and populates an Executive array with information
// entered by the user (array size as well).
// If a bonus value is entered that is too high, i.e. greater than
// $10000 throw the exception.
// Allow the thrown exception to terminate the program.

import java.util.Scanner;
public class BonusTooHigh extends Exception {
    public BonusTooHigh(String message) {
        super(message);
    }
}



