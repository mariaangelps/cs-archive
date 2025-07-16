public class TowerofHanoi {
    //1. Move n-1 disks from src to use
    //2. move the ntn disk from tower a (source) to tower c (destination)
    //3. Move the n-1 disk from use tower(b) to destination tower(c)
    //M(n) = 2^n-1
    //
    //M(n)= 0 , n=0 --> 0 disk, 0 moves
    //    = M(n-1) + 1
    //    = 2M(n-1) +1, when n>0
    //  M(n) = 2*M(n-1) +1
    //  M(n) = 2*(2*M(n-2)+1)+1
    //       = 4* M(n-2)+3
    //       = 4 *(2*M(n-3)+1)+3
    //       = 8 *  M(n-3)+7
    //       = 16 * M(n-4)+15
    //       = 2^k * M(n-k)+2^k-1
    //       let k = n
    //       = 2^n *


    //  M(3) = 2*M(2)+1
    //  M(2) = y continua
    //  M(3) = 7
    //  m(2) = 3
    //  m(1) = 1
    //  m(0) = 0

    public static void tower(int n, char src, char dst, char temp) {
        /*3 Steps
        1. Move n-1 disks from source tower to temp tower
        2. Move the n-th disk from src tower to destination tower
        3. Move the n-1 disks from the temp tower the dst tower

        M(n) = 2^n - 1 --> the minimum number of moves to solve

        Base Case: M(n) = 0; n = 0
                        =   2M(n-1) + 1; n > 0
        M(3) = 2 * M(2) + 1 --> 7
        M(2) = 2 * M(1) + 1 --> 3
        M(1) = 2 * M(0) + 1 --> 1
        M(0) = 0

        M(n) = 2 * M(n-1) + 1
             = 2 * (2 * M(n-2) + 1) + 1
             = 4 * M(n-2) + 3
             = 4 * (2 * M(n-3) + 1) + 3
             = 8 * M(n-3) + 7
             = 16 * M(n-4) + 15
             = 2^k * M(n-k) + 2^k - 1 --> the pattern
             let k = n
             = 2^n * M(0) + 2^n - 1
             = 2^n - 1 --> Proof that 2^n - 1 moves is the correct formula
        */

        if (n > 0) {
            //move the n-1 disks to the temp tower
            tower(n - 1, src, temp, dst);
            //move the n-th disk to the dst tower
            System.out.println("Move disk " + n + " from " + src + " to " + dst);
            //move the n-1 disk to the dst tower
            tower(n - 1, temp, dst, src);
        }
    }


    public static void main(String[] args) {
        tower(4, 'A', 'C', 'B');
    }




}
