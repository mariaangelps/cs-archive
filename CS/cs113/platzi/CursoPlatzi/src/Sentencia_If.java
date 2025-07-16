public class Sentencia_If{


    public static void main(String[]args){
        boolean isBluetoothEnabled = false;
        int files = 3;
        if(isBluetoothEnabled){
            files++;
            System.out.println("Files sent");
        }
        else{
            files--;
            System.out.println("por favor enciende tu Bluetooth para iniciar la transferecnia");
        }
        System.out.println(files);
    }
}
