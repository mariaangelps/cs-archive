//DECLARATIVAS

function miFuncion(){
    return 3;
}

miFuncion();
//Expresion 
var miFuncion =function(){
    return a+b
}

miFuncion();

function saludarEstudiantes(estudiante){ 
    console.log(estudiante);
}
saludarEstudiantes("Diego")//---> se est'a llamando a la funcion con parametro deigo, es como el valor de cuando i toma el valor de 2 


// Para que una funcion funcione como que en un loop con Distintos Datos,
// Es importante escribir la funcuin de tal manera que se abra como tipo un diccionario
// Con llaves y luego se llame a la funcion, EJEMPLO ----->
//
function saludarEstudiantes(estudiante){ console.log(`Hola ${estudiante}`);
}
saludarEstudiantes("Maria"); // entonces la funcion saldrá--> Hola Maria , Hola Diego, claro, evidentemente lo scacar'a de una fuente de datos.

//PERO QUE PASARÍA SI NO HAY FUENTE DE DATOS, DE DONDE SALDRÍAN LOS NOMBRES, WHAT IF I WANT TO GET A LIST THAT REPEATS THREE TIMES


//WE WANT A VALUE OF RETURN

function sumar(a,b){
    var result =a+b;
    return result;
}
sumar(1,2)//---> El resultado va a ser 3, se llama a la funcion con los parametros adentro
