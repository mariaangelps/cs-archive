%factorial? multiplicacion, factores

val1=5; %el num que queremos factorizar
tempval=1; %baseline value to operate on

for i=1:val1   %here goes from 1 to 5
    tempval=tempval*i;
    status1= [i, tempval]
    pause(1)
end 