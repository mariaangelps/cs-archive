//my first program

public class MyProgram
{
   

   public static void main(String[] args)
   {
   
      //para que el code runs, tengo que llamar al method dentro del Main, sin necesidad de crear un object 
      System.out.println("Hello");
      MyMethods obj=new MyMethods();
      
      
      
      //test add method
      System.out.println(obj.add(5,9));
      
      //test rollTwo method
      Die die1=new Die();
      Die die2=new Die();
      int answer=obj.rollTwo(die1,die2);
      //call for a method
      //tb se puede hacer esto? ---> int answer = rollTwo(die1,die2);
      System.out.println(obj.rollTwo(die1,die2));
   
    }
    
    
    
    
  }