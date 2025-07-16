%Maria Angel Palacios 

%Question 3:
%Create a program that prompts the user to enter a value
%or the outside air temperature. 
%If the temperature is equal to or above 80 0F, wear shorts. 
% If temperature is between 60 0F and 80 0F, its a beautiful day. 
% If the temperature is equal to or below 60 0F, wear a jacket or a coat.


Temp= input('Enter the air temperature=')


if Temp>=80 
disp('Wear shorts')

elseif Temp>=60 & Temp<=80
    disp("Its a beautiful day outside")

elseif Temp<=60 
    disp("Wear a jacket or coat, its below 60")


end
