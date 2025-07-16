public class LeerFiles {
    public static void main(String[] args) {

        //an array of integers
        Integer[] a = {12 ,23 ,34 ,45, 56, 67, 78, 89 ,90};

        System.out.println(ssearch(a, 45));
        System.out.println(ssearch(a, 46));

        System.out.println(bsearch(a, 45));
        System.out.println(bsearch(a, 46));

    }

    // the <E> is Generic
    //Comparable is compareTo method
    //Sequential Search
    public static <E extends Comparable<E>> int ssearch(E[] arr, E key) {
        return ssearch(arr, key, 0);
    }

    private static <E extends Comparable<E>> int ssearch(E[] arr, E key, int index) {
        //if the array is not empty run whats in the if statement
        if(index < arr.length) {
            if(key.compareTo(arr[index]) == 0) {
                return index;
            }
            return ssearch(arr, key, index + 1);//check the next index of its not the one we are looking for
        }
        //if the array is empty or the number is not in the array return -1
        return -1;
    }

    //Binary Search
    public static <E extends Comparable<E>> int bsearch(E[] arr, E key) {
        return bsearch(arr, key, 0, arr.length-1);
    }

    private static <E extends Comparable<E>> int bsearch(E[] arr, E key, int left, int right) {
        if(left <= right) {
            int cmp, middle = (left + right) / 2;
            if((cmp = key.compareTo(arr[middle])) == 0) {
                return middle;
            }
            else if(cmp < 0) {
                return bsearch(arr, key, left, middle - 1);
            }
            else {
                return bsearch(arr, key, middle + 1, right);
            }
        }
        return -1;
    }
}
