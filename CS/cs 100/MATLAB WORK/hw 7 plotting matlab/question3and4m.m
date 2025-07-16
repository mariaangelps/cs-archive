
%Maria Palacios 

%From question 3 to 4:


%Question 3: 
%Create an M-file to find the volume of a right circular cylinder. 
%V = π r 2 h . 
%Prompt the user to enter the values of r and h.

r= input('Enter r:');
h= input('Enter h:');
V= pi*(r)^2*h
a=input('Startpoint a:');
b=input('Endpoint b:');
c=input('Spacing for the variables, c:');
h=a:c:b

%Question4:
% a)Use the disp command to create a title for a 
% table that converts inches to feet.

disp('<strong>Inches to feet </strong>')


% b) Use the disp command to create column headings 
% for your table.

disp('inches feet')

% c)Create an inches vector from 0 to 120 with an increment of 10.

in= 0:10:120;

% d)Calculate the corresponding values of feet.

ft= in*0.833;   


% d) Group the inch vector and the feet vector together into a table matrix.

Conversionchart=[in', ft'];


% f) Use the fprintf command to send your table to the command window.


fprintf('%-5i %6.3f\n',Conversionchart')




