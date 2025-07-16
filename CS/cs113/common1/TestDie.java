public class TestDie{

   public static void main(String[] args){
   
      Die die1= new Die(); //constructor--> die1 solo tiene un adress 
      System.out.println(die1.getFaceValue());//-> del die1, toma el facevalue, permite el acceso al die1 
      die1.roll(); //method call, no lo ponemos en prinln porque esto no retorna nada 
      System.out.println(die1.getFaceValue());//vemos las caras luego de tirarlos(dados)'
      die1.setFaceValue(2);
      System.out.println(die1.getFaceValue());

   }
 }
   