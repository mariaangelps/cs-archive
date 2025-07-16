public class LogicOperators {

    /**
     *
     * @return boolean, lo que dependa la condicion, si es falsa false, si es v true
     */
    public static boolean condition() {
        int a = 9;
        int b = 11;
        if (a > b) {
            return true;
        } else {
            return false;
        }
    }


        public static void main (String[]args){
            int a = 8;
            int b = 5;

            System.out.println("Es a igual a b?" + (a == b));
            System.out.println("A es diferent a b?" + (a != b));
            condition();
            System.out.println(condition());

        }

    }

