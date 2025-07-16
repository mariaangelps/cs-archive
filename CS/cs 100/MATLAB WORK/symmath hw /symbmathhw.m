
% Maria Angel Palacios Sarmiento
% Question 1:

x1 = 15; % Random number for the factorial
fact=1; 

for i=1:x1 
fact=fact*i;
pause(1)
output=[i,fact]
end

% Question 2:

x2=3 ; % number we want factorial of 
n3=4; 
fact2=2; 

while n3<=x2
fact2=fact2*n3;
output=[fact2,n3]
pause(1)
n3=n3+5 ;
end


% Question 3:
% Use solve function to solve these expressions
% a. x^2-1
% b. a*x^2 + b*x + c 
% c. cos(x)

syms x a b c 
a=2;
b=4;
c=1;

d=x^2-1
d2=a*x^2 + b*x + c 
d3=cos(x)

s2=solve(d2)

s1=solve(d)

s3=solve(d3)


% Question 4:
% Solve the following system of linear equations:
% a) 5x+6y -3z=10 
% b) 3x-3y+2z=14
% c) 2x-4y-12z=24


syms x y z
eq1= 5*x+6*y -3*z==10
eq2= 3*x-3*y+2*z==14
eq3= 2*x-4*y-12*z==24

[A B]= equationsToMatrix([eq1 eq2 eq3],[x, y, z])
R= linsolve(A,B)
R1= solve([eq1 eq2 eq3],[x y z])
solx=R1.x
soly=R1.y
Solz=R1.z

% Question 5: 
% Use ezplot to plot sin(x) from -2pi to +2pi.

syms x y1
y1=sin(x);
diff(y1,x)

axis([-2*pi 2*pi -1.5 1.5])
figure(1)
ezplot(y1)

% Question 6: 
% Find the first derivative with respect to x of the following expressions:
% x2 - x + 1
% sin(x) 
% tan(x) 
% ln(x)

syms x 
f = x^2 -x +1;
diff(f)
syms x1
f1 = sin(x);
diff(f1)
f2= tan(x) ;
diff(f2)
f3= log(x);
diff(f3)

% Question 7:
% Use a for loop to sum the elements in the following vector:

x = [1, 23, 43, 72, 87, 56, 98, 33];

sum= 0;
for n = 1:8
    sum = sum+x(n)
end 






