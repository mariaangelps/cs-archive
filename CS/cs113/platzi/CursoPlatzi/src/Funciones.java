public class Funciones{
    public static double CircleArea(double r){
        return Math.PI*Math.pow(r,2);
    }

    /**
     * Descripcion: Funcion que especificnado su moneda convierte
     * una cantidad de dinero a Dolares
     * @param quantity Cantidad de Dinero
     * @param currency tipo de Moneda, solo valida para pesos MEX o Ccolombianos, y otro de defualt
     * return quantity  Devuelve la cantidad actualizada en Dolares
     */

    public static double ConvertoDollar(double quantity, String currency){
        //switch statment
        switch(currency){
            case "Mex": quantity=quantity*0.052;break;
            case "Colombian": quantity=quantity*0.00031;break;
            default : quantity=quantity*67;break;
        }
    return quantity; //acordarse de retornar, porque no hay un void

    }
    public static void main(String[]args){
        double area = CircleArea(3.8);
        System.out.println("tHE CIRCLE AREA IS: "+ area);
        double moneda = ConvertoDollar(5679.97,"Ecuadorian");
        System.out.println(moneda);

    }
}