
%Maria Palacios 
%Question 5:

% Create a variable of name D that represents dollars. 
%In intervals from 0 to 15, with a spacing of 1.
D= 0:1:15;  


%Create a variable that represents Euro, Pounds and Japanese Yen, each one
%with its corresponding value of conversion.

Euro= D*1.01;
GBP= D*0.86;
JPY= D*147.64;

%Use the the disp command to create the chart headings and columns names.
disp('<strong> Currency Chart </strong>')

disp('Euro  GBP  JPY')

%Group the Euro vector, GBP and JPY vector together into a table matrix.

Currencychart=[Euro', GBP', JPY'];

%Use the fprintf command to print the table to the command window.

fprintf('%2.2f %2.2f %2.2f\n' ,[Euro(:),GBP(:),JPY(:)].')