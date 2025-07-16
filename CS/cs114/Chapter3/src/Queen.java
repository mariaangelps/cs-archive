public class Queen {
// Terminal Symbols = {a,b}
//N = {<A>}
//PRODUCTION RULES
//<A> --> ab| a<A>B
        // "aaabbb" \in L(G)? --> True
        //<A> --> a<A>b
        //      --> aa<A>bb
        //      --> aaa<A>bbb
//"aaabb" \in L(G) ? False, no está dentro del language
//"aababb" False, no puede existir un a depsues de una b
// l{W : W consists of n 'a's followed by the same number of 'b's

//We want to recognize strings mas que crearlas, reconcer que sean del mismo "idioma"
// OBJECT L: language we are describing using our grammas

//CREATE IDENTIFIER GRAMMAR:
        //       <I> --> <L> |<L><S>
        //      <D> --> 0| ...| 9
        //       <S> --> <L> | <D> | <L><S> | <D><S>
        //    <L> --> a|...|Z

    //lior's notes
    //4 queen problem: cannot have a queen see another queen
    //. q . .
    //. . . q
    //q . . .
    //. . q .

    /*
    Basics to Grammarr or making a language
    Terminal Symbols t = {a, b}
    non-terminal Symbols = {<A>}

    production rules
    <A> => ab | a<A>b

    L = {w : w consists of n a's followed by the same number of b's}

    "aaabbb" in L(G)? This is true (We proved it)
    "aaabb" in L(G)? False
    "aababb" in L(G)? False

    <A> -> a<A>b
        -> aa<A>bb
        -> aaabbb
    */

    /* I = identifier; S = String; D = Digit; L = Letter
     <I> => <L> | <L><S>
     <S> => <L> | <D> | <L><S> | <D><S>
     <L> => a | ... | z (a-z any letter)
     <D> = > 0 | ... | 9 (0-9 any number)
     */
    static String s;
    public static boolean I() {
        if(L()) {
            if(S()) {
                return true;
            }
            return true;
        }
        return false;
    }

    public static boolean S() {
        if(L()) {
            if(S()) {
                return true;
            }
            return true;
        }
        else if (D()) {
            if(S()) {
                return true;
            }
            return true;
        }
        return false;
    }

    public static boolean L() {
        return false;
    }

    public static boolean D() {
        int i=0;
        if( i < s.length() && '0' <= s.charAt(i) && s.charAt(i) <= '9') {
            ++i;
            return true;
        }
        return false;
    }


    //Palindromes
    public static boolean pal(String s) {
        if(s.length() > 1) {
            if(s.charAt(0) == s.charAt(s.length()-1)) {
                return pal(s.substring(1, s.length()-1));
            }
            return false;
        }

        return true;
    }
    public static void main(String[] args) {
        System.out.println("The string \"" + args[0] + "\"" + (pal(args[0]) ? "is" : "is not") + " a palindrome." );
    }
}






