t1= 1:20; %some time of measurement 
y1= 60+2*t1; %temperature 

%if y1>90* Air conditioner kicks in 


for i=1:20 % there are 20 entries in y1 %esto es la evaluación de un  matrix o un vector 
    if y1(i)>90
        y1(i)=88
    end
end 


figure(1)
plot (t1,y1)
