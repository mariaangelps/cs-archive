x1=1:10;

%para sacar uno por uno, especificamente

for i=1:5
i;

x2(i)=x1(i)^i;

pause(1);  %empieza a correr el código de mamnera pausada, como que
          %uno por uno.


end 

results=[x1(1:5)',x2']