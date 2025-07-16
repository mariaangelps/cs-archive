public class Arrays2d {
        public static void main(String[] args)
        {
            int[][] arr = new int[4][5];
            int counter = 0;

            for (int i = 0; i < arr.length; i++) // 4
            {
                for (int j = 0; j < arr[i].length; j++) // 5
                {
                    counter++;
                    arr[i][j] = counter;
                }
            }

            printArr(arr);
        }

        public static void printArr(int[][] arr)
        {
            for (int i = 0; i < arr.length; i++) // 4
            {
                for (int j = 0; j < arr[i].length; j++) // 5
                {
                    System.out.print(arr[i][j] + " ");
                }

                System.out.println();
            }
        }
    }

// 1d arr
// {0, 1, 2, 3}

// 2d arr
// {0  1  2, 3},
// {4  5  6  7},
// {8  9  10 11},
// {12 13 14 15}

// arr.length = 4
// arr[0].length = 3


