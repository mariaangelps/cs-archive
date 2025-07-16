public class Palindrome {
    public static void main (String[] args){
        System.out.println("The string \"" +args[0]+"\""+(pal(args[0])? "is": "is not")+" a plaindorme.");
    }
    public static boolean pal(String s){
        if(s.length()>1){
            if(s.charAt(0)==s.charAt(s.length()-1)){
                return pal(s.substring(1,s.length()-1));
            }
            return false;
        }
        return true;
    }
}
