public class Problem12F1 {
        public int [] eStatistics (String [] names){
            int [] freq = new int[names.length];
            char desireChar = 'e';
            for(int i=0;i<names.length;i++){
                int count = 0;
                for(int j = 0;j<names[i].length();j++)
                    if(names[i].charAt(j)== desireChar){
                count++;
                }
                freq[i]=count;
            }
            return freq;




        }





    public static void main(String[] args) {
        String[] names = {"Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"};
        Problem12F1 problem = new Problem12F1();
        int[] result = problem.eStatistics(names);

        // Imprime el array result
        System.out.println(java.util.Arrays.toString(result));
        }
    }













