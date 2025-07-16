/*Write  a methid called calcAverage that takes one parameter, called transcript, which is a 2-dimensional array of integers where each row
represents a course containing the scores of different assignments. 
cs113: 100,90
cs280: 85,80
The method returns [95.0,82.5]
public static ---calcAverage2(int[][]transcript)
*/


public class ArraysLab{ //se le pone double al calcaverage porque es average
    public static double calcAverage(int[][]transcript){
        int totalScore = 0;
        int numRows = transcript.length;
        int numColumns = transcript[0].length;

        for(int i=0;i<numRows;i++){
            for(int j = 0; j<numColumns;j++){
                totalScore+=transcript[i][j];
            }
        }
        return (double)totalScore/(numRows*numColumns); //casting
    }

    public static double calcAverage2(int[][]transcript){
        
        int r = transcript.length;
        int c = transcript[0].length;
        double []averages = new double[r]; //hasta aqu'i todo es 0, tengo qu epopular el array
      
        for(int row = 0;row<r;row++){
                int rowTotal=0;
                for(int column=0;column<c;column++){
                    total+=transcript[r][c];
                    //average for a row: (double)total/numColumns;
                    averages[r]=(double)total/c;

                }
                }
            return averages;

            }
        
        */
    
            // Coin method
    public static int coinStats (int size){
        Coin [] piggyBank = new Coin[size];
        int heads = 0;
        for (int coin = 0; coin< size; coin++){
            piggyBank[coin] = new Coin();
            piggyBank[coin].flip();
            System.out.println(piggyBank[coin]);
            if(piggyBank[coin].isHeads())heads++;

        }
        return heads;
    }    
}

    public static void main(String[]args){

        int[][] myTranscript = { {100,90,75,80},{65,98,85,89},{10,67,89,97}};
        double average = calcAverage(myTranscript); 
        System.out.println(average+"Average");

        double[][]courseAverages= calcAverage2(myTranscript);
        for(double avg:courseAverages);
        System.out.println("Each course average: ");
        System.out.print(" "+avg);



}

    




