//HOISTING EN VARIABLES//

console.log(miNombre);//--> funcion que nos ayuda a imprimir los resultados en la consola 
var miNombre; //--> esto es declarar una variable
miNombre="Maria";//--> esto es inicializar una variable 


//Ahora un contraejemplo de lo que pasa si es que mandamos a llamar 
//una variable antes de declrarla e inicializarla:

//1. vamos a llamar la variable de miNombre en la consola:
console.log(miNombre);

//2. vamos a declarar una variable e inicialzarla:
var miNombre="maria";

/*El return de esta función va a ser "Undefined" --> pero why?
El hecho por el que este sale undefined es porque se produce el HOISTING
Es decir, que java le da un valor e inicializa el valor de la variable por si mismo
En otras palabras, lo que hace Java sería:
1. okay veo la primera linea de código y veo que se está llamadno a una variable,
entonces busco mi variable, y como NO LA ENCUENTRO, entonces yo mismo la declaro.
Bien una vez que la declara, se da cuenta que debe inicializarla y darle un valor, 
pero entonces se choca y ve que no sabe que valor asignarle ya que el usuario no le dio ningun valor,
therefore JS procede a darle el valor de undefined, es por tal razón que no sale un Error.

En código pasar'ia esto :*/
var miNombre= undefined;
console.log(miNombre) 

/* Código que respresenta lo que sucede dentro de java, o sea la primera
linea es solo que sale en el jit compilor, de ahí lo demas es como we should fix it.  

var miNombre=undefined;
console.log(miNombre);
miNombre= "Maria"; */


//HOISTING EN FUNCIONES//

//1. se est'a mandando a llamar antes de inicializarla:

hey();
function hey(){
    console.log("Hola "+miNombre);
}
var miNombre="Maria "

//2. EL RESULTADO VA A SALIR HOLA MARIA 
