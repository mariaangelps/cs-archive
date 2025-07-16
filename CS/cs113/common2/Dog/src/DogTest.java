
public class DogTest {
    public static void main(String[] args) {
//Dog dog = new Dog("Spike");
//System.out.println(dog.getName() + " says " + dog.speak());
//LAS COMENTAMOS A LAS DE ARRIBA PORQUE NO SE PUEDE INSTANTIATE ABSTRACT CLASSES
//create an object for the labrador

        Labrador labrador = new Labrador("Luna", "Dorado");
        System.out.println(labrador.getName() + "says" + labrador.speak());
        System.out.println("Average Weight: " + labrador.avgBreedWeight());

//CREATE OBJECT FOR YORKSHIRE
        Yorkshire perrito2 = new Yorkshire("Lulu");
        System.out.println(perrito2.getName() + "says");
        System.out.println("Average weight del Yorkshire: " + perrito2.avgBreedWeight());

    }
}
/*when you dont change the size, or get bigger size, you move lejos del recursive method
public static int recurse(int n){
    int result = 1;
    int rec=2;
    if (n< 2) {
        result = (n - 1) * rec;
        return result;
    }
}


public static int rose(int n){
    if(n<=0) {
        return 1;
    }
    else{
        return rose(n-1)*n; //se acerca cada vez m'as al cero
    }
}
/* rose(4) =
rose(4) = rose(3)*4
rose(3) = rose(2)*3
rose(2) = rose(1)*2
rose(1) = rose(0)*1


 */

