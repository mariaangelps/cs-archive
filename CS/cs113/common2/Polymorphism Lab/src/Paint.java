public class Paint {
        private double coverage;  //number of square feet per gallon
        //-----------------------------------------
//  Constructor:  Sets up the paint object.
//-----------------------------------------
        public Paint(double c)
        {
            coverage = c;
        }
        //---------------------------------------------------
//  Returns the amount of paint (number of gallons)
//  needed to paint the shape given as the parameter.
//---------------------------------------------------
        public double amount(Shape s)
        {
            System.out.println ("Computing amount for " + s); // s is an object, es como decir s.toString --> lo que significa (VER NOTAS)
            return s.area()/coverage;
        }

    }

