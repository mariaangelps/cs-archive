
%Maria Palacios 


%From Question 1 to Question 2 


%Question 1:Plot x versus y for y=sin(x).
%Let x vary from 0 to 2π in increments of 0.1π. 
%Add a title and label to your plot.


x= 0:0.1*pi:2*pi;
y=sin(x);
figure(1);
plot(x,y);
xlabel('Values of x from 0 to 2pi');
ylabel('Values for sine');
title('Figure 1, plot x and y');

%Question 2:Plot x versus y1 and y2 for y1 = sin(x) and y2 =cos(x).
%Let x vary from 0 to 2π in increments of 0.1π.
%Make the sin (x) line dashed and red. 
%Make the cos(x) line green and dotted. 
%Add a title and labels to your plot. 
%Also add a legend to this plot.

y1=sin(x);
y2=cos(x);
x= 0:0.1*pi:2*pi;
figure(2);
plot(x,y1,x,y2);
title('Figure 2, x,versus y1 and y2');
xlabel('values of x from 0 to 2pi');
ylabel('values for sine and cosine');
legend('sin(x)','cos(x)');





