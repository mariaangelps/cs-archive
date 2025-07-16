public class Executive extends Employee {
    //  Represents an executive staff member, who can earn a bonus.
//******************************************************************

        private double bonus;
        //-----------------------------------------------------------------
//  Sets up an executive with the specified information.
//-----------------------------------------------------------------
        public Executive (String eName, String eAddress, String ePhone,
                          String socSecNumber, double rate)
        {
            super (eName, eAddress, ePhone, socSecNumber, rate);
            bonus = 0;  // bonus has yet to be awarded
          int vacations =10;
        }
        //-----------------------------------------------------------------
//  Awards the specified bonus to this executive.
//-----------------------------------------------------------------
        public void awardBonus (double execBonus) {

            bonus = execBonus;
        }
        //-----------------------------------------------------------------
//  Computes and returns the pay for an executive, which is the
//  regular employee payment plus a one-time bonus.
//-----------------------------------------------------------------
        public double pay()
        {
            double payment = super.pay() + bonus;
            bonus = 0;
            return payment;
        }

        //PROBLEM 1
    @Override
    public int getVacation() {
        return super.getVacation();
    }
}

