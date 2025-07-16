public class IntegerList {
 int[] list; //values in the list
    //-------------------------------------------------------
    //create a list of the given size
    //-------------------------------------------------------
   public int maxSize =5;

    public IntegerList(int size, int[] list)
    {
        list = new int[size];
        this.list = list;
    }


    //-------------------------------------------------------
        //fill array with integers between 1 and 100, inclusive
        //-------------------------------------------------------
    public void randomize()
    {
        for (int i=0; i<list.length; i++)
            list[i] = (int)(Math.random() * 100) + 1;
        }
        //-------------------------------------------------------
        //print array elements with indices
        //-------------------------------------------------------

    public static void increaseSize(){
        IntegerList size = new IntegerList(5,new int[3]);
    }
    public void addElement(int newVal){
        if(list.length==maxSize){
            increaseSize();
        }
    }
    public void print()
    {
        for (int i=0; i<list.length; i++)
            System.out.println(i + ":\t" + list[i]);
    }

}

