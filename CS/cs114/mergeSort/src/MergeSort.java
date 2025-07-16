public class MergeSort {
    //in place, does it use the original memory
    //                      best        avg     worst    in place?       stable?
    // bubble               n           n^2     n^2        true            true
    // insert               n           n^2     n^2        true            true
    // select               n^2         n^2     n^2        true            true
    // merge                nlgn        nlgn    nlgn       false           true
    // quick
    // heap




    //03 06 15 09 12 11 13 08 16 10 04 05 02 01 07 14
    //03 06 15 09 12 11 13 08| 16 10 04 05 02 01 07 14
    //03 06 09 15| 12 11 13 08
    //i
    //03 06| 15 09
    //l  r
    //03.06

    //we icnrement i, 3 is
    //   i
    //03 06| 15 09

    // .. ..
    // x  y  --> 2 elements, comp 1

    //.. .. .. ..
    //01 03.02 04 --> 4 elements, comp 3

    //.. .. .. .. .. .. .. ..
    //01 03 05 07.02 04 06 08 --> 8 elemensts, comp 7
    //                        --> n elements, comp n-1
    //                        --> 16 elements, times we split in half: 4 times
    //                        -->  n elements, times we split it half: log(n) times [ 0(n) * 0(nlogn)]

}
