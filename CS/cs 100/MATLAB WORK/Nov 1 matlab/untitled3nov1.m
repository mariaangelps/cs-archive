A= zeros(4,4)

pause(5)

for i=1:4

    for j=1:4

    current=[i,j]
    A(i,j)=i*j;
    A 
    pause(2) %keep ony the odd numbers and replace the evens with 0

if mod (i*j,2)==0 %quedaría como (i multiplicado por j)/ para 2
    A(i,j)=0 



end
    end
 end 
 

 % mod(5,1) %el primero el numero que se quiere dividir, 