// **************************************************
// StringPlay.java
//
// Play with String objects
// **************************************************
public class StringPlay
{
   public static void main (String[] args)
   {
   String town =  "Anytown USA";
   
   stringLength=college.length();
   System.out.prinln(college+"contains"+stringLength);
   //________________________________________________________; // part (a)
    int stringLength;
   String change1, change2, change3;
   //________________________________________________________; // part (b)
   stringLength=college.length();
   System.out.println (college + " contains " + stringLength + " characters.");
   //changel = _____________________________________________; // part (c)
   change1=college.toUpperCase();
   //change2 = _____________________________________________; // part (d)
   change2=change1.replace('0','*');
   //change3 = _____________________________________________; // part (e)
   change3=college.concat(town);
   System.out.println ("The final string is " + change3);
   }
}