A=[-1,2,3,4; 4,4,4,4; 3,3,2,1]

x1= 13.65;
switch x1
    case 13
        fprintf("you have more than 12")
    case 11
fprintf("si es que el  caso dice cambair x1=13 a 11, se pone as'i")
    case 9
fprintf("Y así sigue la cadena ")
    otherwise 
fprintf("other situation")
end 


 %we want to know if A(1,1)>0
 %And if A(3,4)=0

 if  A(1,1)> 0 | A(3,4)==0 %siempre se utiliza doble signo igual 
     % para que matlab no lo lea al código como si fuera
     % otro valor asignado a la variabale. If A(1,1)> 0 & A(3,4)==0
     %se utiliza el & para decir and o unir
     %Se utiliza | para que ese signo funcione como un "or" u "o"

     fprintf("All good")


 end

 